# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from wink_sdk_travel_agent.api.analytics_api import AnalyticsApi
    from wink_sdk_travel_agent.api.travel_agent_api import TravelAgentApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from wink_sdk_travel_agent.api.analytics_api import AnalyticsApi
from wink_sdk_travel_agent.api.travel_agent_api import TravelAgentApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
