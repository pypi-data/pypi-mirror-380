# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_channel_manager.api.channel_manager_api import ChannelManagerApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_channel_manager.api.channel_manager_api import ChannelManagerApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
