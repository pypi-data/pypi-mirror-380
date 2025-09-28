from framework.base_class import BaseTestCase
from framework.global_attribute import CONTEXT, _FRAMEWORK_CONTEXT, CONFIG


class __BaseScript(BaseTestCase):
    BaseTestCase.context = CONTEXT
    BaseTestCase.config = CONFIG
    BaseTestCase.http = _FRAMEWORK_CONTEXT.get("_http")


class BaseScript(__BaseScript):
    app = None

    def run(self):
        raise NotImplementedError

    def default_app(self, app):
        return app or self.app
