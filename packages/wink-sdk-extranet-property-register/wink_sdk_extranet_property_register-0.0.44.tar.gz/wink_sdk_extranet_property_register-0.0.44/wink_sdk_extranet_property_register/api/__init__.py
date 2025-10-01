# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_extranet_property_register.api.leads_api import LeadsApi
    from wink_sdk_extranet_property_register.api.registration_api import RegistrationApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_extranet_property_register.api.leads_api import LeadsApi
from wink_sdk_extranet_property_register.api.registration_api import RegistrationApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
