# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_distribution.api.affiliate_api import AffiliateApi
    from wink_sdk_extranet_distribution.api.inventory_api import InventoryApi
    from wink_sdk_extranet_distribution.api.inventory_usage_api import InventoryUsageApi
    from wink_sdk_extranet_distribution.api.sales_channel_api import SalesChannelApi
    from wink_sdk_extranet_distribution.api.sales_channel_request_api import SalesChannelRequestApi
    from wink_sdk_extranet_distribution.api.scheduler_api import SchedulerApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_distribution.api.affiliate_api import AffiliateApi
from wink_sdk_extranet_distribution.api.inventory_api import InventoryApi
from wink_sdk_extranet_distribution.api.inventory_usage_api import InventoryUsageApi
from wink_sdk_extranet_distribution.api.sales_channel_api import SalesChannelApi
from wink_sdk_extranet_distribution.api.sales_channel_request_api import SalesChannelRequestApi
from wink_sdk_extranet_distribution.api.scheduler_api import SchedulerApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
