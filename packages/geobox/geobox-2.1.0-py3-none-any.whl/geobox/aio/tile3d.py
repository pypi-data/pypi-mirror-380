from typing import List, Dict, Optional, TYPE_CHECKING, Union
from urllib.parse import urljoin

from .base import AsyncBase

if TYPE_CHECKING:
    from . import AsyncGeoboxClient
    from .user import User
    from ..api import GeoboxClient as SyncGeoboxClient
    from ..tile3d import Tile3d as SyncTile3d


class Tile3d(AsyncBase):
    
    BASE_ENDPOINT = '3dtiles/'

    def __init__(self, 
                 api: 'AsyncGeoboxClient',
                 uuid: str,
                 data: Optional[Dict] = {}):
        """
        Initialize a 3D Tile instance.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            name (str): The name of the 3D Tile.
            uuid (str): The unique identifier for the 3D Tile.
            data (Dict): The data of the 3D Tile.
        """
        super().__init__(api, uuid=uuid, data=data)


    @classmethod
    async def get_3dtiles(cls, api: 'AsyncGeoboxClient', **kwargs) -> Union[List['Tile3d'], int]:
        """
        [async] Get list of 3D Tiles with optional filtering and pagination.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.

        Keyword Args:
            q (str): query filter based on OGC CQL standard. e.g. "field1 LIKE '%GIS%' AND created_at > '2021-01-01'"
            search (str): search term for keyword-based searching among search_fields or all textual fields if search_fields does not have value. NOTE: if q param is defined this param will be ignored.
            search_fields (str): comma separated list of fields for searching.
            order_by (str): comma separated list of fields for sorting results [field1 A|D, field2 A|D, …]. e.g. name A, type D. NOTE: "A" denotes ascending order and "D" denotes descending order.
            return_count (bool): Whether to return total count. default is False.
            skip (int): Number of items to skip. default is 0.
            limit (int): Number of items to return. default is 10.
            user_id (int): Specific user. privileges required.
            shared (bool): Whether to return shared maps. default is False.

        Returns:
            List[Tile3d] | int: A list of 3D Tile instances or the total number of 3D Tiles.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tiles = await Tile3d.get_3dtiles(client, q="name LIKE '%My tile%'")
            or  
            >>>     tiles = await client.get_3dtiles(q="name LIKE '%My tile%'")
        """ 
        params = {
           'f': 'json',
           'q': kwargs.get('q'),
           'search': kwargs.get('search'),
           'search_fields': kwargs.get('search_fields'),
           'order_by': kwargs.get('order_by'),
           'return_count': kwargs.get('return_count', False),
           'skip': kwargs.get('skip', 0),
           'limit': kwargs.get('limit', 10),
           'user_id': kwargs.get('user_id'),
           'shared': kwargs.get('shared', False)
        }
        return await super()._get_list(api, cls.BASE_ENDPOINT, params, factory_func=lambda api, item: Tile3d(api, item['uuid'], item))
    

    @classmethod
    async def get_3dtile(cls, api: 'AsyncGeoboxClient', uuid: str, user_id: int = None) -> 'Tile3d':
        """
        [async] Get a 3D Tile by its UUID.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            uuid (str): The UUID of the map to 3D Tile.
            user_id (int): Specific user. privileges required.

        Returns:
            Tile3d: The 3D Tile object.

        Raises:
            NotFoundError: If the 3D Tile with the specified UUID is not found.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            or  
            >>>     tile = await client.get_3dtile(uuid="12345678-1234-5678-1234-567812345678")
        """ 
        params = {
            'f': 'json',
            'user_id': user_id,
        }
        return await super()._get_detail(api, cls.BASE_ENDPOINT, uuid, params, factory_func=lambda api, item: Tile3d(api, item['uuid'], item))


    @classmethod
    async def get_3dtile_by_name(cls, api: 'AsyncGeoboxClient', name: str, user_id: int = None) -> Union['Tile3d', None]:
        """
        [async] Get a 3dtile by name

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            name (str): the name of the 3dtile to get
            user_id (int, optional): specific user. privileges required.

        Returns:
            Tile3d | None: returns the 3dtile if a 3dtile matches the given name, else None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile3d = await Tile3d.get_3dtile_by_name(client, name='test')
            or  
            >>>     tile3d = await client.get_3dtile_by_name(name='test')
        """
        tile3ds = await cls.get_3dtiles(api, q=f"name = '{name}'", user_id=user_id)
        if tile3ds and tile3ds[0].name == name:
            return tile3ds[0]
        else:
            return None
    

    async def update(self, **kwargs) -> Dict:
        """
        [async] Update the 3D Tile.

        Keyword Args:
            name (str): The name of the 3D Tile.
            display_name (str): The display name of the 3D Tile.
            description (str): The description of the 3D Tile.
            settings (Dict): The settings of the 3D Tile.
            thumbnail (str): The thumbnail of the 3D Tile.

        Returns:
            Dict: The updated 3D Tile data.

        Raises:
            ApiRequestError: If the API request fails.
            ValidationError: If the 3D Tile data is invalid.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     await tile.update_3dtile(display_name="New Display Name")
        """
        data = {
            "name": kwargs.get('name'),
            "display_name": kwargs.get('display_name'),   
            "description": kwargs.get('description'),
            "settings": kwargs.get('settings'),
            "thumbnail": kwargs.get('thumbnail'),
        }
        return await super()._update(self.endpoint, data)
    

    async def delete(self) -> None:
        """
        [async] Delete the 3D Tile.

        Returns:
            None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Map.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     await tile.delete()
        """
        await super().delete(self.endpoint)


    @property
    def thumbnail(self) -> str:
        """
        Get the thumbnail URL of the 3D Tile.

        Returns:
            str: The thumbnail url of the 3D Tile.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     tile.thumbnail
            'https://example.com/thumbnail.png'
        """
        return super().thumbnail()


    async def get_item(self, path: str) -> Dict:
        """
        [async] Get an Item from 3D Tiles

        Args:
            path (str): the path of the item.

        Returns:
            Dict: the data of the item.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            or  
            >>>     tile = await client.get_3dtile(uuid="12345678-1234-5678-1234-567812345678")
            >>>     item = await tile.get_item()
        """
        endpoint = f"{self.endpoint}{path}"
        return await self.api.get(endpoint)


    async def share(self, users: List['User']) -> None:
        """
        [async] Shares the 3D Tile with specified users.

        Args:
            users (List[User]): The list of user objects to share the 3D Tile with.

        Returns:
            None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     users = await client.search_users(search='John')
            >>>     await tile.share(users=users)
        """
        await super()._share(self.endpoint, users)
    

    async def unshare(self, users: List['User']) -> None:
        """
        [async] Unshares the 3D Tile with specified users.

        Args:
            users (List[User]): The list of user objects to unshare the 3D Tile with.

        Returns:
            None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     users = await client.search_users(search='John')
            >>>     await tile.unshare(users=users)
        """
        await super()._unshare(self.endpoint, users)


    async def get_shared_users(self, search: str = None, skip: int = 0, limit: int = 10) -> List['User']:
        """
        [async] Retrieves the list of users the 3D Tile is shared with.

        Args:
            search (str, optional): The search query.
            skip (int, optional): The number of users to skip.
            limit (int, optional): The maximum number of users to retrieve.

        Returns:
            List[User]: The list of shared users.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     await tile.get_shared_users(search='John', skip=0, limit=10)
        """
        params = {
            'search': search,
            'skip': skip,
            'limit': limit
        }
        return await super()._get_shared_users(self.endpoint, params)
    

    async def get_tileset_json(self) -> Dict:
        """
        [async] Get Tileset JSON of a 3D Tiles.
        
        Returns:
            Dict: The tileset JSON configuration.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> async with AsyncGeoboxClient() as client:
            >>>     tile = await Tile3d.get_3dtile(api=client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     tile_json = await tile.get_tileset_json()
        """
        endpoint = urljoin(self.endpoint, 'tileset.json') 
        return await self.api.get(endpoint)


    def to_sync(self, sync_client: 'SyncGeoboxClient') -> 'SyncTile3d':
        """
        Switch to sync version of the 3d tile instance to have access to the sync methods

        Args:
            sync_client (SyncGeoboxClient): The sync version of the GeoboxClient instance for making requests.

        Returns:
            geobox.tile3d.Tile3d: the sync instance of the 3d tile.

        Example:
            >>> from geobox import Geoboxclient
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.tile3d import Tile3d
            >>> client = GeoboxClient()
            >>> async with AsyncGeoboxClient() as async_client:
            >>>     tile = await Tile3d.get_3dtile(api=async_client, uuid="12345678-1234-5678-1234-567812345678")
            >>>     sync_tile = tile.to_sync(client)
        """
        from ..tile3d import Tile3d as SyncTile3d

        return SyncTile3d(api=sync_client, uuid=self.uuid, data=self.data)