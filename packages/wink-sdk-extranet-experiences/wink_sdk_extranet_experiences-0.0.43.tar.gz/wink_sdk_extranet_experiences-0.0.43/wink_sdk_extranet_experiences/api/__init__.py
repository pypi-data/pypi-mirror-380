# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_experiences.api.activity_api import ActivityApi
    from wink_sdk_extranet_experiences.api.attraction_api import AttractionApi
    from wink_sdk_extranet_experiences.api.place_api import PlaceApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_experiences.api.activity_api import ActivityApi
from wink_sdk_extranet_experiences.api.attraction_api import AttractionApi
from wink_sdk_extranet_experiences.api.place_api import PlaceApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
