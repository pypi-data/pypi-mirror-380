# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_user_settings.api.user_settings_api import UserSettingsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_user_settings.api.user_settings_api import UserSettingsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
