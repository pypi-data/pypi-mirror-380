# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from code_size_analyzer_client.api.analyzer_api import AnalyzerApi
    from code_size_analyzer_client.api.asyncapi_api import AsyncapiApi
    from code_size_analyzer_client.api.default_api import DefaultApi
    from code_size_analyzer_client.api.parser_api import ParserApi
    from code_size_analyzer_client.api.results_api import ResultsApi

else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from code_size_analyzer_client.api.analyzer_api import AnalyzerApi
from code_size_analyzer_client.api.asyncapi_api import AsyncapiApi
from code_size_analyzer_client.api.default_api import DefaultApi
from code_size_analyzer_client.api.parser_api import ParserApi
from code_size_analyzer_client.api.results_api import ResultsApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
