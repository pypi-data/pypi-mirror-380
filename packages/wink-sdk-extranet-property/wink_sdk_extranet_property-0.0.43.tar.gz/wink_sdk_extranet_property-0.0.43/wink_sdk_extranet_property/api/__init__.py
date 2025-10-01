# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_property.api.channel_manager_api import ChannelManagerApi
    from wink_sdk_extranet_property.api.geo_location_api import GeoLocationApi
    from wink_sdk_extranet_property.api.lifestyle_api import LifestyleApi
    from wink_sdk_extranet_property.api.media_api import MediaApi
    from wink_sdk_extranet_property.api.policy_api import PolicyApi
    from wink_sdk_extranet_property.api.property_api import PropertyApi
    from wink_sdk_extranet_property.api.recognition_api import RecognitionApi
    from wink_sdk_extranet_property.api.reference_api import ReferenceApi
    from wink_sdk_extranet_property.api.social_network_api import SocialNetworkApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_property.api.channel_manager_api import ChannelManagerApi
from wink_sdk_extranet_property.api.geo_location_api import GeoLocationApi
from wink_sdk_extranet_property.api.lifestyle_api import LifestyleApi
from wink_sdk_extranet_property.api.media_api import MediaApi
from wink_sdk_extranet_property.api.policy_api import PolicyApi
from wink_sdk_extranet_property.api.property_api import PropertyApi
from wink_sdk_extranet_property.api.recognition_api import RecognitionApi
from wink_sdk_extranet_property.api.reference_api import ReferenceApi
from wink_sdk_extranet_property.api.social_network_api import SocialNetworkApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
