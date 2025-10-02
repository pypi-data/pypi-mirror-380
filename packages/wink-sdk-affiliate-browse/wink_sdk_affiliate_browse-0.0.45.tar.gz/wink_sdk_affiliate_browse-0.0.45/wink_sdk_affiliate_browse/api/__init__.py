# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_affiliate_browse.api.browse_api import BrowseApi
    from wink_sdk_affiliate_browse.api.curated_list_api import CuratedListApi
    from wink_sdk_affiliate_browse.api.dynamic_list_api import DynamicListApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_affiliate_browse.api.browse_api import BrowseApi
from wink_sdk_affiliate_browse.api.curated_list_api import CuratedListApi
from wink_sdk_affiliate_browse.api.dynamic_list_api import DynamicListApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
