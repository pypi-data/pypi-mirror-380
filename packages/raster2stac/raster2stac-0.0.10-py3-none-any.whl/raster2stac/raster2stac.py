"""
Raster2STAC - Generate STAC metadata from raster data

This module provides a class `Raster2STAC` for extracting from raster data, represented as an `xr.DataArray`
or a file path to netCDF(s) file(s), SpatioTemporal Asset Catalog (STAC) format metadata JSON files.

Authors: Mercurio Lorenzo, Eurac Research - Inst. for Earth Observation, Bolzano/Bozen IT
Authors: Michele Claus, Eurac Research - Inst. for Earth Observation, Bolzano/Bozen IT
Authors: Suriyah Dhinakaran, Eurac Research - Inst. for Earth Observation, Bolzano/Bozen IT
"""

import datetime
import json
import logging
import os
from copy import copy, deepcopy
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse, urlunparse

import s3fs
from s3fs import S3FileSystem
import boto3
import botocore
import dask
import numpy as np
import pandas as pd
import pystac
import rasterio

import ujson
import xarray as xr
from fsspec.implementations.local import LocalFileSystem
from openeo.local import LocalConnection
from pystac.utils import str_to_datetime

# Import rio_stac methods
# Import extension version
from rio_stac.stac import (
    EO_EXT_VERSION,
    PROJECTION_EXT_VERSION,
    RASTER_EXT_VERSION,
    bbox_to_geom,
    get_dataset_geom,
    get_eobands_info,
    get_projection_info,
    get_raster_info,
)

from .rioxarray_stac import (
    rioxarray_get_dataset_geom,
    rioxarray_get_projection_info,
    rioxarray_get_raster_info,
)

_log = logging.getLogger(__name__)


DATACUBE_EXT_VERSION = "v2.2.0"


