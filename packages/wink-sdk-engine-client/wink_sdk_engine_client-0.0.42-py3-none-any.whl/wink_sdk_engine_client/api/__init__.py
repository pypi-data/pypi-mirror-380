# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_engine_client.api.configuration_api import ConfigurationApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_engine_client.api.configuration_api import ConfigurationApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
