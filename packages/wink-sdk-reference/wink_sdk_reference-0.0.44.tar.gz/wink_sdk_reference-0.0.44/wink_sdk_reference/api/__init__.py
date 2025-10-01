# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_reference.api.geo_data_api import GeoDataApi
    from wink_sdk_reference.api.rate_provider_api import RateProviderApi
    from wink_sdk_reference.api.reference_api import ReferenceApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_reference.api.geo_data_api import GeoDataApi
from wink_sdk_reference.api.rate_provider_api import RateProviderApi
from wink_sdk_reference.api.reference_api import ReferenceApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
