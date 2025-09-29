from kivy.uix.boxlayout import BoxLayout

from carveracontroller.addons.probing.operations.ConfigUtils import ConfigUtils
from carveracontroller.addons.probing.operations.Bore.BoreParameterDefinitions import BoreParameterDefinitions


class BoreSettings(BoxLayout):
    config_filename = "bore-probe-settings.json"
    config = {}

    def __init__(self, **kwargs):
        self.config = ConfigUtils.load_config(self.config_filename)
        self.config = self.order_config(self.config)
        super(BoreSettings, self).__init__(**kwargs)

    def setting_changed(self, key: str, value: float):
        param = getattr(BoreParameterDefinitions, key, None)
        if param is None:
            raise KeyError(f"Invalid key '{key}'")

        self.config[param.code] = value
        self.config = self.order_config(self.config)
        ConfigUtils.save_config(self.config, self.config_filename)

    def order_config(self, config: dict[str, float]):
        order = ["X", "Y", "Z", "J", "D", "H", "F", "K", "L", "R", "C", "Q", "E", "S", "I"]
        temp_config = {}
        for key in order:
            if key in config:
                temp_config[key] = config[key]
        return temp_config

    def get_setting(self, key: str) -> str:
        param = getattr(BoreParameterDefinitions, key, None)
        return str(self.config[param.code] if param.code in self.config else "")

    def get_config(self):
        return self.config;
