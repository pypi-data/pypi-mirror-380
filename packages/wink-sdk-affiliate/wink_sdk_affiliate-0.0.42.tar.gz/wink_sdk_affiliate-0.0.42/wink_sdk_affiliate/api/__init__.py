# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_affiliate.api.account_manager_api import AccountManagerApi
    from wink_sdk_affiliate.api.affiliate_api import AffiliateApi
    from wink_sdk_affiliate.api.leads_api import LeadsApi
    from wink_sdk_affiliate.api.notification_api import NotificationApi
    from wink_sdk_affiliate.api.travel_agent_api import TravelAgentApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_affiliate.api.account_manager_api import AccountManagerApi
from wink_sdk_affiliate.api.affiliate_api import AffiliateApi
from wink_sdk_affiliate.api.leads_api import LeadsApi
from wink_sdk_affiliate.api.notification_api import NotificationApi
from wink_sdk_affiliate.api.travel_agent_api import TravelAgentApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
