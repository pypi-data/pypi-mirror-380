# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_affiliate_winklinks.api.syndicated_item_api import SyndicatedItemApi
    from wink_sdk_affiliate_winklinks.api.syndication_category_api import SyndicationCategoryApi
    from wink_sdk_affiliate_winklinks.api.syndication_settings_api import SyndicationSettingsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_affiliate_winklinks.api.syndicated_item_api import SyndicatedItemApi
from wink_sdk_affiliate_winklinks.api.syndication_category_api import SyndicationCategoryApi
from wink_sdk_affiliate_winklinks.api.syndication_settings_api import SyndicationSettingsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
