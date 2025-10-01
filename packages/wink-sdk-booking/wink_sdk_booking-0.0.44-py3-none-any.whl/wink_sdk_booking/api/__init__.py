# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_booking.api.booking_api import BookingApi
    from wink_sdk_booking.api.checkout_api import CheckoutApi
    from wink_sdk_booking.api.review_api import ReviewApi
    from wink_sdk_booking.api.shopping_cart_api import ShoppingCartApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_booking.api.booking_api import BookingApi
from wink_sdk_booking.api.checkout_api import CheckoutApi
from wink_sdk_booking.api.review_api import ReviewApi
from wink_sdk_booking.api.shopping_cart_api import ShoppingCartApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
