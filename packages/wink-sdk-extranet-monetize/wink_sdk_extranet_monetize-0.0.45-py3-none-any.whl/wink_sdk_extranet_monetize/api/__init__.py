# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_monetize.api.add_on_api import AddOnApi
    from wink_sdk_extranet_monetize.api.cancellation_policy_api import CancellationPolicyApi
    from wink_sdk_extranet_monetize.api.daily_rate_api import DailyRateApi
    from wink_sdk_extranet_monetize.api.inventory_api import InventoryApi
    from wink_sdk_extranet_monetize.api.inventory_usage_api import InventoryUsageApi
    from wink_sdk_extranet_monetize.api.master_rate_api import MasterRateApi
    from wink_sdk_extranet_monetize.api.promotion_api import PromotionApi
    from wink_sdk_extranet_monetize.api.promotion_bundle_api import PromotionBundleApi
    from wink_sdk_extranet_monetize.api.rate_plan_api import RatePlanApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_monetize.api.add_on_api import AddOnApi
from wink_sdk_extranet_monetize.api.cancellation_policy_api import CancellationPolicyApi
from wink_sdk_extranet_monetize.api.daily_rate_api import DailyRateApi
from wink_sdk_extranet_monetize.api.inventory_api import InventoryApi
from wink_sdk_extranet_monetize.api.inventory_usage_api import InventoryUsageApi
from wink_sdk_extranet_monetize.api.master_rate_api import MasterRateApi
from wink_sdk_extranet_monetize.api.promotion_api import PromotionApi
from wink_sdk_extranet_monetize.api.promotion_bundle_api import PromotionBundleApi
from wink_sdk_extranet_monetize.api.rate_plan_api import RatePlanApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
