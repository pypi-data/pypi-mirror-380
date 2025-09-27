import os
from urllib.parse import urljoin, urlencode
from typing import Optional, Dict, List, Optional, Union, TYPE_CHECKING
import mimetypes
import requests
import sys

from geobox.field import Field

from .base import Base
from .utils import clean_data, join_url_params
from .task import Task
from .vectorlayer import VectorLayer
from .view import VectorLayerView
from .enums import PolygonizeConnectivity, AnalysisResampleMethod, SlopeUnit, AnalysisAlgorithm, AnalysisDataType, RangeBound, DistanceUnit

if TYPE_CHECKING:
    from . import GeoboxClient 
    from .user import User
    from .aio import AsyncGeoboxClient
    from .aio.raster import Raster as AsyncRaster

class Raster(Base):

    BASE_ENDPOINT: str = 'rasters/'

    def __init__(self,
                 api: 'GeoboxClient',
                 uuid: str,
                 data: Optional[Dict] = {}):
        """
        Constructs all the necessary attributes for the Raster object.

        Args:
            api (GeoboxClient): The API instance.
            uuid (str): The UUID of the raster.
            data (Dict, optional): The raster data.
        """ 
        super().__init__(api, uuid=uuid, data=data)


    @classmethod
    def get_rasters(cls, api: 'GeoboxClient', **kwargs) -> Union[List['Raster'], int]:
        """
        Get all rasters.

        Args:
            api (GeoboxClient): The API instance.

        Keyword Args:
            terrain (bool): whether to get terrain rasters.
            q (str): query filter based on OGC CQL standard. e.g. "field1 LIKE '%GIS%' AND created_at > '2021-01-01'"
            search (str): search term for keyword-based searching among search_fields or all textual fields if search_fields does not have value. NOTE: if q param is defined this param will be ignored.        
            search_fields (str): comma separated list of fields for searching
            order_by (str): comma separated list of fields for sorting results [field1 A|D, field2 A|D, …]. e.g. name A, type D. NOTE: "A" denotes ascending order and "D" denotes descending order.
            return_count (bool): whether to return the total count of rasters. default is False.
            skip (int): number of rasters to skip. minimum is 0.
            limit (int): number of rasters to return. minimum is 1.
            user_id (int): user id to show the rasters of the user. privileges required.
            shared (bool): whether to return shared rasters. default is False.

        Returns:
            List[Raster] | int: A list of Raster objects or the total count of rasters.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> rasters = Raster.get_rasters(client, terrain=True, q="name LIKE '%GIS%'")
            or
            >>> rasters = client.get_rasters(terrain=True, q="name LIKE '%GIS%'")
        """
        params = {
            'terrain': kwargs.get('terrain', None),
            'f': 'json',
            'q': kwargs.get('q', None),
            'search': kwargs.get('search', None),
            'search_fields': kwargs.get('search_fields', None),
            'order_by': kwargs.get('order_by', None),
            'return_count': kwargs.get('return_count', False),
            'skip': kwargs.get('skip', 0),
            'limit': kwargs.get('limit', 100),
            'user_id': kwargs.get('user_id', None),
            'shared': kwargs.get('shared', False)
        }
        return super()._get_list(api, cls.BASE_ENDPOINT, params, factory_func=lambda api, item: Raster(api, item['uuid'], item))
    


    @classmethod
    def get_rasters_by_ids(cls, api: 'GeoboxClient', ids: List[str], user_id: int = None) -> List['Raster']:
        """
        Get rasters by their IDs.

        Args:
            api (GeoboxClient): The API instance.
            ids (List[str]): The IDs of the rasters.
            user_id (int, optional): specific user. privileges required.

        Returns:
            List['Raster']: A list of Raster objects.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> rasters = Raster.get_rasters_by_ids(client, ids=['123', '456'])
            or
            >>> rasters = client.get_rasters_by_ids(ids=['123', '456'])
        """ 
        params = {
            'ids': ids,
            'user_id': user_id,
        }
        endpoint = urljoin(cls.BASE_ENDPOINT, 'get-rasters/')

        return super()._get_list_by_ids(api, endpoint, params, factory_func=lambda api, item: Raster(api, item['uuid'], item))


    @classmethod
    def get_raster(cls, api: 'GeoboxClient', uuid: str, user_id: int = None) -> 'Raster':
        """
        Get a raster by its UUID.

        Args:
            api (GeoboxClient): The API instance.
            uuid (str): The UUID of the raster.
            user_id (int, optional): specific user. privileges required.

        Returns:
            Raster: A Raster object.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            or
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
        """
        params = {
            'f': 'json',
            'user_id': user_id
        }
        return super()._get_detail(api, cls.BASE_ENDPOINT, uuid, params, factory_func=lambda api, item: Raster(api, item['uuid'], item))


    @classmethod
    def get_raster_by_name(cls, api: 'GeoboxClient', name: str, user_id: int = None) -> Union['Raster', None]:
        """
        Get a raster by name

        Args:
            api (GeoboxClient): The GeoboxClient instance for making requests.
            name (str): the name of the raster to get
            user_id (int, optional): specific user. privileges required.

        Returns:
            Raster | None: returns the raster if a raster matches the given name, else None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster_by_name(client, name='test')
            or
            >>> raster = client.get_raster_by_name(name='test')
        """
        rasters = cls.get_rasters(api, q=f"name = '{name}'", user_id=user_id)
        if rasters and rasters[0].name == name:
            return rasters[0]
        else:
            return None
    
    
    def update(self, **kwargs) -> None:
        """
        Update the raster.

        Keyword Args:
            name (str): The name of the raster.
            display_name (str): The display name of the raster.
            description (str): The description of the raster.

        Returns:
            None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.update(name="new_name")
        """ 
        params = {
            'name': kwargs.get('name'),
            'display_name': kwargs.get('display_name'),
            'description': kwargs.get('description')
        }
        return super()._update(self.endpoint, params)
    

    def delete(self) -> None:
        """
        Delete the raster.

        Returns:
            None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.delete()
        """
        super().delete(self.endpoint)
    

    @property
    def thumbnail(self) -> str:
        """
        Get the thumbnail of the raster.

        Returns:
            str: The url of the thumbnail.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.thumbnail
        """
        return super().thumbnail(format='')
    
    
    @property
    def info(self) -> Dict:
        """
        Get the info of the raster.

        Returns:
            Dict: The info of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.info
        """
        endpoint = urljoin(self.endpoint, 'info/')
        return self.api.get(endpoint)
    

    def get_statistics(self, indexes: str = None) -> Dict:
        """
        Get the statistics of the raster.

        Args:
            indexes (str): list of comma separated band indexes. e.g. 1, 2, 3

        Returns:
            Dict: The statistics of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_statistics(indexes='1, 2, 3')
        """
        params = clean_data({
            'indexes': indexes,
        })
        query_string = urlencode(params)
        endpoint = urljoin(self.endpoint, f'statistics/?{query_string}')
        return self.api.get(endpoint)
    

    def get_point(self, lat: float, lng: float) -> Dict:
        """
        Get the point of the raster.

        Args:
            lat (float): The latitude of the point. minimum is -90, maximum is 90.
            lng (float): The longitude of the point. minimum is -180, maximum is 180.

        Returns:
            Dict: The point of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_point(lat=60, lng=50)
        """
        if lat < -90 or lat > 90:
            raise ValueError("lat must be between -90 and 90")
        if lng < -180 or lng > 180:
            raise ValueError("lng must be between -180 and 180")
        
        params = clean_data({
            'lat': lat,
            'lng': lng,
        })
        query_string = urlencode(params)
        endpoint = urljoin(self.endpoint, f'point?{query_string}')
        return self.api.get(endpoint)
    

    def _get_save_path(self, save_path: str = None) -> str:
        """
        Get the path where the file should be saved.

        Args:
            save_path (str, optional): The path to save the file.

        Returns:
            str: The path where the file is saved.
        
        Raises:
            ValueError: If save_path does not end with a '/'.
        """
        # If save_path is provided, check if it ends with a '/'
        if save_path and save_path.endswith('/'):
            return f'{save_path}'
        
        if save_path and not save_path.endswith('/'):
            raise ValueError("save_path must end with a '/'")
        
        return os.getcwd()
    
    
    def _get_file_name(self, response: requests.Response) -> str:
        """
        Get the file name from the response.

        Args:
            response (requests.Response): The response of the request.

        Returns:
            str: The file name 
        """
        if 'Content-Disposition' in response.headers and 'filename=' in response.headers['Content-Disposition']:
            file_name = response.headers['Content-Disposition'].split('filename=')[-1].strip().strip('"')

        else:
            content_type = response.headers.get("Content-Type", "")
            file_name = f'{self.name}.{mimetypes.guess_extension(content_type.split(";")[0])}'

        return file_name


    def _create_progress_bar(self) -> 'tqdm':
        """Creates a progress bar for the task."""
        try:
            from tqdm.auto import tqdm
        except ImportError:
            from .api import logger
            logger.warning("[tqdm] extra is required to show the progress bar. install with: pip insatll geobox[tqdm]")
            return None

        return tqdm(unit="B", 
                        total=int(self.size), 
                        file=sys.stdout,
                        dynamic_ncols=True,
                        desc="Downloading",
                        unit_scale=True,
                        unit_divisor=1024, 
                        ascii=True
                )


    def download(self, save_path: str = None, progress_bar: bool = True) -> str:
        """
        Download the raster.

        Args:
            save_path (str, optional): Path where the file should be saved. 
                                    If not provided, it saves to the current working directory
                                    using the original filename and appropriate extension.
            progress_bar (bool, optional): Whether to show a progress bar. default: True
        
        Returns:
            str: The path to save the raster.

        Raises:
            ValueError: If file_uuid is not set
            OSError: If there are issues with file operations        

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.download(save_path="path/to/save/")
        """
        if not self.uuid:
            raise ValueError("Raster UUID is required to download the raster file")
        
        save_path = self._get_save_path(save_path)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with self.api.get(f"{self.endpoint}download/", stream=True) as response:
            file_name = self._get_file_name(response)
            full_path = f"{save_path}/{file_name}"
            with open(full_path, 'wb') as f:
                pbar = self._create_progress_bar() if progress_bar else None
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    if pbar:
                        pbar.update(len(chunk))
                        pbar.refresh()
                if pbar:
                    pbar.close()

        return os.path.abspath(full_path)


    def get_content_file(self, save_path: str = None, progress_bar: bool = True) -> str: 
        """
        Get Raster Content URL

        Args:
            save_path (str, optional): Path where the file should be saved. 
                                    If not provided, it saves to the current working directory
                                    using the original filename and appropriate extension.
            progress_bar (bool, optional): Whether to show a progress bar. default: True
        
        Returns:
            str: The path to save the raster.

        Raises:
            ValueError: If uuid is not set
            OSError: If there are issues with file operations   

        Examples:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster_tiff = raste.get_content_file()
        """
        if not self.uuid:
            raise ValueError("Raster UUID is required to download the raster content")
        
        save_path = self._get_save_path(save_path)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        with self.api.get(f"{self.endpoint}content/", stream=True) as response:
            file_name = self._get_file_name(response)
            full_path = f"{save_path}/{file_name}"
            with open(full_path, 'wb') as f:
                pbar = self._create_progress_bar() if progress_bar else None
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    if pbar:
                        pbar.update(len(chunk))
                        pbar.refresh()
                if pbar:
                    pbar.close()

        return os.path.abspath(full_path)


    def get_render_png_url(self, x: int, y: int, z: int, **kwargs) -> str:
        """
        Get the PNG URL of the raster.

        Args:
            x (int): The x coordinate of the tile.
            y (int): The y coordinate of the tile.
            z (int): The zoom level of the tile.

        Keyword Args:
            indexes (str, optional): list of comma separated band indexes to be rendered. e.g. 1, 2, 3
            nodata (int, optional)
            expression (str, optional): band math expression. e.g. b1*b2+b3
            rescale (List, optional): comma (',') separated Min,Max range. Can set multiple time for multiple bands.
            color_formula (str, optional): Color formula. e.g. gamma R 0.5
            colormap_name (str, optional)
            colormap (str, optional): JSON encoded custom Colormap. e.g. {"0": "#ff0000", "1": "#00ff00"} or [[[0, 100], "#ff0000"], [[100, 200], "#00ff00"]]

        Returns:
            str: The PNG Render URL of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_tile_render_url(x=10, y=20, z=1)
        """
        params = clean_data({
            'indexes': kwargs.get('indexes'),
            'nodata': kwargs.get('nodata'),
            'expression': kwargs.get('expression'),
            'rescale': kwargs.get('rescale'),
            'color_formula': kwargs.get('color_formula'),
            'colormap_name': kwargs.get('colormap_name'),
            'colormap': kwargs.get('colormap')
        })
        query_string = urlencode(params)
        endpoint = f'{self.api.base_url}{self.endpoint}render/{z}/{x}/{y}.png'
        if query_string:
            endpoint = f'{endpoint}?{query_string}'

        if not self.api.access_token and self.api.apikey:
            endpoint = join_url_params(endpoint, {"apikey": self.api.apikey})
            
        return endpoint
    

    def get_tile_pbf_url(self, x: int = '{x}', y: int = '{y}', z: int = '{z}', indexes: str = None) -> str:
        """
        Get the URL of the tile.

        Args:
            x (int, optional): The x coordinate of the tile.
            y (int, optional): The y coordinate of the tile.
            z (int, optional): The zoom level of the tile.
            indexes (str, optional): list of comma separated band indexes to be rendered. e.g. 1, 2, 3

        Returns:
            str: The URL of the tile.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_tile_pbf_url(x=10, y=20, z=1)
        """
        params = clean_data({
            'indexes': indexes
        })
        query_string = urlencode(params)
        endpoint = urljoin(self.api.base_url, f'{self.endpoint}tiles/{z}/{x}/{y}.pbf')
        endpoint = urljoin(endpoint, f'?{query_string}')

        if not self.api.access_token and self.api.apikey:
            endpoint = join_url_params(endpoint, {"apikey": self.api.apikey})

        return endpoint
    

    def get_tile_png_url(self, x: int = 'x', y: int = 'y', z: int = 'z') -> str:
        """
        Get the URL of the tile.

        Args:
            x (int, optional): The x coordinate of the tile.
            y (int, optional): The y coordinate of the tile.
            z (int, optional): The zoom level of the tile.

        Returns:
            str: The URL of the tile.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_tile_png_url(x=10, y=20, z=1)
        """
        endpoint = f'{self.api.base_url}{self.endpoint}tiles/{z}/{x}/{y}.png'
            
        if not self.api.access_token and self.api.apikey:
            endpoint = f'{endpoint}?apikey={self.api.apikey}'

        return endpoint


    def get_tile_json(self) -> Dict:
        """
        Get the tile JSON of the raster.

        Returns:
            Dict: The tile JSON of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_tile_json()
        """
        endpoint = urljoin(self.endpoint, 'tilejson.json')
        return self.api.get(endpoint)


    def wmts(self, scale: int = None) -> str:
        """
        Get the WMTS URL

        Args:
            scale (int, optional): The scale of the raster. values are: 1, 2

        Returns:
            str: the raster WMTS URL

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.wmts(scale=1)
        """ 
        endpoint = urljoin(self.api.base_url, f'{self.endpoint}wmts/')
        if scale:
            endpoint = f"{endpoint}?scale={scale}"

        if not self.api.access_token and self.api.apikey:
            endpoint = join_url_params(endpoint, {"apikey": self.api.apikey})

        return endpoint


    @property
    def settings(self) -> Dict:
        """
        Get the settings of the raster.

        Returns:
            Dict: The settings of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.settings
        """
        return super()._get_settings(self.endpoint)
    

    def update_settings(self, settings: Dict) -> Dict:
        """
        Update the settings

        settings (Dict): settings dictionary

        Returns:
            Dict: updated settings

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster1 = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster2 = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster1.update_settings(raster2.settings)
        """
        return super()._set_settings(self.endpoint, settings)  


    def set_settings(self, **kwargs) -> None:
        """
        Set the settings of the raster.

        Keyword Args:
            nodata (int): The nodata value of the raster.
            indexes (list[int]): The indexes of the raster.
            rescale (list[int]): The rescale of the raster.
            colormap_name (str): The colormap name of the raster.
            color_formula (str): The color formula of the raster.
            expression (str): The expression of the raster.
            exaggeraion (int): The exaggeraion of the raster.
            min_zoom (int): The min zoom of the raster.
            max_zoom (int): The max zoom of the raster.
            use_cache (bool): Whether to use cache of the raster.
            cache_until_zoom (int): The cache until zoom of the raster.


        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.set_settings(nodata=0, 
            ...                         indexes=[1], 
            ...                         rescale=[[0, 10000]], 
            ...                         colormap_name='gist_rainbow', 
            ...                         color_formula='Gamma R 0.5', 
            ...                         expression='b1 * 2', 
            ...                         exaggeraion=10, 
            ...                         min_zoom=0, 
            ...                         max_zoom=22, 
            ...                         use_cache=True, 
            ...                         cache_until_zoom=17)
        """
        visual_settings = {
            'nodata', 'indexes', 'rescale', 'colormap_name', 
            'color_formula', 'expression', 'exaggeraion'
        }
        tile_settings = {
            'min_zoom', 'max_zoom', 'use_cache', 'cache_until_zoom'
        }

        settings = self.settings

        for key, value in kwargs.items():
            if key in visual_settings:
                settings['visual_settings'][key] = value
            elif key in tile_settings:
                settings['tile_settings'][key] = value


        return super()._set_settings(self.endpoint, settings)


    def share(self, users: List['User']) -> None:
        """
        Shares the raster with specified users.

        Args:
            users (List[User]): The list of user objects to share the raster with.

        Returns:
            None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> users = client.search_users(search="John")
            >>> raster.share(users=users)
        """
        super()._share(self.endpoint, users)
    

    def unshare(self, users: List['User']) -> None:
        """
        Unshares the raster with specified users.

        Args:
            users (List[User]): The list of user objects to unshare the raster with.

        Returns:
            None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> users = client.search_users(search="John")
            >>> raster.unshare(users=users)
        """
        super()._unshare(self.endpoint, users)


    def get_shared_users(self, search: str = None, skip: int = 0, limit: int = 10) -> List['User']:
        """
        Retrieves the list of users the raster is shared with.

        Args:
            search (str, optional): The search query.
            skip (int, optional): The number of users to skip.
            limit (int, optional): The maximum number of users to retrieve.

        Returns:
            List[User]: The list of shared users.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.get_shared_users(search='John', skip=0, limit=10)
        """
        params = {
            'search': search,
            'skip': skip,
            'limit': limit
        }
        return super()._get_shared_users(self.endpoint, params)


    def seed_cache(self, from_zoom: int = None, to_zoom: int = None, extent: List[int] = None, workers: int = 1) -> List['Task']:
        """
        Seed the cache of the raster.

        Args:
            from_zoom (int, optional): The from zoom of the raster.
            to_zoom (int, optional): The to zoom of the raster.
            extent (List[int], optional): The extent of the raster.
            workers (int, optional): The number of workers to use. default is 1.

        Returns:
            Task: The task of the seed cache.

        Example:
            >>> from geobox import GeoboxClient 
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> task = raster.seed_cache(from_zoom=0, to_zoom=22, extent=[0, 0, 100, 100], workers=1)
        """
        data = {
            'from_zoom': from_zoom,
            'to_zoom': to_zoom,
            'extent': extent,
            'workers': workers
        }
        return super()._seed_cache(self.endpoint, data)


    def clear_cache(self) -> None:
        """
        Clear the cache of the raster.

        Returns:
            None

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.clear_cache()
        """
        super()._clear_cache(self.endpoint)
        

    @property
    def cache_size(self) -> int:
        """
        Get the size of the cache of the raster.

        Returns:
            int: The size of the cache of the raster.

        Example:
            >>> from geobox import GeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.cache_size
        """
        return super()._cache_size(self.endpoint)


    def to_async(self, async_client: 'AsyncGeoboxClient') -> 'AsyncRaster':
        """
        Switch to async version of the raster instance to have access to the async methods

        Args:
            async_client (AsyncGeoboxClient): The async version of the GeoboxClient instance for making requests.

        Returns:
            geobox.aio.raster.Raster: the async instance of the raster.

        Example:
            >>> from geobox import Geoboxclient
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.raster import Raster
            >>> client = GeoboxClient()
            >>> raster = Raster.get_raster(client, uuid="12345678-1234-5678-1234-567812345678")
            >>> async with AsyncGeoboxClient() as async_client:
            >>>     async_raster = raster.to_async(async_client)
        """
        from .aio.raster import Raster as AsyncRaster

        return AsyncRaster(api=async_client, uuid=self.uuid, data=self.data)


    def polygonize(self,
        output_layer_name: str,
        band_index: int = 1,
        value_field: Optional[str] = None,
        mask_nodata: bool = False,
        connectivity: PolygonizeConnectivity = PolygonizeConnectivity.connected_4,
        keep_values: Optional[str] = None,
        layer_name: Optional[str] = None,
        user_id: Optional[int] = None) -> 'Task':
        """
        Convert a raster to vector polygons

        vectorizes a raster (polygonize) to a vector dataset (*.gpkg). Only users with Publisher role or higher can perform this operation

        Args:
            api (GeoboxClient): The GeoboxClient instance for making requests
            raster (Raster): Raster instance
            output_layer_name  (str): Name for the output vector layer.
            band_index (int, optional): Raster band to polygonize. default: 1
            value_field (str, optional): Name of attribute field storing the pixel value. default: None
            mask_nodata (bool, optional): If True, NoData pixels are excluded using the band mask. default: False
            connectivity (PolygonizeConnectivity, optional): 4 or 8 connectivity for region grouping. default: PolygonizeConnectivity.connected_4 
            keep_values (str, optional): JSON array of values to keep (e.g., '[1,2,3]'). default: None
            layer_name (str, optional): Output layer name. default: None
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.polygonize(output_layer_name='test')
        """
        from .analysis import Analysis
        return Analysis.polygonize(self.api,
            self,
            output_layer_name=output_layer_name,
            band_index=band_index,
            value_field=value_field,
            mask_nodata=mask_nodata,
            connectivity=connectivity,
            keep_values=keep_values,
            layer_name=layer_name,
            user_id=user_id)


    def clip(self,
        layer: Union[VectorLayer, VectorLayerView],
        output_raster_name: str,
        where: Optional[str] = None,
        dst_nodata: int = -9999,
        crop: bool = True,
        resample: AnalysisResampleMethod = AnalysisResampleMethod.near,
        user_id: Optional[int] = None) -> 'Task':
        """
        Clip a raster using a vector layer as a mask

        clips a raster dataset using a vector layer as the clipping boundary. Only users with Publisher role or higher can perform this operation

        Args:
            api (GeoboxClient): The GeoboxClient instance for making requests
            raster (Raster): Raster instance
            layer (VectorLayer | VectorLayerView): VectorLayer or VectorLayerView instance
            output_raster_name (str): Name for the output raster dataset
            where (str, optional): Optional attribute filter, e.g. 'VEG=forest'.
            dst_nodata (int, optional): Output NoData value. default: -9999
            crop (bool, optional): True=shrink extent to polygon(s); False=keep full extent but mask outside. default: True
            resample (AnalysisResampleMethod, optional): Resampling method: 'near', 'bilinear', 'cubic', 'lanczos', etc. default: AnalysisResampleMethod.near
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> vector = client.get_vector(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.clip(layer=vector, output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.clip(self.api,
            self,
            layer=layer,
            output_raster_name=output_raster_name,
            where=where,
            dst_nodata=dst_nodata,
            crop=crop,
            resample=resample,
            user_id=user_id)


    def slope(self,
        output_raster_name: str,
        slope_units: SlopeUnit = SlopeUnit.degree,
        algorithm: AnalysisAlgorithm = AnalysisAlgorithm.Horn,
        scale: int = 1,
        compute_edges: bool = True,
        nodata_out: int = -9999,
        user_id: Optional[int] = None) -> 'Task':
        """
        Calculate slope from a DEM raster.

        This endpoint creates a slope raster from a Digital Elevation Model (DEM). Only users with Publisher role or higher can perform this operation.

        Args:
            output_raster_name (str): Name for the output raster dataset.
            slope_units (SlopeUnit, optional): Slope units: 'degree' or 'percent'. default: SlopeUnit.degree
            algorithm (AnalysisAlgorithm, optional): Algorithm: 'Horn' or 'ZevenbergenThorne'. default: AnalysisAlgorithm.Horn
            scale (int, optional): Ratio of vertical units to horizontal units. default: 1
            compute_edges (bool, optional): Whether to compute edges. default: True
            nodata (int, optional): NoData value for the output raster. default = -9999
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.slope(output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.slope(self.api,
            self,
            slope_units=slope_units,
            output_raster_name=output_raster_name,
            algorithm=algorithm,
            scale=scale,
            compute_edges=compute_edges,
            nodata_out=nodata_out,
            user_id=user_id)


    def aspect(self,
        output_raster_name: str,
        algorithm: AnalysisAlgorithm = AnalysisAlgorithm.Horn,
        trigonometric: bool = False,
        zero_for_flat: bool = True,
        compute_edges: bool = True,
        nodata_out: int = -9999,
        user_id: Optional[int] = None) -> 'Task':
        """
        Calculate aspect from a DEM raster.

        it creates an aspect raster (degrees 0–360) from a Digital Elevation Model (DEM).
        Only users with Publisher role or higher can perform this operation.

        Args:
            api (GeoboxClient): The GeoboxClient instance for making requests
            raster (Raster): DEM Raster instance
            output_raster_name (str): Name for the output raster dataset.
            algorithm (AnalysisAlgorithm, optional): Algorithm: 'Horn' or 'ZevenbergenThorne'. default: AnalysisAlgorithm.Horn
            trigonometric (bool, optional): False: azimuth (0°=N, 90°=E, clockwise); True: 0°=E, counter-clockwise. default: False
            zero_for_flat (bool, optional): Set flats (slope==0) to 0 instead of NoData. default: True
            compute_edges (bool, optional): Whether to compute edges. default: True
            nodata (int, optional): NoData value for the output raster. default = -9999
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.aspect(output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.aspect(self.api,
            self,
            output_raster_name=output_raster_name,
            algorithm=algorithm,
            trigonometric=trigonometric,
            zero_for_flat=zero_for_flat,
            compute_edges=compute_edges,
            nodata_out=nodata_out,
            user_id=user_id)


    def reclassify(self,
        output_raster_name: str,
        rules: str,
        default_value: Optional[int] = None,
        nodata_in: int = -9999,
        nodata_out: int = -9999,
        out_dtype: AnalysisDataType = AnalysisDataType.int16,
        inclusive: RangeBound = RangeBound.left,
        user_id: Optional[int] = None) -> 'Task':
        """
        Reclassify a raster using value mapping or class breaks.

        This endpoint reclassifies raster values according to specified rules. 
        Only users with Publisher role or higher can perform this operation.

        Args:
            output_raster_name (str): Name for the output reclassified raster dataset.
            rules (str): JSON string containing reclassification rules. 
                            For mode='exact', it should be a dict {old_value: new_value}. 
                            For mode='range', it should be a list of (low, high, new_value). 
                            Example for mode='exact': '{"1": 10, "2": 20, "3": 30}'. 
                            Example for mode='range': '[[0, 10, 1], [10, 20, 2], [20, 30, 3]]'.
                            the method would detect the mode type based on the rules input.
            default_value (str, optional): Value to assign when a pixel matches no rule.
            nodata_in (int, optional): NoData of input. If None, tries to get from the input raster.
            nodata_out (int, optional): NoData value to set on output band.
            out_dtype (AnalysisDataType, optional): Output data type. default: AnalysisDataType.int16
            inclusive (RangeBound, optional): Range bound semantics for mode='range': 'left', 'right', 'both', 'neither'. default: RangeBound.left
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.reclassify(output_raster_name='test', rules='{"1": 10, "2": 20, "3": 30}')
        """
        from .analysis import Analysis
        return Analysis.reclassify(self.api,
            self,
            output_raster_name=output_raster_name,
            rules=rules,
            default_value=default_value,
            nodata_in=nodata_in,
            nodata_out=nodata_out,
            out_dtype=out_dtype,
            inclusive=inclusive,
            user_id=user_id)


    def resample(self,
        output_raster_name: str,
        out_res: Optional[str] = None,
        scale_factor: Optional[str] = None,
        match_raster_uuid: Optional[str] = None,
        resample_method: AnalysisResampleMethod = AnalysisResampleMethod.near,
        dst_nodata: int = -9999,
        user_id: Optional[int] = None) -> 'Task':
        """
        Resample a raster to a different resolution.

        it resamples a raster using GDAL Warp. 
        Exactly one of out_res, scale_factor, or match_raster_uuid must be provided. 
        Only users with Publisher role or higher can perform this operation.

        Args:
            output_raster_name (str): Name for the output reclassified raster dataset.
            out_res (str, optional): Output resolution as 'x_res,y_res' (e.g., '10,10').
            scale_factor (int, optional): Scale factor (e.g., 2.0 for 2x finer resolution).
            match_raster_uuid (str, optional): UUID of reference raster to match resolution/extent.
            resample_method (AnalysisResampleMethod, optional): Resampling method: 'near', 'bilinear', 'cubic', 'lanczos', etc.
            dst_nodata (int, optional): Output NoData value.
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> raster.resample(output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.resample(self.api,
            self,
            output_raster_name=output_raster_name,
            out_res=out_res,
            scale_factor=scale_factor,
            match_raster_uuid=match_raster_uuid,
            resample_method=resample_method,
            dst_nodata=dst_nodata,
            user_id=user_id)


    def fill_nodata(self,
        output_raster_name: str,
        band: Union[int, str] = 1,
        nodata: Optional[int] = None,
        max_search_dist: Optional[int] = None,
        smoothing_iterations: Optional[int] = None,
        mask_raster_uuid: Optional[str] = None,
        user_id: Optional[int] = None) -> 'Task':
        """
        Fill NoData regions in a raster using GDAL's FillNodata algorithm.

        it fills gaps (NoData regions) in a raster by interpolating values from surrounding valid pixels. 
        This is commonly used for data cleaning and gap filling in remote sensing and elevation data. 
        Only users with Publisher role or higher can perform this operation.

        Args:
            output_raster_name (str): Name for the output filled raster dataset.
            band (int | str): 1-based band index to process or 'all' to process all bands. default: 1
            nodata (int, optional): NoData value to use. If None, uses the band's existing NoData.
            max_search_dist (int, optoinal): Maximum distance in pixels to search for valid data.
            smoothing_iterations (int, optional): Number of smoothing iterations to apply.
            mask_raster_uuid (str, optional): Optional UUID of a mask raster (0=masked, >0=valid).
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> task = raster.fill_nodata(output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.fill_nodata(self.api,
            self,
            output_raster_name=output_raster_name,
            band=band,
            nodata=nodata,
            max_search_dist=max_search_dist,
            smoothing_iterations=smoothing_iterations,
            mask_raster_uuid=mask_raster_uuid,
            user_id=user_id)


    def proximity(self,
        output_raster_name: str,
        dist_units: DistanceUnit = DistanceUnit.GEO,
        burn_value: int = 1,
        nodata: int = -9999,
        user_id: Optional[int] = None) -> 'Task':
        """
        Create a proximity (distance) raster from a raster layer.

        it creates a raster showing the distance from each pixel to the nearest pixel in the input raster layer. 
        Only users with Publisher role or higher can perform this operation.

        Args:
            output_raster_name (str): Name for the output proximity raster dataset.
            dist_units (DistanceUnit, optional): Distance units: 'GEO' for georeferenced units, 'PIXEL' for pixels. default: DistanceUnit.GEO
            burn_value (int, optional): Value treated as targets (distance 0). default: 1
            nodata (int, optional): NoData value to use in the output raster. default: -9999
            user_id (int, optional): specific user. priviledges required!

        Returns:
            Task: task instance of the process

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> task = raster.proximity(output_raster_name='test')
        """
        from .analysis import Analysis
        return Analysis.proximity(self.api,
            self,
            output_raster_name=output_raster_name,
            dist_units=dist_units,
            burn_value=burn_value,
            nodata=nodata,
            user_id=user_id)


    def profile(self,
        polyline: List,
        number_of_samples: int = 100,
        output_epsg: Optional[int] = None,
        include_distance: bool = True,
        treat_nodata_as_null: bool = True) -> Dict:
        """
        Create a profile form a raster along a path

        Args:
            polyline (List): Path coordinates as [x, y] pairs. Use raster CRS unless `output_epsg` is provided.
            number_of_samples (int, optional): Number of samples along the path. default: 100.
            output_epsg (int, optional): EPSG code for output coordinates. If None, use raster CRS.
            include_distance (bool, optional): Include cumulative distance for each sample. default: True.
            treat_nodata_as_null (bool, optional): Treat NoData pixels as null values. default: True.

        Returns:
            Dict: the profile result as geojson

        Example:
            >>> from geobox import GeoboxClient
            >>> client = GeoboxClient()
            >>> raster = client.get_raster(uuid="12345678-1234-5678-1234-567812345678")
            >>> task = raster.profile(polyline=[[0, 0], [10, 10]], number_of_samples=200)
        """
        endpoint = f"{self.endpoint}profile/"

        data = clean_data({
            'polyline': polyline,
            'number_of_samples': number_of_samples,
            'output_epsg': output_epsg,
            'include_distance': include_distance,
            'treat_nodata_as_null': treat_nodata_as_null
        })

        response = self.api.post(endpoint=endpoint, payload=data)
        return response
