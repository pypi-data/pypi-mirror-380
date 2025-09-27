from typing import List, Dict, Optional, TYPE_CHECKING, Union
from urllib.parse import urljoin

from .base import AsyncBase

if TYPE_CHECKING:
    from . import AsyncGeoboxClient
    from ..api import GeoboxClient as SyncGeoboxClient
    from ..plan import Plan as SyncPlan


class Plan(AsyncBase):

    BASE_ENDPOINT = 'plans/'

    def __init__(self,
                 api: 'AsyncGeoboxClient',
                 plan_id: int,
                 data: Optional[Dict] = {}):
        """
        Initialize a plan instance.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            plan_id (str): The id for the plan.
            data (Dict, optional): The data of the plan.
        """
        super().__init__(api, data=data)
        self.plan_id = plan_id
        self.endpoint = urljoin(self.BASE_ENDPOINT, str(self.id))


    @classmethod
    async def get_plans(cls, api: 'AsyncGeoboxClient', **kwargs) -> Union[List['Plan'], int]:
        """
        [async] Get list of plans with optional filtering and pagination.

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
            shared (bool): Whether to return shared plans. default is False.

        Returns:
            List[Plan] | int: A list of plan instances or the total number of plans.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plans = await Plan.get_plan(client, q="name LIKE '%My plan%'")
            or  
            >>>     plans = await client.get_plan(q="name LIKE '%My plan%'")
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
        return await super()._get_list(api, cls.BASE_ENDPOINT, params, factory_func=lambda api, item: Plan(api, item['id'], item))


    @classmethod
    async def create_plan(cls, 
                    api: 'AsyncGeoboxClient', 
                    name: str,
                    plan_color: str,
                    storage: int,
                    concurrent_tasks: int,
                    daily_api_calls: int,
                    monthly_api_calls: int,
                    daily_traffic: int,
                    monthly_traffic: int,
                    daily_process: int,
                    monthly_process: int,
                    number_of_days: int = None,
                    display_name: str = None,
                    description: str = None) -> 'Plan':
        """
        [async] Create a new plan.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            name (str): The name of the plan.
            plan_color (str): hex value of the color. e.g. #000000.
            storage (int): storage value in bytes. must be greater that 1.
            concurrent_tasks (int): number of concurrent tasks. must be greater that 1.
            daily_api_calls (int): number of daily api calls. must be greater that 1.
            monthly_api_calls (int): number of monthly api calls. must be greater that 1.
            daily_traffic (int): number of daily traffic. must be greater that 1.
            monthly_traffic (int): number of monthly traffic. must be greater that 1.
            daily_process (int): number of daily processes. must be greater that 1.
            monthly_process (int): number of monthly processes. must be greater that 1.
            number_of_days (int, optional): number of days. must be greater that 1.
            display_name (str, optional): display name of the plan.
            description (str, optional): description of the plan.

        Returns:
            Plan: The newly created plan instance.

        Raises:
            ValidationError: If the plan data is invalid.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plan = await Plan.create_plan(client, 
            ...                                 name="new_plan",
            ...                                 display_name=" New Plan",
            ...                                 description="new plan description",
            ...                                 plan_color="#000000",
            ...                                 storage=10,
            ...                                 concurrent_tasks=10,
            ...                                 daily_api_calls=10,
            ...                                 monthly_api_calls=10,
            ...                                 daily_traffic=10,
            ...                                 monthly_traffic=10,
            ...                                 daily_process=10,
            ...                                 monthly_process=10,
            ...                                 number_of_days=10)
            or  
            >>>     plan = await client.create_plan(name="new_plan",
            ...                                 display_name=" New Plan",
            ...                                 description="new plan description",
            ...                                 plan_color="#000000",
            ...                                 storage=10,
            ...                                 concurrent_tasks=10,
            ...                                 daily_api_calls=10,
            ...                                 monthly_api_calls=10,
            ...                                 daily_traffic=10,
            ...                                 monthly_traffic=10,
            ...                                 daily_process=10,
            ...                                 monthly_process=10,
            ...                                 number_of_days=10)
        """
        data = {
            "name": name,
            "display_name": display_name,
            "description": description,
            "plan_color": plan_color,
            "storage": storage,
            "concurrent_tasks": concurrent_tasks,
            "daily_api_calls": daily_api_calls,
            "monthly_api_calls": monthly_api_calls,
            "daily_traffic": daily_traffic,
            "monthly_traffic": monthly_traffic,
            "daily_process": daily_process,
            "monthly_process": monthly_process,
            "number_of_days": number_of_days
        }
        return await super()._create(api, cls.BASE_ENDPOINT, data, factory_func=lambda api, item: Plan(api, item['id'], item))


    @classmethod
    async def get_plan(cls, api: 'AsyncGeoboxClient', plan_id: int) -> 'Plan':
        """
        [async] Get a plan by its id.

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            plan_id (int): The id of the plan to get.

        Returns:
            Plan: The plan object

        Raises:
            NotFoundError: If the plan with the specified id is not found.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plan = await Plan.get_plan(client, plan_id=1)
            or  
            >>>     plan = await client.get_plan(plan_id=1)
        """
        params = {
            'f': 'json'
        }
        return await super()._get_detail(api, cls.BASE_ENDPOINT, plan_id, params, factory_func=lambda api, item: Plan(api, item['id'], item))
    

    @classmethod
    async def get_plan_by_name(cls, api: 'AsyncGeoboxClient', name: str) -> Union['Plan', None]:
        """
        [async] Get a plan by name

        Args:
            api (AsyncGeoboxClient): The AsyncGeoboxClient instance for making requests.
            name (str): the name of the plan to get

        Returns:
            Plan | None: returns the plan if a plan matches the given name, else None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plan = await Plan.get_plan_by_name(client, name='test')
            or  
            >>>     plan = await client.get_plan_by_name(name='test')
        """
        plans = await cls.get_plans(api, q=f"name = '{name}'")
        if plans and plans[0].name == name:
            return plans[0]
        else:
            return None


    async def update(self, **kwargs) -> Dict:
        """
        [async] Update the plan

        Keyword Args:
            name (str): The name of the plan.
            plan_color (str): hex value of the color. e.g. #000000.
            storage (int): storage value in bytes. must be greater that 1.
            concurrent_tasks (int): number of concurrent tasks. must be greater that 1.
            daily_api_calls (int): number of daily api calls. must be greater that 1.
            monthly_api_calls (int): number of monthly api calls. must be greater that 1.
            daily_traffic (int): number of daily traffic. must be greater that 1.
            monthly_traffic (int): number of monthly traffic. must be greater that 1.
            daily_processes (int): number of daily processes. must be greater that 1.
            monthly_processes (int): number of monthly processes. must be greater that 1.
            number_of_days (int): number of days. must be greater that 1.
            display_name (str): display name of the plan.
            description (str): description of the plan.

        Returns:
            Dict: The updated plan data.

        Raises:
            ValidationError: If the plan data is invalid.

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plan = await Plan.get_plan(client, plan_id=1)
            >>>     await plan.update(display_name="New Display Name")
        """
        data = {
            "name": kwargs.get('name'),
            "display_name": kwargs.get('display_name'),
            "description": kwargs.get('description'),
            "plan_color": kwargs.get('plan_color'),
            "storage": kwargs.get('storage'),
            "concurrent_tasks": kwargs.get('concurrent_tasks'),
            "daily_api_calls": kwargs.get('daily_api_calls'),
            "monthly_api_calls": kwargs.get('monthly_api_calls'),
            "daily_traffic": kwargs.get('daily_traffic'),
            "monthly_traffic": kwargs.get('monthly_traffic'),
            "daily_process": kwargs.get('daily_process'),
            "monthly_process": kwargs.get('monthly_process'),
            "number_of_days": kwargs.get('number_of_days')
        }
        return await super()._update(self.endpoint, data)


    async def delete(self) -> None:
        """
        [async] Delete the plan.

        Returns:
            None

        Example:
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> async with AsyncGeoboxClient() as client:
            >>>     plan = await Plan.get_plan(client, plan_id=1)
            >>>     await plan.delete()
        """
        await super().delete(self.endpoint)
        self.plan_id = None


    def to_sync(self, sync_client: 'SyncGeoboxClient') -> 'SyncPlan':
        """
        Switch to sync version of the plan instance to have access to the sync methods

        Args:
            sync_client (SyncGeoboxClient): The sync version of the GeoboxClient instance for making requests.

        Returns:
            geobox.plan.Plan: the sync instance of the plan.

        Example:
            >>> from geobox import Geoboxclient
            >>> from geobox.aio import AsyncGeoboxClient
            >>> from geobox.aio.plan import Plan
            >>> client = GeoboxClient()
            >>> async with AsyncGeoboxClient() as async_client:
            >>>     plan = await Plan.get_plan(async_client, plan_id=1)
            >>>     sync_plan = plan.to_sync(client)
        """
        from ..plan import Plan as SyncPlan

        return SyncPlan(api=sync_client, plan_id=self.plan_id, data=self.data)