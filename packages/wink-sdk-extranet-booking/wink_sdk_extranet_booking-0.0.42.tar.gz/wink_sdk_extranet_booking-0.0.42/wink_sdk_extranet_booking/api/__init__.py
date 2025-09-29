# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_booking.api.analytics_api import AnalyticsApi
    from wink_sdk_extranet_booking.api.booking_api import BookingApi
    from wink_sdk_extranet_booking.api.calendar_sync_api import CalendarSyncApi
    from wink_sdk_extranet_booking.api.review_api import ReviewApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_booking.api.analytics_api import AnalyticsApi
from wink_sdk_extranet_booking.api.booking_api import BookingApi
from wink_sdk_extranet_booking.api.calendar_sync_api import CalendarSyncApi
from wink_sdk_extranet_booking.api.review_api import ReviewApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
