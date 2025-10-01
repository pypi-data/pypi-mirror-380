import logging

from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver
from pyhap.const import CATEGORY_LIGHTBULB

from xp.models.homekit.homekit_config import HomekitAccessoryConfig
from xp.models.homekit.homekit_conson_config import ConsonModuleConfig
from xp.models.telegram.action_type import ActionType
from xp.services.conbus.conbus_output_service import ConbusOutputService
from xp.services.telegram.telegram_output_service import TelegramOutputService


class LightBulb(Accessory):
    """Fake lightbulb, logs what the client sets."""

    category = CATEGORY_LIGHTBULB
    output_service = ConbusOutputService()
    telegram_output_service = TelegramOutputService()

    accessory: HomekitAccessoryConfig
    module: ConsonModuleConfig

    def __init__(
        self,
        driver: AccessoryDriver,
        module: ConsonModuleConfig,
        accessory: HomekitAccessoryConfig,
    ):
        super().__init__(driver, accessory.description)

        self.logger = logging.getLogger(__name__)
        self.accessory = accessory
        self.module = module

        self.logger.info(
            "Creating Lightbulb { serial_number : %s, output_number: %s }",
            module.serial_number,
            accessory.output_number,
        )

        serial = f"{module.serial_number}.{accessory.output_number:02d}"
        version = accessory.id
        manufacturer = "Conson"
        model = ("XP24_lightbulb",)
        serv_light = self.add_preload_service("Lightbulb")
        self.set_info_service(version, manufacturer, model, serial)

        self.char_on = serv_light.configure_char(
            "On", getter_callback=self.get_on, setter_callback=self.set_on
        )

    def set_on(self, value: bool) -> None:
        # Emit event using PyDispatcher
        self.logger.debug(f"set_on: {bool}")
        result = self.output_service.send_action(
            serial_number=self.module.serial_number,
            output_number=self.accessory.output_number,
            action_type=(ActionType.ON_RELEASE if value else ActionType.OFF_PRESS),
        )
        self.logger.debug(f"result: {result}")

    def get_on(self) -> bool:
        # Emit event and get response
        self.logger.debug("get_on")
        response = self.output_service.get_output_state(
            serial_number=self.module.serial_number,
        )
        self.logger.debug(f"result: {response}")
        if response.received_telegrams:
            result = self.telegram_output_service.parse_status_response(
                response.received_telegrams[0]
            )
            return result[3 - self.accessory.output_number]

        return False