class Raster2STAC:
    """
    Raster2STAC Class - Convert raster data format into STAC metadata.

    Args:
        data: str or xr.DataArray
            Raster data as xr.DataArray or file path referring to a netCDF file.
        collection_id: str
            Identifier of the collection as a string (Example: 'blue-river-basin')
        collection_url: str
            Collection URL (must refer to the FastAPI URL where this collection will be uploaded).
        item_prefix: Optional[str] = ""
            Prefix to add before the datetime as item_id, if the same datetime can occur in multiple items.
        output_folder: Optional[str] = None
            Local folder for rasters and STAC metadata outputs. Default folder will be set as run timestamp folder
            (ex: ./20231215103000/)
        description: Optional[str] = ""
            Description of the STAC collection.
        title: Optional[str] = None,
            Title of the STAC collection.
        ignore_warns: Optional[bool] = False,
            If True, warnings during processing (such as xr lib warnings) will be ignored.
        keywords: Optional[list] = None,
            Keywords associated with the STAC item.
        providers: Optional[list] = None,
            Data providers associated with the STAC item.
        stac_version: str = "1.0.0",
            Version of the STAC specification to use.
        s3_upload: bool = True,
            If True, upload files to Amazon S3 Bucket.
            1. For the "COG" output format: upload to S3 the COG files
            2. For the "KERCHUNK" output format: upload the netCDFs and the json Kerchunk files to S3.
        bucket_name: str = None,
            Part of AWS S3 configuration: bucket name.
        bucket_file_prefix: str = None,
             Part of AWS S3 configuration: prefix for files in the S3 bucket.
        aws_region: str = None,
             Part of AWS S3 configuration: AWS region for S3.
        version: Optional[str] = None,
            Version of the STAC collection.
        license: Optional[str] = None,
            License information about STAC collection and its assets.
        sci_citation: Optional[str] = None
            Scientific citation(s) reference(s) about STAC collection.
        write_collection_assets = False,
            Include all assets in the STAC Collection, with unique keys.
    """

    def __init__(
        self,
        data,
        collection_id,
        collection_url=None,
        item_prefix: Optional[str] = "",
        output_folder: Optional[str] = None,
        description: Optional[str] = "",
        title: Optional[str] = None,
        ignore_warns: Optional[bool] = False,
        keywords: Optional[list] = None,
        providers: Optional[list] = None,
        links: Optional[list] = None,
        stac_version="1.0.0",
        s3_upload=False,
        bucket_name=None,
        bucket_file_prefix=None,
        aws_region=None,
        aws_access_key=None,
        aws_secret_key=None,
        version=None,
        license=None,
        sci_doi=None,
        sci_citation=None,
        write_collection_assets=False,
        s3_endpoint_url=None,  # Optional argument
    ):
        if ignore_warns:
            import warnings

            warnings.filterwarnings("ignore")

        self.data_ds = None
        self.X_DIM = None
        self.Y_DIM = None
        self.T_DIM = None
        self.B_DIM = None
        self.OTHER_DIMS = None
        self.media_type = None

        self.properties = {}  # additional properties to add in the item
        self.collection_id = (
            collection_id  # name of collection the item belongs to
        )
        self.collection_url = collection_url
        self.item_prefix = item_prefix
        self.description = description
        self.keywords = keywords
        self.providers = providers
        self.links = links
        self.stac_version = stac_version
        self.sci_doi = sci_doi
        self.write_collection_assets = write_collection_assets
        self.extensions = [
            f"https://stac-extensions.github.io/projection/{PROJECTION_EXT_VERSION}/schema.json",
            f"https://stac-extensions.github.io/raster/{RASTER_EXT_VERSION}/schema.json",
            f"https://stac-extensions.github.io/eo/{EO_EXT_VERSION}/schema.json",
        ]

        if output_folder is not None:
            self.output_folder = output_folder
        else:
            self.output_folder = datetime.datetime.utcnow().strftime(
                "%Y%m%d%H%M%S%f"
            )[:-3]

        self.output_file = f"{self.collection_id}.json"

        Path(self.output_folder).mkdir(parents=True, exist_ok=True)

        self.stac_collection = None
        self.bucket_name = bucket_name
        self.bucket_file_prefix = bucket_file_prefix
        self.aws_region = aws_region
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.s3_endpoint_url = s3_endpoint_url  # added newly
        self.s3_client = None
        self.version = version
        self.title = title
        self.license = license
        self.sci_citation = sci_citation
        self._input_source = data
        self._data = None  # Will lazy-load when needed
        self.s3_upload = s3_upload
        if self.s3_upload:
            # Initialize S3 client (supports both AWS & custom endpoints)
            s3_config = {
                "aws_access_key_id": aws_access_key,
                "aws_secret_access_key": aws_secret_key,
            }

            # Only add endpoint settings if provided (otherwise use AWS default)
            if s3_endpoint_url:
                s3_config["endpoint_url"] = s3_endpoint_url
                s3_config["config"] = botocore.client.Config(
                    s3={"addressing_style": "path"}
                )
            self.s3_client = boto3.client("s3", **s3_config)

        if isinstance(
            self._input_source, (str, Path)
        ):  # Removing this block of code still runs, but this block of code helps user to not re-write again the same data in the same s3/https based bucket, which is simply over-writing!!!
            path_str = str(self._input_source)
            if path_str.startswith("s3://") or path_str.startswith("https://"):
                if self.s3_upload:
                    raise ValueError(
                        "The 's3_upload' argument must be set to False when using a remote input source (starting with 'https://' or 's3://')."
                    )

    def _ensure_crs(self):
        """Ensure the dataset has a valid CRS by checking all standard locations."""

        def _extract_crs(data):

            if isinstance(data, list):
                return None
            """Helper to extract CRS from an xarray object"""
            # 1. Check rioxarray's native CRS first
            if hasattr(data, "rio") and data.rio.crs is not None:
                return data.rio.crs

            # 2. Check for CF-compliant 'crs' variable (only for Dataset)
            if isinstance(data, xr.Dataset) and "crs" in data.variables:
                crs_var = data["crs"]
                # Check common CF attributes
                for attr in ["crs_wkt", "spatial_ref", "EPSG_code"]:
                    if attr in crs_var.attrs:
                        return crs_var.attrs[attr]

            # 3. Check global attributes
            for attr in ["crs_wkt", "spatial_ref", "EPSG_code", "proj4"]:
                if attr in data.attrs:
                    return data.attrs[attr]

            # 4. Check GDAL-style grid_mapping (only for Dataset)
            if isinstance(data, xr.Dataset) and "grid_mapping" in data.attrs:
                grid_var = data[data.attrs["grid_mapping"]]
                if "crs_wkt" in grid_var.attrs:
                    return grid_var.attrs["crs_wkt"]

            return None

        if self._data is None:
            return

        # Try to get CRS from main data
        crs = _extract_crs(self._data)

        # Fallback to checking dataset if available
        if (
            crs is None
            and hasattr(self, "data_ds")
            and self.data_ds is not None
        ):
            crs = _extract_crs(self.data_ds)

        if crs is None:
            raise ValueError(
                "No valid CRS information found. Checked:\n"
                "1. rioxarray's native CRS\n"
                "2. 'crs' variable with standard attributes (crs_wkt, spatial_ref, EPSG_code)\n"
                "3. Global attributes (crs_wkt, spatial_ref, EPSG_code, proj4)\n"
                "4. CF grid_mapping variable\n"
                "\nPlease add CRS using one of these methods:\n"
                "- data.rio.write_crs('EPSG:xxxx')\n"
                "- Add 'crs_wkt' attribute to a 'crs' variable\n"
                "- Set global 'crs_wkt' attribute"
            )

        # Ensure CRS is set in rioxarray
        if hasattr(self._data, "rio") and self._data.rio.crs is None:
            self._data.rio.write_crs(crs, inplace=True)

        # Sync with dataset if exists
        if (
            hasattr(self, "data_ds")
            and self.data_ds is not None
            and hasattr(self.data_ds, "rio")
            and self.data_ds.rio.crs is None
        ):
            self.data_ds.rio.write_crs(crs, inplace=True)

    @property
    def data(self):
        """Lazy-loading property that returns a DataArray, maintaining sync with data_ds"""
        if self._data is None:
            if hasattr(self, "data_ds") and self.data_ds is not None:
                # Convert existing Dataset to DataArray
                self._data = self.data_ds.to_dataarray(dim="bands")
            elif isinstance(self._input_source, (xr.Dataset, xr.DataArray)):
                if isinstance(self._input_source, xr.Dataset):
                    self.data_ds = self._input_source
                    self._data = self.data_ds.to_dataarray(dim="bands")
                else:  # DataArray
                    self._data = self._input_source
                    self.data_ds = self._data.to_dataset(
                        dim=self._data.openeo.band_dims[0]
                    )
            elif isinstance(self._input_source, (str, Path)):
                path_str = str(self._input_source)
                if path_str.endswith(".zarr"):
                    self.data_ds = xr.open_zarr(
                        path_str,
                        storage_options=(
                            {
                                "client_kwargs": {
                                    "endpoint_url": self.s3_endpoint_url
                                }
                            }
                            if path_str.startswith("s3://")
                            else {}
                        ),
                        consolidated=True,
                    )
                    self._data = self.data_ds.to_dataarray(dim="bands")
                else:
                    self.data_ds = xr.open_dataset(
                        path_str, decode_coords="all"
                    )
                    self._data = self.data_ds.to_dataarray(dim="bands")
            elif isinstance(self._input_source, list):
                self._data = self._input_source
            else:
                raise ValueError(
                    f"Unsupported input type: {type(self._input_source)}"
                )

            if not isinstance(self._data, list):
                self._ensure_crs()
        return self._data

    @data.setter
    def data(self, value):
        """Setter that maintains sync between DataArray and Dataset"""
        if isinstance(value, xr.Dataset):
            self.data_ds = value
            self._data = value.to_dataarray(dim="bands")
        elif isinstance(value, xr.DataArray):
            self._data = value
            self.data_ds = value.to_dataset(dim=value.openeo.band_dims[0])
        elif isinstance(value, list):
            self._data = value
        else:
            raise ValueError(
                "Input must be xarray Dataset or DataArray or a list of path"
            )

    def fix_path_slash(self, res_loc):
        return res_loc if res_loc.endswith("/") else res_loc + "/"

    # TODO/FIXME: maybe better to put this method as an external static function? (and s3_client attribute as global variable)
    def upload_s3(self, file_path):
        if self.s3_client is not None:
            prefix = self.bucket_file_prefix
            file_name = os.path.basename(file_path)
            object_name = f"{self.fix_path_slash(prefix)}{file_name}"

            try:
                self.s3_client.upload_file(
                    file_path, self.bucket_name, object_name
                )
                _log.debug(
                    f"Successfully uploaded {file_name} to {self.bucket_name} as {object_name}"
                )
            except botocore.exceptions.NoCredentialsError:
                _log.debug(
                    "AWS credentials not found. Make sure you set the correct access key and secret key."
                )
            except botocore.exceptions.ClientError as e:
                _log.debug(
                    f'Error uploading file: {e.response["Error"]["Message"]}'
                )

    def upload_s3_for_nc(self, file_path):
        if self.s3_client is not None:
            prefix = self.bucket_file_prefix
            file_name = os.path.basename(file_path)
            object_name = f"{prefix}{file_name}"

            try:
                self.s3_client.upload_file(
                    file_path, self.bucket_name, object_name
                )
                _log.debug(
                    f"Successfully uploaded {file_name} to {self.bucket_name} as {object_name}"
                )
            except botocore.exceptions.NoCredentialsError:
                _log.debug(
                    "AWS credentials not found. Make sure you set the correct access key and secret key."
                )
            except botocore.exceptions.ClientError as e:
                _log.debug(
                    f'Error uploading file: {e.response["Error"]["Message"]}'
                )

    def get_root_url(self, url):
        parsed_url = urlparse(url)
        # Extract protocol + domain
        root_url = urlunparse(
            (parsed_url.scheme, parsed_url.netloc, "", "", "", "")
        )
        return root_url

    def _upload_zarr_directory(self, zarr_path, item_id):

        import s3fs

        """Upload a local Zarr directory to S3"""
        s3 = s3fs.S3FileSystem(
            key=self.aws_access_key,
            secret=self.aws_secret_key,
            client_kwargs={"region_name": self.aws_region},
        )

        dest_path = f"{self.bucket_name}/{self.fix_path_slash(self.bucket_file_prefix)}{item_id}.zarr"

        # Recursively upload all files in the Zarr directory
        for root, _, files in os.walk(zarr_path):
            for file in files:
                local_path = os.path.join(root, file)
                relative_path = os.path.relpath(local_path, zarr_path)
                s3_path = f"{dest_path}/{relative_path}"
                with open(local_path, "rb") as f:
                    self.s3_client.put_object(
                        Bucket=self.bucket_name,
                        Key=f"{self.fix_path_slash(self.bucket_file_prefix)}{item_id}.zarr/{relative_path}",
                        Body=f,
                    )

    def _copy_zarr_locally(self, zarr_path, item_id):
        """Copy a Zarr directory to the output folder"""
        import shutil

        dest_path = os.path.join(self.output_folder, f"{item_id}.zarr")
        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(zarr_path, dest_path)

    def _get_s3fs_with_endpoint_support(self):
        """Returns an S3FileSystem configured for AWS or custom endpoints."""
        s3_kwargs = {
            "key": self.aws_access_key,
            "secret": self.aws_secret_key,
            "default_fill_cache": False,
        }

        # Custom endpoint (EODC)
        if hasattr(self, "s3_endpoint_url") and self.s3_endpoint_url:
            s3_kwargs.update(
                {
                    "client_kwargs": {
                        "endpoint_url": self.s3_endpoint_url,
                        "region_name": self.aws_region,
                    },
                    "config_kwargs": {"s3": {"addressing_style": "path"}},
                }
            )
        # Default AWS
        else:
            s3_kwargs["client_kwargs"] = {"region_name": self.aws_region}

        return S3FileSystem(**s3_kwargs)

    def _get_s3_link_path(self, item_id):
        """Returns the correct S3 URL (AWS or custom endpoint)."""
        if hasattr(self, "s3_endpoint_url") and self.s3_endpoint_url:
            # Custom endpoint (EODC-style URL)
            return f"s3://{self.bucket_name}/{self.fix_path_slash(self.bucket_file_prefix)}{item_id}.zarr"
        else:
            # Default AWS URL
            return f"https://{self.bucket_name}.{self.aws_region}.amazonaws.com/{self.fix_path_slash(self.bucket_file_prefix)}{item_id}.zarr"

    def _get_s3_link_path_netcdf(self, filename):
        """Returns the correct S3 URL for netCDF files (AWS or custom endpoint)."""
        if hasattr(self, "s3_endpoint_url") and self.s3_endpoint_url:
            # Custom endpoint URL
            return f"s3://{self.bucket_name}/{self.bucket_file_prefix}{os.path.basename(filename)}"
        else:
            # Default AWS URL
            return f"https://{self.bucket_name}.s3.{self.aws_region}.amazonaws.com/{self.bucket_file_prefix}{os.path.basename(filename)}"

    def generate_kerchunk_stac(self):
        from kerchunk.hdf import SingleHdf5ToZarr

        def gen_json(u, so, json_dir):
            fs = LocalFileSystem(skip_instant_cache=True)
            with fs.open(u, **so) as inf:
                h5chunks = SingleHdf5ToZarr(inf, u, inline_threshold=300)
                with open(
                    f"{str(json_dir)}/{u.split('/')[-1]}.json", "wb"
                ) as outf:
                    outf.write(ujson.dumps(h5chunks.translate()).encode())
            return f"{str(json_dir)}/{u.split('/')[-1]}.json"

        # Create the output folder for the Kerchunk files
        kerchunk_folder = os.path.join(self.output_folder, "kerchunk")
        Path(kerchunk_folder).mkdir(parents=True, exist_ok=True)

        kerchunk_files_list = []
        # Read the list of netCDFs
        for same_time_netcdfs in self.data:
            t_labels = []
            for var in same_time_netcdfs:
                source_nc = var
                source_path = os.path.dirname(var)
                local_conn = LocalConnection(source_path)
                tmp = local_conn.load_collection(source_nc).execute()
                t_labels.append(tuple(tmp[tmp.openeo.temporal_dims[0]].values))
            t_steps = [len(x) for x in t_labels]
            if len(set(t_steps)) != 1:
                raise ValueError(
                    f"The provided netCDFs contain a different number of dates! {same_time_netcdfs}"
                )
            if len(set(t_labels)) != 1:
                raise ValueError(
                    "The provided netCDFs contain a different set of dates!"
                )

            so = dict(mode="rb", anon=True, default_fill_cache=False)
            same_time_kerchunks = dask.compute(
                *[
                    dask.delayed(gen_json)(var, so, kerchunk_folder)
                    for var in same_time_netcdfs
                ]
            )
            kerchunk_files_list.append(same_time_kerchunks)

        # List of List json Kerchunk.
        # First list: each element (list) different year/time
        # Second list: each element different variables
        datasets_list = []
        for same_time_data in kerchunk_files_list:
            for d in same_time_data:
                if d.endswith(".json"):
                    self.data = xr.open_dataset(
                        "reference://",
                        engine="zarr",
                        decode_coords="all",
                        backend_kwargs={
                            "storage_options": {
                                "fo": d,
                            },
                            "consolidated": False,
                        },
                        chunks={},
                    ).to_dataarray(dim="bands")
                    # IS_KERCHUNK = True # UNUSED VARIABLE IS_KERCHUNK
                    datasets_list.append(self.data)
                    # Need to create one Item per time/netCDF
        self.data = xr.combine_by_coords(
            datasets_list, combine_attrs="drop_conflicts"
        )
        # raise ValueError("'data' paramter must be either xr.DataArray, a str (path to a netCDF) or a list of lists with paths to JSON Kerchunk files.")

        self.X_DIM = self.data.openeo.x_dim
        self.Y_DIM = self.data.openeo.y_dim
        self.T_DIM = self.data.openeo.temporal_dims[0]
        self.B_DIM = self.data.openeo.band_dims[0]
        _log.debug(
            f"Extracted label dimensions from input are:\nx dimension:{self.X_DIM}\ny dimension:{self.Y_DIM}\nbands dimension:{self.B_DIM}\ntemporal dimension:{self.T_DIM}"
        )

        self.media_type = pystac.MediaType.JSON

        spatial_extents = []
        temporal_extents = []

        # Get the time dimension values
        # time_values = self.data[self.T_DIM].values # unused variable

        eo_info = {}

        # resetting CSV file
        open(f"{Path(self.output_folder)}/inline_items.csv", "w+")

        _log.debug("Cycling all timestamps")

        # Loop over the kerchunk files
        for same_time_data in kerchunk_files_list:
            _log.debug(f"\nts: {same_time_data}")

            time_ranges = []
            bands_data = {}
            for d in same_time_data:
                if d.endswith(".json"):
                    band_data = xr.open_dataset(
                        "reference://",
                        engine="zarr",
                        decode_coords="all",
                        backend_kwargs={
                            "storage_options": {
                                "fo": d,
                            },
                            "consolidated": False,
                        },
                        chunks={},
                    ).to_dataarray(dim="bands")
                    bands_data[d] = band_data
                    time_ranges.append(band_data[self.T_DIM].values)
            # for i,t_r in enumerate(time_ranges):
            #     if i==0:
            #         first_range = t_r
            #         _are_all_time_steps_equal = True
            #     else:
            #         _are_all_time_steps_equal = np.array_equal(first_range,t_r) and _are_all_time_steps_equal

            #             _log.debug(f"Are the time steps provided in the kerchunks aligned {_are_all_time_steps_equal}")

            #             if not _are_all_time_steps_equal:
            #                 raise Exception(f"The time steps provided in the kerchunk files {same_time_data} are not the same, can't continue.")

            # Now we can create one STAC Item for this time range, with one asset each band/variable

            start_datetime = np.min(time_ranges[0])
            end_datetime = np.max(time_ranges[0])

            # Convert the time value to a datetime object
            # Format the timestamp as a string to use in the file name
            start_datetime_str = pd.Timestamp(start_datetime).strftime(
                "%Y%m%d%H%M%S"
            )
            end_datetime_str = pd.Timestamp(end_datetime).strftime(
                "%Y%m%d%H%M%S"
            )

            _log.debug(
                f"Extracted temporal extrema for this time range: {start_datetime_str} {end_datetime_str}"
            )

            item_id = f"{f'{self.item_prefix}_' if self.item_prefix != '' else ''}{start_datetime_str}_{end_datetime_str}"

            # Create a unique directory for each time slice
            time_slice_dir = os.path.join(
                self.output_folder, f"{start_datetime_str}_{end_datetime_str}"
            )

            Path(time_slice_dir).mkdir(parents=True, exist_ok=True)

            # Get the band name (you may need to adjust this part based on your data)
            # bands = self.data[self.B_DIM].values

            pystac_assets = []

            # Cycling all bands/variables
            _log.debug("Cycling all bands")

            eo_bands_list = []
            for b_d in bands_data:
                band = bands_data[b_d][self.B_DIM].values[0]
                kerchunk_file = b_d
                _log.debug(f"b: {band}")

                link_path = kerchunk_file

                #                 if self.s3_upload:
                #                     #Uploading file to s3
                #                     _log.debug(f"Uploading {path} to {self.fix_path_slash(self.bucket_file_prefix)}{os.path.basename(path)}")
                #                     self.upload_s3(path)

                #                     link_path = f"https://{self.bucket_name}.{self.aws_region}.amazonaws.com/{self.fix_path_slash(self.bucket_file_prefix)}{curr_file_name}"

                bboxes = []

                # Create an asset dictionary for this time slice
                # Get BBOX and Footprint
                _log.debug(bands_data[b_d].rio.crs)
                _log.debug(bands_data[b_d].rio.bounds())

                dataset_geom = rioxarray_get_dataset_geom(
                    bands_data[b_d], densify_pts=0, precision=-1
                )
                bboxes.append(dataset_geom["bbox"])

                proj_info = {
                    f"proj:{name}": value
                    for name, value in rioxarray_get_projection_info(
                        bands_data[b_d]
                    ).items()
                }

                raster_info = {
                    "raster:bands": rioxarray_get_raster_info(
                        bands_data[b_d], max_size=1024
                    )
                }

                band_dict = {"name": band}

                eo_bands_list.append(band_dict)

                eo_info["eo:bands"] = [band_dict]

                pystac_assets.append(
                    (
                        band,
                        pystac.Asset(
                            href=link_path,
                            media_type=self.media_type,
                            extra_fields={
                                **proj_info,
                                **raster_info,
                                **eo_info,
                            },
                            roles=["data", "index"],
                        ),
                    )
                )

            eo_info["eo:bands"] = eo_bands_list

            minx, miny, maxx, maxy = zip(*bboxes)
            bbox = [min(minx), min(miny), max(maxx), max(maxy)]

            # item
            item = pystac.Item(
                id=item_id,
                geometry=bbox_to_geom(bbox),
                bbox=bbox,
                collection=None,  # self.collection_id, #FIXME: da errore se lo si decommenta
                stac_extensions=self.extensions,
                datetime=None,
                start_datetime=pd.Timestamp(start_datetime),
                end_datetime=pd.Timestamp(end_datetime),
                properties=self.properties,
            )

            # Calculate the item's spatial extent and add it to the list
            spatial_extents.append(item.bbox)

            # Calculate the item's temporal extent and add it to the list
            # item_datetime = item.start_datetime
            temporal_extents.append(
                [pd.Timestamp(start_datetime), pd.Timestamp(end_datetime)]
            )

            for key, asset in pystac_assets:
                item.add_asset(key=key, asset=asset)

            item.validate()

            item.add_link(
                pystac.Link(
                    pystac.RelType.COLLECTION,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item.add_link(
                pystac.Link(
                    pystac.RelType.PARENT,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item.add_link(
                pystac.Link(
                    pystac.RelType.SELF,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/{item_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item_dict = item.to_dict()

            # FIXME: persistent pystac bug or logical error (urllib error when adding root link to current item)
            # now this link is added manually by editing the dict
            item_dict["links"].append(
                {
                    "rel": "root",
                    "href": self.get_root_url(
                        f"{self.fix_path_slash(self.collection_url)}{self.collection_id}"
                    ),
                    "type": "application/json",
                }
            )

            # self.stac_collection.add_item(item)
            # Append the item to the list instead of adding it to the collection
            # item_dict = item.to_dict()
            item_dict["collection"] = self.collection_id

            item_oneline = json.dumps(
                item_dict, separators=(",", ":"), ensure_ascii=False
            )

            output_path = Path(self.output_folder)
            with open(f"{output_path}/inline_items.csv", "a+") as out_csv:
                out_csv.write(f"{item_oneline}\n")

            jsons_path = f"{output_path}/items/"
            Path(jsons_path).mkdir(parents=True, exist_ok=True)

            with open(
                f"{self.fix_path_slash(jsons_path)}{item_id}.json", "w+"
            ) as out_json:
                out_json.write(json.dumps(item_dict, indent=4))

        # Calculate overall spatial extent
        minx, miny, maxx, maxy = zip(*spatial_extents)
        overall_bbox = [min(minx), min(miny), max(maxx), max(maxy)]

        # Calculate overall temporal extent
        min_datetime = min(temporal_extents, key=lambda x: x[0])[0]
        max_datetime = max(temporal_extents, key=lambda x: x[1])[1]
        overall_temporal_extent = [min_datetime, max_datetime]

        s_ext = pystac.SpatialExtent([overall_bbox])
        t_ext = pystac.TemporalExtent([overall_temporal_extent])

        extra_fields = {}

        extra_fields["stac_version"] = self.stac_version

        if self.keywords is not None:
            extra_fields["keywords"] = self.keywords

        if self.providers is not None:
            extra_fields["providers"] = self.providers

        if self.version is not None:
            extra_fields["version"] = self.version

        if self.title is not None:
            extra_fields["title"] = self.title

        if self.sci_citation is not None:
            extra_fields["sci:citation"] = self.sci_citation

        if self.sci_doi is not None:
            extra_fields["sci:doi"] = self.sci_doi

        if self.sci_citation is not None or self.sci_doi is not None:
            self.extensions.append(
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
            )

        extra_fields["summaries"] = eo_info
        self.extensions.append(
            f"https://stac-extensions.github.io/datacube/{DATACUBE_EXT_VERSION}/schema.json"
        )
        extra_fields["stac_extensions"] = self.extensions

        cube_dimensions = {
            self.X_DIM: {
                "axis": "x",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.X_DIM].min()),
                    float(self.data.coords[self.X_DIM].max()),
                ],
                "reference_system": int(
                    (self.data.rio.crs.to_string()).split(":")[1]
                ),
            },
            self.Y_DIM: {
                "axis": "y",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.Y_DIM].min()),
                    float(self.data.coords[self.Y_DIM].max()),
                ],
                "reference_system": int(
                    (self.data.rio.crs.to_string()).split(":")[1]
                ),
            },
            self.T_DIM: {
                "type": "temporal",
                "extent": [
                    str(self.data[self.T_DIM].min().values),
                    str(self.data[self.T_DIM].max().values),
                ],
            },
            self.B_DIM: {
                "type": "bands",
                "values": list(self.data[self.B_DIM].values),
            },
        }

        extra_fields["cube:dimensions"] = cube_dimensions

        self.stac_collection = pystac.collection.Collection(
            id=self.collection_id,
            description=self.description,
            extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
            extra_fields=extra_fields,
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ITEMS,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items",
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.PARENT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.SELF,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        # self.stac_collection.remove_links(rel=pystac.RelType.ROOT)

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ROOT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        if self.license is not None:
            self.stac_collection.license = self.license

        # Create a single JSON file with all the items
        stac_collection_dict = self.stac_collection.to_dict()

        # in order to solve the double "root" link bug/issue
        links_dict = stac_collection_dict["links"]

        ctr_roots = 0
        self_exists = False
        self_idx = 0

        for idx, link in enumerate(links_dict):
            if link["rel"] == "root":
                ctr_roots = ctr_roots + 1
            if link["rel"] == "self":
                self_exists = True
                self_idx = idx

        if ctr_roots == 2 and self_exists:
            for idx, link in enumerate(links_dict):
                if (
                    link["rel"] == "root"
                    and link["href"] == links_dict[self_idx]["href"]
                    and link["type"] == links_dict[self_idx]["type"]
                ):
                    del links_dict[idx]
                    break

        if self.links is not None:
            stac_collection_dict["links"] = (
                stac_collection_dict["links"] + self.links
            )

        json_str = json.dumps(stac_collection_dict, indent=4)

        # printing metadata.json test output file
        output_path = Path(self.output_folder) / Path(self.output_file)
        with open(output_path, "w+") as metadata:
            metadata.write(json_str)

        if self.s3_upload:
            # Uploading metadata JSON file to s3
            _log.debug(
                f'Uploading metatada JSON "{output_path}" to {self.fix_path_slash(self.bucket_file_prefix)}{os.path.basename(output_path)}'
            )
            self.upload_s3(output_path)

        return

    def generate_netcdf_stac(self):

        # resetting CSV file
        open(f"{Path(self.output_folder)}/inline_items.csv", "w+")
        collection_assets = {}
        spatial_extents = []
        temporal_extents = []
        netcdf_list = copy(self.data)

        # Read the list of netCDFs
        for same_time_netcdfs in netcdf_list:
            t_labels = []
            to_combine = []
            to_combine_ds = []

            for source_nc in same_time_netcdfs:
                source_path = os.path.dirname(source_nc)
                tmp_ds = xr.open_dataset(
                    source_nc, decode_coords="all", chunks={}
                )
                tmp = tmp_ds.to_dataarray(dim="bands")
                to_combine.append(tmp)
                to_combine_ds.append(tmp_ds)
                t_labels.append(tuple(tmp[tmp.openeo.temporal_dims[0]].values))

            ## I should understand what happens here!
            t_steps = [len(x) for x in t_labels]
            if len(set(t_steps)) != 1:
                raise ValueError(
                    f"The provided netCDFs contain a different number of dates! {same_time_netcdfs}"
                )
            if len(set(t_labels)) != 1:
                raise ValueError(
                    "The provided netCDFs contain a different set of dates!"
                )

            self.data = xr.combine_by_coords(
                to_combine, combine_attrs="drop_conflicts"
            )
            self.data_ds = xr.combine_by_coords(
                to_combine_ds, combine_attrs="drop_conflicts"
            )
            self.X_DIM = self.data.openeo.x_dim
            self.Y_DIM = self.data.openeo.y_dim
            self.T_DIM = self.data.openeo.temporal_dims[0]
            self.B_DIM = self.data.openeo.band_dims[0]
            self.B_DIMS = self.data.openeo.band_dims
            self.OTHER_DIMS = self.data.openeo.other_dims

            _log.debug(
                f"Extracted label dimensions from input are:\nx dimension:{self.X_DIM}\ny dimension:{self.Y_DIM}\nbands dimension:{self.B_DIM}\ntemporal dimension:{self.T_DIM}\nother dimensions:{self.OTHER_DIMS}"
            )

            self.media_type = pystac.MediaType.NETCDF

            eo_info = {}
            time_ranges = []
            bands_data = {}

            _log.debug("Cycling all netcdfs")
            # Loop over the netcdf files
            for source_nc in same_time_netcdfs:
                source_path = os.path.dirname(source_nc)
                local_conn = LocalConnection(source_path)
                band_data = local_conn.load_collection(source_nc).execute()
                bands_data[source_nc] = band_data
                time_ranges.append(band_data[self.T_DIM].values)

                # Now we can create one STAC Item for this time range

                start_datetime = np.min(time_ranges)
                end_datetime = np.max(time_ranges)

                # Convert the time value to a datetime object
                # Format the timestamp as a string to use in the file name
                start_datetime_str = pd.Timestamp(start_datetime).strftime(
                    "%Y%m%d%H%M%S"
                )
                end_datetime_str = pd.Timestamp(end_datetime).strftime(
                    "%Y%m%d%H%M%S"
                )

                _log.debug(
                    f"Extracted temporal extrema for this time range: {start_datetime_str} {end_datetime_str}"
                )

                item_id = f"{f'{self.item_prefix}_' if self.item_prefix != '' else ''}{start_datetime_str}_{end_datetime_str}"

                # Create a unique directory for each time slice
                time_slice_dir = os.path.join(
                    self.output_folder,
                    f"{start_datetime_str}_{end_datetime_str}",
                )

                Path(time_slice_dir).mkdir(parents=True, exist_ok=True)

                # Get the band name (you may need to adjust this part based on your data)
                bands = self.data[self.B_DIM].values

                pystac_assets = []

                # Cycling all bands/variables
                _log.debug("Cycling all netcdfs")
                eo_bands_list = []
                for b_d in bands_data:
                    bands = bands_data[b_d][self.B_DIM].values
                    _log.debug(f"b: {bands}")
                    link_path = b_d

                    if self.s3_upload:

                        link_path = self._get_s3_link_path_netcdf(b_d)
                        self.upload_s3_for_nc(b_d)  # Use the new method

                    _log.debug(f"b: {link_path}")

                    bboxes = []

                    # Create an asset dictionary for this time slice
                    # Get BBOX and Footprint
                    _log.debug(bands_data[b_d].rio.crs)
                    _log.debug(bands_data[b_d].rio.bounds())

                    dataset_geom = rioxarray_get_dataset_geom(
                        bands_data[b_d], densify_pts=0, precision=-1
                    )
                    bboxes.append(dataset_geom["bbox"])

                    proj_info = {
                        f"proj:{name}": value
                        for name, value in rioxarray_get_projection_info(
                            bands_data[b_d]
                        ).items()
                    }

                    xarray_ext = {
                        "xarray:open_kwargs": {
                            "engine": "netcdf4",
                            "decode_coords": "all",
                            "chunks": {},
                        },
                        "xarray:storage_options": {
                            "client_kwargs": {"trust_env": True}
                        },
                    }

                    if self.s3_endpoint_url:
                        xarray_ext["xarray:storage_options"]["client_kwargs"][
                            "endpoint_url"
                        ] = self.s3_endpoint_url

                    asset_name = Path(b_d).stem
                    asset = pystac.Asset(
                        href=link_path,
                        media_type=self.media_type,
                        extra_fields={**proj_info, **xarray_ext},
                        roles=["data"],
                    )

                    pystac_assets.append(
                        (
                            asset_name,
                            asset,
                        )
                    )
                    if self.write_collection_assets:
                        collection_assets[f"{asset_name}"] = asset

                minx, miny, maxx, maxy = zip(*bboxes)
                bbox = [min(minx), min(miny), max(maxx), max(maxy)]

                cube_dimensions = {
                    self.X_DIM: {
                        "axis": "x",
                        "type": "spatial",
                        "extent": [
                            float(bands_data[b_d].coords[self.X_DIM].min()),
                            float(bands_data[b_d].coords[self.X_DIM].max()),
                        ],
                        "reference_system": int(
                            (bands_data[b_d].rio.crs.to_string()).split(":")[1]
                        ),
                    },
                    self.Y_DIM: {
                        "axis": "y",
                        "type": "spatial",
                        "extent": [
                            float(bands_data[b_d].coords[self.Y_DIM].min()),
                            float(bands_data[b_d].coords[self.Y_DIM].max()),
                        ],
                        "reference_system": int(
                            (self.data.rio.crs.to_string()).split(":")[1]
                        ),
                    },
                    self.T_DIM: {
                        "type": "temporal",
                        "extent": [
                            str(bands_data[b_d][self.T_DIM].min().values),
                            str(bands_data[b_d][self.T_DIM].max().values),
                        ],
                    },
                }

                for _o_dim in self.OTHER_DIMS:
                    values = [x for x in bands_data[b_d][_o_dim].values]
                    if isinstance(values[0], np.int64) or isinstance(
                        values[0], np.int32
                    ):
                        values = [int(x) for x in values]
                    else:
                        values = [str(x) for x in values]
                    cube_dimensions[_o_dim] = {
                        "type": "other",
                        "values": values,
                    }

                cube_variables = {}
                for _b_dim in self.B_DIMS:
                    for _b in bands_data[b_d][_b_dim].values:
                        cube_variables[_b] = {
                            "type": "data",
                            "dimensions": list(
                                bands_data[b_d].loc[{_b_dim: _b}].dims
                            ),
                        }
                        if "unit" in self.data_ds[_b].attrs:
                            cube_variables[_b]["unit"] = self.data_ds[
                                _b
                            ].attrs["unit"]
                extra_fields = {}
                extra_fields["cube:dimensions"] = cube_dimensions
                extra_fields["cube:variables"] = cube_variables

                # item
                item = pystac.Item(
                    id=item_id,
                    geometry=bbox_to_geom(bbox),
                    bbox=bbox,
                    collection=None,  # self.collection_id, #FIXME: da errore se lo si decommenta
                    stac_extensions=self.extensions,
                    datetime=None,
                    start_datetime=pd.Timestamp(start_datetime),
                    end_datetime=pd.Timestamp(end_datetime),
                    properties={**self.properties, **extra_fields},
                )

                # Calculate the item's spatial extent and add it to the list
                spatial_extents.append(item.bbox)

                # Calculate the item's temporal extent and add it to the list
                temporal_extents.append(
                    [pd.Timestamp(start_datetime), pd.Timestamp(end_datetime)]
                )

                for key, asset in pystac_assets:
                    item.add_asset(key=key, asset=asset)

                item.validate()

                item.add_link(
                    pystac.Link(
                        pystac.RelType.COLLECTION,
                        f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                        media_type=pystac.MediaType.JSON,
                    )
                )

                item.add_link(
                    pystac.Link(
                        pystac.RelType.PARENT,
                        f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                        media_type=pystac.MediaType.JSON,
                    )
                )

                item.add_link(
                    pystac.Link(
                        pystac.RelType.SELF,
                        f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/{item_id}",
                        media_type=pystac.MediaType.JSON,
                    )
                )

                item_dict = item.to_dict()

                # FIXME: persistent pystac bug or logical error (urllib error when adding root link to current item)
                # now this link is added manually by editing the dict
                item_dict["links"].append(
                    {
                        "rel": "root",
                        "href": self.get_root_url(
                            f"{self.fix_path_slash(self.collection_url)}{self.collection_id}"
                        ),
                        "type": "application/json",
                    }
                )

                item_dict["collection"] = self.collection_id

                item_oneline = json.dumps(
                    item_dict, separators=(",", ":"), ensure_ascii=False
                )

                output_path = Path(self.output_folder)
                with open(f"{output_path}/inline_items.csv", "a+") as out_csv:
                    out_csv.write(f"{item_oneline}\n")

                jsons_path = f"{output_path}/items/"
                Path(jsons_path).mkdir(parents=True, exist_ok=True)

                with open(
                    f"{self.fix_path_slash(jsons_path)}{item_id}.json", "w+"
                ) as out_json:
                    out_json.write(json.dumps(item_dict, indent=4))

        # Calculate overall spatial extent
        minx, miny, maxx, maxy = zip(*spatial_extents)
        overall_bbox = [min(minx), min(miny), max(maxx), max(maxy)]

        # Calculate overall temporal extent
        min_datetime = min(temporal_extents, key=lambda x: x[0])[0]
        max_datetime = max(temporal_extents, key=lambda x: x[1])[1]
        overall_temporal_extent = [min_datetime, max_datetime]

        s_ext = pystac.SpatialExtent([overall_bbox])
        t_ext = pystac.TemporalExtent([overall_temporal_extent])

        extra_fields = {}

        extra_fields["stac_version"] = self.stac_version

        if self.keywords is not None:
            extra_fields["keywords"] = self.keywords

        if self.providers is not None:
            extra_fields["providers"] = self.providers

        if self.version is not None:
            extra_fields["version"] = self.version

        if self.title is not None:
            extra_fields["title"] = self.title

        if self.sci_citation is not None:
            extra_fields["sci:citation"] = self.sci_citation

        if self.sci_doi is not None:
            extra_fields["sci:doi"] = self.sci_doi

        if self.sci_citation is not None or self.sci_doi is not None:
            self.extensions.append(
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
            )

        extra_fields["summaries"] = eo_info
        extra_fields["stac_extensions"] = self.extensions

        if self.write_collection_assets:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
                assets=collection_assets,
            )
        else:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
            )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ITEMS,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items",
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.PARENT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.SELF,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ROOT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        if self.license is not None:
            self.stac_collection.license = self.license

        # Create a single JSON file with all the items
        stac_collection_dict = self.stac_collection.to_dict()

        # in order to solve the double "root" link bug/issue
        links_dict = stac_collection_dict["links"]

        ctr_roots = 0
        self_exists = False
        self_idx = 0

        for idx, link in enumerate(links_dict):
            if link["rel"] == "root":
                ctr_roots = ctr_roots + 1
            if link["rel"] == "self":
                self_exists = True
                self_idx = idx

        if ctr_roots == 2 and self_exists:
            for idx, link in enumerate(links_dict):
                if (
                    link["rel"] == "root"
                    and link["href"] == links_dict[self_idx]["href"]
                    and link["type"] == links_dict[self_idx]["type"]
                ):
                    del links_dict[idx]
                    break

        if self.links is not None:
            stac_collection_dict["links"] = (
                stac_collection_dict["links"] + self.links
            )

        json_str = json.dumps(stac_collection_dict, indent=4)

        # printing metadata.json test output file
        output_path = Path(self.output_folder) / Path(self.output_file)
        with open(output_path, "w+") as metadata:
            metadata.write(json_str)

        # if self.s3_upload:
        #     # Uploading metadata JSON file to s3
        #     _log.debug(
        #         f'Uploading metatada JSON "{output_path}" to {self.fix_path_slash(self.bucket_file_prefix)}{os.path.basename(output_path)}'
        #     )
        #     self.upload_s3(output_path)

        return

    def generate_cog_stac(self):

        if isinstance(self.data, xr.Dataset):
            # store datasets in  a placeholder
            self.data_ds = self.data.copy(deep=True)
            self.data = self.data.to_dataarray(dim="bands")
        elif isinstance(self.data, xr.DataArray):
            pass
        elif isinstance(self.data, str):
            source_path = os.path.dirname(self.data)
            local_conn = LocalConnection(source_path)
            self.data = local_conn.load_collection(self.data).execute()
        else:
            raise Exception(
                "Please provide a path to a valid file or an xArray DataArray or Dataset object!"
            )

        self.media_type = pystac.MediaType.COG
        self.X_DIM = self.data.openeo.x_dim
        self.Y_DIM = self.data.openeo.y_dim
        self.T_DIM = self.data.openeo.temporal_dims[0]
        self.B_DIM = self.data.openeo.band_dims[0]
        _log.debug(
            f"Extracted label dimensions from input are:\nx dimension:{self.X_DIM}\ny dimension:{self.Y_DIM}\nbands dimension:{self.B_DIM}\ntemporal dimension:{self.T_DIM}"
        )

        if self.data_ds is None:
            self.data_ds = self.data.to_dataset(dim=self.B_DIM)

        spatial_extents = []
        temporal_extents = []

        collection_assets = {}
        # Get the time dimension values
        time_values = self.data[self.T_DIM].values

        eo_info = {}

        # resetting CSV file
        open(f"{Path(self.output_folder)}/inline_items.csv", "w+")

        _log.debug("Cycling all timestamps")

        # Cycling all timestamps
        for t in time_values:
            _log.debug(f"\nts: {t}")

            # Convert the time value to a datetime object
            timestamp = pd.Timestamp(t)

            # Format the timestamp as a string to use in the file name
            time_str = timestamp.strftime("%Y%m%d%H%M%S")

            item_id = f"{f'{self.item_prefix}_' if self.item_prefix != '' else ''}{time_str}"

            # Create a unique directory for each time slice
            time_slice_dir = os.path.join(self.output_folder, time_str)

            if not os.path.exists(time_slice_dir):
                os.makedirs(time_slice_dir)

            # Get the band name (you may need to adjust this part based on your data)
            bands = self.data[self.B_DIM].values

            pystac_assets = []

            # Cycling all bands
            _log.debug("Cycling all bands")

            eo_bands_list = []

            for band in bands:
                _log.debug(f"b: {band}")

                curr_file_name = f"{band}_{time_str}.tif"
                # Define the GeoTIFF file path for this time slice and band
                path = os.path.join(time_slice_dir, curr_file_name)

                # Write the result to the GeoTIFF file
                if isinstance(self.data, xr.DataArray):
                    self.data.loc[
                        {self.T_DIM: t, self.B_DIM: band}
                    ].to_dataset(name=band).rio.to_raster(
                        raster_path=path, driver="COG"
                    )
                else:
                    cog_file = self.data_ds.loc[{self.T_DIM: t}][band]
                    cog_file.attrs["long_name"] = f"{band}"
                    cog_file.to_dataset(name=band).rio.to_raster(
                        raster_path=path, driver="COG"
                    )

                link_path = path

                if self.s3_upload:
                    # Uploading file to s3
                    _log.debug(
                        f"Uploading {path} to {self.fix_path_slash(self.bucket_file_prefix)}{os.path.basename(path)}"
                    )
                    self.upload_s3(path)

                    link_path = f"https://{self.bucket_name}.{self.aws_region}.amazonaws.com/{self.fix_path_slash(self.bucket_file_prefix)}{curr_file_name}"

                bboxes = []

                # Create an asset dictionary for this time slice
                with rasterio.open(path) as src_dst:
                    # Get BBOX and Footprint
                    dataset_geom = get_dataset_geom(
                        src_dst, densify_pts=0, precision=-1
                    )
                    bboxes.append(dataset_geom["bbox"])

                    proj_info = rioxarray_get_projection_info(self.data)

                    raster_info = {
                        "raster:bands": get_raster_info(src_dst, max_size=1024)
                    }

                    band_dict = get_eobands_info(src_dst)[0]

                    # if type(band_dict) == dict:
                    if isinstance(band_dict, dict):
                        del band_dict["name"]
                        band_dict["name"] = band_dict["description"]
                        del band_dict["description"]
                    else:
                        pass  # band_dict = {}

                    eo_bands_list.append(
                        band_dict
                    )  # TODO: add to dict, rename description with name and remove name

                    cloudcover = src_dst.get_tag_item("CLOUDCOVER", "IMAGERY")
                    # TODO: try to add this field to the COG. Currently not present in the files we write here.
                    if cloudcover is not None:
                        self.properties.update(
                            {"eo:cloud_cover": int(cloudcover)}
                        )

                    eo_info["eo:bands"] = [band_dict]

                    asset = pystac.Asset(
                        href=link_path,
                        media_type=self.media_type,
                        extra_fields={**proj_info, **raster_info, **eo_info},
                        roles=["data"],
                    )
                    pystac_assets.append(
                        (
                            band,
                            asset,
                        )
                    )
                    if self.write_collection_assets:
                        collection_assets[f"{item_id}_{band}"] = asset

            eo_info["eo:bands"] = eo_bands_list

            minx, miny, maxx, maxy = zip(*bboxes)
            bbox = [min(minx), min(miny), max(maxx), max(maxy)]

            # item
            item = pystac.Item(
                id=item_id,
                geometry=bbox_to_geom(bbox),
                bbox=bbox,
                collection=None,
                stac_extensions=self.extensions,
                datetime=str_to_datetime(str(t)),
                properties=self.properties,
            )

            # Calculate the item's spatial extent and add it to the list
            item_bbox = item.bbox
            spatial_extents.append(item_bbox)

            # Calculate the item's temporal extent and add it to the list
            item_datetime = item.datetime
            temporal_extents.append([item_datetime, item_datetime])

            for key, asset in pystac_assets:
                item.add_asset(key=key, asset=asset)
            item.validate()

            item.add_link(
                pystac.Link(
                    pystac.RelType.COLLECTION,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item.add_link(
                pystac.Link(
                    pystac.RelType.PARENT,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item.add_link(
                pystac.Link(
                    pystac.RelType.SELF,
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items/{item_id}",
                    media_type=pystac.MediaType.JSON,
                )
            )

            item_dict = item.to_dict()

            # FIXME: persistent pystac bug or logical error (urllib error when adding root link to current item)
            # now this link is added manually by editing the dict
            item_dict["links"].append(
                {
                    "rel": "root",
                    "href": self.get_root_url(
                        f"{self.fix_path_slash(self.collection_url)}{self.collection_id}"
                    ),
                    "type": "application/json",
                }
            )

            # Append the item to the list instead of adding it to the collection
            item_dict["collection"] = self.collection_id

            item_oneline = json.dumps(
                item_dict, separators=(",", ":"), ensure_ascii=False
            )

            output_path = Path(self.output_folder)
            with open(f"{output_path}/inline_items.csv", "a+") as out_csv:
                out_csv.write(f"{item_oneline}\n")

            jsons_path = f"{output_path}/items/"
            Path(jsons_path).mkdir(parents=True, exist_ok=True)

            with open(
                f"{self.fix_path_slash(jsons_path)}{item_id}.json", "w+"
            ) as out_json:
                out_json.write(json.dumps(item_dict, indent=4))

        # Calculate overall spatial extent
        minx, miny, maxx, maxy = zip(*spatial_extents)
        overall_bbox = [min(minx), min(miny), max(maxx), max(maxy)]

        # Calculate overall temporal extent
        min_datetime = min(temporal_extents, key=lambda x: x[0])[0]
        max_datetime = max(temporal_extents, key=lambda x: x[1])[1]
        overall_temporal_extent = [min_datetime, max_datetime]

        s_ext = pystac.SpatialExtent([overall_bbox])
        t_ext = pystac.TemporalExtent([overall_temporal_extent])

        extra_fields = {}

        extra_fields["stac_version"] = self.stac_version

        if self.keywords is not None:
            extra_fields["keywords"] = self.keywords

        if self.providers is not None:
            extra_fields["providers"] = self.providers

        if self.version is not None:
            extra_fields["version"] = self.version

        if self.title is not None:
            extra_fields["title"] = self.title

        if self.sci_citation is not None:
            extra_fields["sci:citation"] = self.sci_citation

        if self.sci_doi is not None:
            extra_fields["sci:doi"] = self.sci_doi

        if self.sci_citation is not None or self.sci_doi is not None:
            self.extensions.append(
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
            )

        extra_fields["summaries"] = eo_info
        self.extensions.append(
            f"https://stac-extensions.github.io/datacube/{DATACUBE_EXT_VERSION}/schema.json"
        )
        extra_fields["stac_extensions"] = self.extensions

        cube_dimensions = {
            self.X_DIM: {
                "axis": "x",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.X_DIM].min()),
                    float(self.data.coords[self.X_DIM].max()),
                ],
                "reference_system": int(
                    self.data.rio.crs.to_string().split(":")[1]
                ),
            },
            self.Y_DIM: {
                "axis": "y",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.Y_DIM].min()),
                    float(self.data.coords[self.Y_DIM].max()),
                ],
                "reference_system": int(
                    self.data.rio.crs.to_string().split(":")[1]
                ),
            },
            self.T_DIM: {
                "type": "temporal",
                "extent": [
                    str(self.data[self.T_DIM].min().values),
                    str(self.data[self.T_DIM].max().values),
                ],
            },
            self.B_DIM: {
                "type": "bands",
                "values": list(self.data[self.B_DIM].values),
            },
        }

        extra_fields["cube:dimensions"] = cube_dimensions
        if self.write_collection_assets:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
                assets=collection_assets,
            )
        else:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
            )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ITEMS,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items",
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.PARENT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.SELF,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        # self.stac_collection.remove_links(rel=pystac.RelType.ROOT)

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ROOT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        if self.license is not None:
            self.stac_collection.license = self.license

        # Create a single JSON file with all the items
        stac_collection_dict = self.stac_collection.to_dict()

        # in order to solve the double "root" link bug/issue
        links_dict = stac_collection_dict["links"]

        ctr_roots = 0
        self_exists = False
        self_idx = 0

        for idx, link in enumerate(links_dict):
            if link["rel"] == "root":
                ctr_roots = ctr_roots + 1
            if link["rel"] == "self":
                self_exists = True
                self_idx = idx

        if ctr_roots == 2 and self_exists:
            for idx, link in enumerate(links_dict):
                if (
                    link["rel"] == "root"
                    and link["href"] == links_dict[self_idx]["href"]
                    and link["type"] == links_dict[self_idx]["type"]
                ):
                    del links_dict[idx]
                    break

        if self.links is not None:
            stac_collection_dict["links"] = (
                stac_collection_dict["links"] + self.links
            )

        json_str = json.dumps(stac_collection_dict, indent=4)

        # printing metadata.json test output file
        output_path = Path(self.output_folder) / Path(self.output_file)
        with open(output_path, "w+") as metadata:
            metadata.write(json_str)

        if self.s3_upload:
            # Uploading metadata JSON file to s3
            _log.debug(
                f'Uploading metatada JSON "{output_path}" to {self.fix_path_slash(self.bucket_file_prefix)}{os.path.basename(output_path)}'
            )
            self.upload_s3(output_path)

        return

    def generate_zarr_stac(self, item_id=None):
        """
        This method takes as input an xarray.Dataset object, which will be written to Zarr.
        It generates a STAC Collection with one Item and one Asset, taking inspiration from https://earthdatahub.destine.eu/api/stac/v1/collections/era5/items/reanalysis-era5-land
        Args:
            item_id: str
                Custom string assigned as Item id. If None, the id will be based on the dataset temporal range.
        """

        # Initialize outputs
        open(f"{Path(self.output_folder)}/inline_items.csv", "w+")
        collection_assets = {}
        temporal_extents = []
        link_path = None

        # Ensure data is loaded and CRS is valid
        self._ensure_crs()

        # Get Dimensions from property
        self.X_DIM = self.data.openeo.x_dim
        self.Y_DIM = self.data.openeo.y_dim
        self.T_DIM = self.data.openeo.temporal_dims[0]
        self.B_DIM = self.data.openeo.band_dims[0]
        self.B_DIMS = self.data.openeo.band_dims
        self.OTHER_DIMS = self.data.openeo.other_dims

        # Convert DataArray to Dataset if needed
        if isinstance(self.data, xr.DataArray):
            self.data_ds = self.data.to_dataset(dim=self.B_DIM)
        elif isinstance(self.data, xr.Dataset):
            self.data_ds = self.data.copy(deep=True)
            self.data = self.data.to_dataarray(dim=self.B_DIM)
        else:
            raise ValueError("Input must be convertible to xarray format")

        is_zarr_input = False
        if isinstance(self._input_source, (str, Path)):
            source_str = str(self._input_source)
            if source_str.endswith(".zarr"):
                is_zarr_input = True

        # Handle Zarr storage based on s3_upload flag
        if is_zarr_input:
            # For existing Zarr input
            if self.s3_upload:
                if isinstance(self._input_source, (str, Path)):
                    self._upload_zarr_directory(
                        str(self._input_source), item_id
                    )
                link_path = self._get_s3_link_path(item_id)
            else:
                # Only write local copy if _input_source does NOT start with https or s3
                if isinstance(self._input_source, (str, Path)):
                    source_str = str(self._input_source)
                    if not (
                        source_str.startswith("https://")
                        or source_str.startswith("s3://")
                    ):
                        self._copy_zarr_locally(
                            str(self._input_source), item_id
                        )
                    link_path = source_str  # Use the original path if remote
        else:
            # For non-Zarr input, convert to Zarr
            if self.s3_upload:
                s3 = self._get_s3fs_with_endpoint_support()
                store = s3fs.S3Map(
                    root=f"s3://{self.bucket_name}/{self.fix_path_slash(self.bucket_file_prefix)}{item_id}.zarr",
                    s3=s3,
                    check=False,
                )
                self.data_ds.chunk("auto").to_zarr(
                    store, compute=True, mode="w"
                )
                link_path = self._get_s3_link_path(item_id)
            else:
                # Always write local copy when s3_upload is False
                local_zarr_path = os.path.join(
                    self.output_folder, f"{item_id}.zarr"
                )
                self.data_ds.to_zarr(local_zarr_path, compute=True, mode="w")
                link_path = local_zarr_path

        _log.debug(
            f"Extracted label dimensions from input are:\nx dimension:{self.X_DIM}\ny dimension:{self.Y_DIM}\nbands dimension:{self.B_DIM}\ntemporal dimension:{self.T_DIM}\nother dimensions:{self.OTHER_DIMS}"
        )

        self.media_type = pystac.MediaType.ZARR

        time_ranges = []
        time_ranges.append(self.data[self.T_DIM].values)

        # Now we can create one STAC Item for this time range
        start_datetime = np.min(time_ranges)
        end_datetime = np.max(time_ranges)

        # Convert the time value to a datetime object
        # Format the timestamp as a string to use in the file name
        start_datetime_str = pd.Timestamp(start_datetime).strftime(
            "%Y%m%d%H%M%S"
        )
        end_datetime_str = pd.Timestamp(end_datetime).strftime("%Y%m%d%H%M%S")

        _log.debug(
            f"Extracted temporal extrema for this time range: {start_datetime_str} {end_datetime_str}"
        )
        if item_id is None:
            item_id = f"{f'{self.item_prefix}_' if self.item_prefix != '' else ''}{start_datetime_str}_{end_datetime_str}"

        # Create a unique directory for each Item
        item_dir = os.path.join(self.output_folder, item_id)
        _log.debug(f"item_dir: {item_dir}")
        _log.debug(f"item_id: {item_id}")
        Path(item_dir).mkdir(parents=True, exist_ok=True)

        # Get the band name
        bands = self.data[self.B_DIM].values
        _log.debug(f"Variable names for this dataset are: {bands}")

        pystac_assets = []

        _log.debug(f"b: {link_path}")

        bboxes = []

        # Create an asset dictionary for this time slice
        # Get BBOX and Footprint
        _log.debug(self.data.rio.crs)
        _log.debug(self.data.rio.bounds())

        dataset_geom = rioxarray_get_dataset_geom(
            self.data, densify_pts=0, precision=-1
        )
        bboxes.append(dataset_geom["bbox"])

        proj_info = rioxarray_get_projection_info(self.data)

        # custom_endpoint_url - this area is the culprit!
        xarray_ext = {
            "xarray:open_kwargs": {"chunks": {}, "engine": "zarr"},
            "xarray:storage_options": {"client_kwargs": {"trust_env": True}},
        }

        if self.s3_endpoint_url is not None:
            xarray_ext["xarray:storage_options"]["client_kwargs"][
                "endpoint_url"
            ] = self.s3_endpoint_url

        asset = pystac.Asset(
            href=link_path,
            media_type=self.media_type,
            extra_fields={**proj_info, **xarray_ext},
            roles=["data"],
        )
        asset_name = "data"
        pystac_assets.append(
            (
                asset_name,
                asset,
            )
        )
        if self.write_collection_assets:
            collection_assets[f"{asset_name}"] = asset

        # eo_info["eo:bands"] = eo_bands_list

        minx, miny, maxx, maxy = zip(*bboxes)
        bbox = [min(minx), min(miny), max(maxx), max(maxy)]

        cube_dimensions = {
            self.X_DIM: {
                "axis": "x",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.X_DIM].min()),
                    float(self.data.coords[self.X_DIM].max()),
                ],
                "reference_system": int(
                    (self.data.rio.crs.to_string()).split(":")[1]
                ),
            },
            self.Y_DIM: {
                "axis": "y",
                "type": "spatial",
                "extent": [
                    float(self.data.coords[self.Y_DIM].min()),
                    float(self.data.coords[self.Y_DIM].max()),
                ],
                "reference_system": int(
                    (self.data.rio.crs.to_string()).split(":")[1]
                ),
            },
            self.T_DIM: {
                "type": "temporal",
                "extent": [
                    str(self.data[self.T_DIM].min().values),
                    str(self.data[self.T_DIM].max().values),
                ],
            },
        }

        for _o_dim in self.OTHER_DIMS:
            values = [x for x in self.data[_o_dim].values]
            if isinstance(values[0], np.int64) or isinstance(
                values[0], np.int32
            ):
                values = [int(x) for x in values]
            else:
                values = [str(x) for x in values]
            cube_dimensions[_o_dim] = {
                "type": "other",
                "values": values,
            }

        cube_variables = {}
        for _b_dim in self.B_DIMS:
            for _b in self.data[_b_dim].values:
                cube_variables[_b] = {
                    "type": "data",
                    "dimensions": list(self.data_ds[_b].dims),
                }
                if "unit" in self.data_ds[_b].attrs:
                    cube_variables[_b]["unit"] = self.data_ds[_b].attrs["unit"]
        extra_fields = {}
        extra_fields["cube:dimensions"] = cube_dimensions
        extra_fields["cube:variables"] = cube_variables
        _log.debug(extra_fields)
        # item

        # Add xarray extension
        self.extensions.remove(
            f"https://stac-extensions.github.io/raster/{RASTER_EXT_VERSION}/schema.json"
        )
        self.extensions.remove(
            f"https://stac-extensions.github.io/eo/{EO_EXT_VERSION}/schema.json"
        )
        item_extensions = deepcopy(self.extensions)
        item_extensions.append(
            "https://stac-extensions.github.io/xarray-assets/v1.0.0/schema.json"
        )
        item_extensions.append(
            f"https://stac-extensions.github.io/datacube/{DATACUBE_EXT_VERSION}/schema.json"
        )
        item = pystac.Item(
            id=item_id,
            geometry=bbox_to_geom(bbox),
            bbox=bbox,
            collection=None,  # self.collection_id, #FIXME: da errore se lo si decommenta
            stac_extensions=item_extensions,
            datetime=pd.Timestamp(
                start_datetime
            ),  # TODO: Check with latest stac-fastapi if this is necessary
            start_datetime=pd.Timestamp(start_datetime),
            end_datetime=pd.Timestamp(end_datetime),
            properties={**self.properties, **extra_fields},
        )

        # Calculate the item's temporal extent and add it to the list
        # item_datetime = item.start_datetime
        temporal_extents.append(
            [pd.Timestamp(start_datetime), pd.Timestamp(end_datetime)]
        )

        for key, asset in pystac_assets:
            item.add_asset(key=key, asset=asset)
        _log.debug(item.to_dict())
        item.validate()

        item.add_link(
            pystac.Link(
                pystac.RelType.COLLECTION,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        item.add_link(
            pystac.Link(
                pystac.RelType.PARENT,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        item.add_link(
            pystac.Link(
                pystac.RelType.SELF,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/{item_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        item_dict = item.to_dict()

        # FIXME: persistent pystac bug or logical error (urllib error when adding root link to current item)
        # now this link is added manually by editing the dict
        item_dict["links"].append(
            {
                "rel": "root",
                "href": self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}"
                ),
                "type": "application/json",
            }
        )

        # Append the item to the list instead of adding it to the collection
        item_dict["collection"] = self.collection_id

        item_oneline = json.dumps(
            item_dict, separators=(",", ":"), ensure_ascii=False
        )

        output_path = Path(self.output_folder)
        with open(f"{output_path}/inline_items.csv", "a+") as out_csv:
            out_csv.write(f"{item_oneline}\n")

        jsons_path = f"{output_path}/items/"
        Path(jsons_path).mkdir(parents=True, exist_ok=True)

        with open(
            f"{self.fix_path_slash(jsons_path)}{item_id}.json", "w+"
        ) as out_json:
            out_json.write(json.dumps(item_dict, indent=4))

        s_ext = pystac.SpatialExtent([bbox])
        t_ext = pystac.TemporalExtent(
            [[pd.Timestamp(start_datetime), pd.Timestamp(end_datetime)]]
        )

        extra_fields = {}

        extra_fields["stac_version"] = self.stac_version

        if self.keywords is not None:
            extra_fields["keywords"] = self.keywords

        if self.providers is not None:
            extra_fields["providers"] = self.providers

        if self.version is not None:
            extra_fields["version"] = self.version

        if self.title is not None:
            extra_fields["title"] = self.title

        if self.sci_citation is not None:
            extra_fields["sci:citation"] = self.sci_citation

        if self.sci_doi is not None:
            extra_fields["sci:doi"] = self.sci_doi

        if self.sci_citation is not None or self.sci_doi is not None:
            self.extensions.append(
                "https://stac-extensions.github.io/scientific/v1.0.0/schema.json"
            )

        # extra_fields["summaries"] = eo_info
        extra_fields["stac_extensions"] = self.extensions

        if self.write_collection_assets:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
                assets=collection_assets,
            )
        else:
            self.stac_collection = pystac.collection.Collection(
                id=self.collection_id,
                description=self.description,
                extent=pystac.Extent(spatial=s_ext, temporal=t_ext),
                extra_fields=extra_fields,
            )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ITEMS,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items",
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.PARENT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.SELF,
                f"{self.fix_path_slash(self.collection_url)}{self.collection_id}",
                media_type=pystac.MediaType.JSON,
            )
        )

        # self.stac_collection.remove_links(rel=pystac.RelType.ROOT)

        self.stac_collection.add_link(
            pystac.Link(
                pystac.RelType.ROOT,
                self.get_root_url(
                    f"{self.fix_path_slash(self.collection_url)}{self.collection_id}/items"
                ),
                media_type=pystac.MediaType.JSON,
            )
        )

        if self.license is not None:
            self.stac_collection.license = self.license

        # Create a single JSON file
        stac_collection_dict = self.stac_collection.to_dict()

        # in order to solve the double "root" link bug/issue
        links_dict = stac_collection_dict["links"]

        ctr_roots = 0
        self_exists = False
        self_idx = 0

        for idx, link in enumerate(links_dict):
            if link["rel"] == "root":
                ctr_roots = ctr_roots + 1
            if link["rel"] == "self":
                self_exists = True
                self_idx = idx

        if ctr_roots == 2 and self_exists:
            for idx, link in enumerate(links_dict):
                if (
                    link["rel"] == "root"
                    and link["href"] == links_dict[self_idx]["href"]
                    and link["type"] == links_dict[self_idx]["type"]
                ):
                    del links_dict[idx]
                    break

        if self.links is not None:
            stac_collection_dict["links"] = (
                stac_collection_dict["links"] + self.links
            )

        json_str = json.dumps(stac_collection_dict, indent=4)

        # Writing STAC json to file
        output_path = Path(self.output_folder) / Path(self.output_file)
        with open(output_path, "w+") as metadata:
            metadata.write(json_str)

        return
