# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_affiliate_sales_channel.api.affiliate_api import AffiliateApi
    from wink_sdk_affiliate_sales_channel.api.available_supplier_api import AvailableSupplierApi
    from wink_sdk_affiliate_sales_channel.api.relationship_request_api import RelationshipRequestApi
    from wink_sdk_affiliate_sales_channel.api.sales_channel_api import SalesChannelApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_affiliate_sales_channel.api.affiliate_api import AffiliateApi
from wink_sdk_affiliate_sales_channel.api.available_supplier_api import AvailableSupplierApi
from wink_sdk_affiliate_sales_channel.api.relationship_request_api import RelationshipRequestApi
from wink_sdk_affiliate_sales_channel.api.sales_channel_api import SalesChannelApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
