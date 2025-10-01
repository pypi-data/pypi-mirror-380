# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_facilities.api.guest_room_api import GuestRoomApi
    from wink_sdk_extranet_facilities.api.meeting_room_api import MeetingRoomApi
    from wink_sdk_extranet_facilities.api.restaurant_api import RestaurantApi
    from wink_sdk_extranet_facilities.api.spa_api import SpaApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_facilities.api.guest_room_api import GuestRoomApi
from wink_sdk_extranet_facilities.api.meeting_room_api import MeetingRoomApi
from wink_sdk_extranet_facilities.api.restaurant_api import RestaurantApi
from wink_sdk_extranet_facilities.api.spa_api import SpaApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
