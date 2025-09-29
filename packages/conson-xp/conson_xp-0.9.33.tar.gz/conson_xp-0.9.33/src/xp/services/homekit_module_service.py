import logging
from typing import Optional, List, Any

from pydispatch import dispatcher

from xp.models.action_type import ActionType
from xp.models.homekit_conson_config import ConsonModuleConfig, ConsonModuleListConfig
from xp.services.homekit_cache_service import HomeKitCacheService
from xp.services.telegram_output_service import TelegramOutputService


class HomekitModuleService:

    def __init__(self, config_path: str = "conson.yml"):

        # Set up logging
        self.logger = logging.getLogger(__name__)

        self.conson_modules_config = ConsonModuleListConfig.from_yaml(config_path)
        self.telegram_output_service = TelegramOutputService()
        self.cache_service = HomeKitCacheService()

        # Connect to PyDispatcher events
        self._setup_event_listeners()

    def get_module_by_name(self, name: str) -> Optional[ConsonModuleConfig]:
        """Get a module by its name"""
        module = next(
            (
                module
                for module in self.conson_modules_config.root
                if module.name == name
            ),
            None,
        )
        self.logger.debug(
            f"Module search by name '{name}': {'found' if module else 'not found'}"
        )
        return module

    def get_module_by_serial(self, serial_number: str) -> Optional[ConsonModuleConfig]:
        """Get a module by its serial number"""
        module = next(
            (
                module
                for module in self.conson_modules_config.root
                if module.serial_number == serial_number
            ),
            None,
        )
        self.logger.debug(
            f"Module search by serial '{serial_number}': {'found' if module else 'not found'}"
        )
        return module

    def get_modules_by_type(self, module_type: str) -> List[ConsonModuleConfig]:
        """Get all modules of a specific type"""
        modules = [
            module
            for module in self.conson_modules_config.root
            if module.module_type == module_type
        ]
        self.logger.debug(f"Found {len(modules)} modules of type '{module_type}'")
        return modules

    def _setup_event_listeners(self) -> None:
        """Set up PyDispatcher event listeners"""
        dispatcher.connect(
            self._outlet_set_outlet_in_use, signal="outlet_set_outlet_in_use"
        )
        dispatcher.connect(
            self._on_outlet_get_outlet_in_use, signal="outlet_get_outlet_in_use"
        )
        dispatcher.connect(self._on_accessory_set_on, signal="accessory_set_on")
        dispatcher.connect(self._on_accessory_get_on, signal="accessory_get_on")

    # noinspection PyUnusedLocal
    def _outlet_set_outlet_in_use(self, sender: Any, **kwargs: Any) -> None:
        serial_number: Optional[Any] = kwargs.get("serial_number")
        output_number: Optional[Any] = kwargs.get("output_number")
        value: Optional[Any] = kwargs.get("value")

        self.logger.info(
            f"_outlet_set_outlet_in_use {{ sender: {sender}, serial_number: {serial_number}, output_number: {output_number}, value: {value} }}"
        )

    # noinspection PyUnusedLocal
    def _on_outlet_get_outlet_in_use(self, sender: Any, **kwargs: Any) -> None:
        serial_number: Optional[Any] = kwargs.get("serial_number")
        output_number: Optional[Any] = kwargs.get("output_number")

        self.logger.info(
            f"_on_outlet_get_outlet_in_use {{ sender: {sender}, serial_number: {serial_number}, output_number: {output_number}}}"
        )

    # noinspection PyUnusedLocal
    def _on_accessory_set_on(self, sender: Any, **kwargs: Any) -> None:
        """Handle accessory set_on events from PyDispatcher"""
        serial_number: Optional[str] = kwargs.get("serial_number")
        output_number: Optional[int] = kwargs.get("output_number")
        value: Optional[bool] = kwargs.get("value")

        self.logger.info(
            f"_on_accessory_set_on {{ sender: {sender}, serial_number: {serial_number} output_number: {output_number} }}"
        )

        if serial_number is None:
            self.logger.warning("Invalid serial_number")
            return

        if output_number is None:
            self.logger.warning("Invalid output_number")
            return

        module = self.get_module_by_serial(serial_number)
        if not module:
            self.logger.warning(f"Module not found for serial {serial_number}")
            return

        action_type = ActionType.PRESS
        if value:
            action_type = ActionType.RELEASE

        self.cache_service.send_action(
            serial_number=serial_number,
            output_number=output_number,
            action_type=action_type,
        )

    # noinspection PyUnusedLocal
    def _on_accessory_get_on(self, sender: Any, **kwargs: Any) -> bool:
        """Handle accessory get_on events from PyDispatcher"""
        serial_number: Optional[str] = kwargs.get("serial_number")
        output_number: Optional[int] = kwargs.get("output_number")

        self.logger.info(
            f"_on_accessory_get_on {{ sender: {sender}, serial_number: {serial_number}, output_number: {output_number}}}"
        )

        if serial_number is None:
            self.logger.warning("Invalid serial_number")
            return False

        if output_number is None:
            self.logger.warning("Invalid output_number")
            return False

        module = self.get_module_by_serial(serial_number)
        if not module:
            self.logger.warning(f"Module not found for serial {serial_number}")
            return False

        # tag = f"E{module.module_type_code}L{module.link_number}I{output_number}"
        tag = f"E{module.module_type_code:02d}L{module.link_number:02d}"
        response = self.cache_service.get(key=serial_number, tag=tag)
        if response.data is None:
            self.logger.warning(f"No output_telegram for serial {serial_number}")
            return False

        result = self.telegram_output_service.parse_status_response(response.data)
        return result[output_number]
