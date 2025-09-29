"""XP24 Action Table models for input actions and settings."""

from dataclasses import dataclass, field

from .input_action_type import InputActionType, InputTimeParam


@dataclass
class InputAction:
    """Represents an input action with type and parameter"""

    type: InputActionType
    param: InputTimeParam


@dataclass
class Xp24MsActionTable:
    """
    XP24 Action Table for managing input actions and settings.

    Each input has an action type (TOGGLE, TURNON, LEVELSET, etc.)
    with an optional parameter string.
    """

    # MS timing constants
    MS300 = 12
    MS500 = 20

    # Input actions for each input (default to TOGGLE with None parameter)
    input1_action: InputAction = field(
        default_factory=lambda: InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
    )
    input2_action: InputAction = field(
        default_factory=lambda: InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
    )
    input3_action: InputAction = field(
        default_factory=lambda: InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
    )
    input4_action: InputAction = field(
        default_factory=lambda: InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
    )

    # Boolean settings
    mutex12: bool = False  # Mutual exclusion between inputs 1-2
    mutex34: bool = False  # Mutual exclusion between inputs 3-4
    curtain12: bool = False  # Curtain setting for inputs 1-2
    curtain34: bool = False  # Curtain setting for inputs 3-4
    mutual_deadtime: int = MS300  # Master timing (MS300=12 or MS500=20)
