from arize.config import SDKConfiguration


class DatasetsClient:
    def __init__(self, sdk_config: SDKConfiguration):
        self._sdk_config = sdk_config

        # Import at runtime so it’s still lazy and extras-gated by the parent
        from arize._generated import api_client as gen

        # Use the shared generated client from the config
        self._api = gen.DatasetsApi(self._sdk_config.get_generated_client())

        # Forward methods to preserve exact runtime signatures/docs
        self.list = self._api.datasets_list
        self.get = self._api.datasets_get
        self.create = self._api.datasets_create
        self.delete = self._api.datasets_delete
        self.list_examples = self._api.datasets_list_examples
