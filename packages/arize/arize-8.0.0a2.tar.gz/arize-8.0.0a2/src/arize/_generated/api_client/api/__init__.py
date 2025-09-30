# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from arize._generated.api_client.api.datasets_api import DatasetsApi
    from arize._generated.api_client.api.experiments_api import ExperimentsApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from arize._generated.api_client.api.datasets_api import DatasetsApi
from arize._generated.api_client.api.experiments_api import ExperimentsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
