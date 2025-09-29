"""Unit tests for XP24 Action Table models."""

from xp.models.input_action_type import InputActionType, InputTimeParam
from xp.models.xp24_msactiontable import InputAction, Xp24MsActionTable


class TestInputAction:
    """Test cases for InputAction model"""

    def test_create_input_action_with_param(self):
        """Test creating InputAction with parameter"""
        action = InputAction(InputActionType.TURNON, InputTimeParam.T5SEC)

        assert action.type == InputActionType.TURNON
        assert action.param == InputTimeParam.T5SEC

    def test_create_input_action_without_param(self):
        """Test creating InputAction without parameter"""
        action = InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)

        assert action.type == InputActionType.TOGGLE
        assert action.param == InputTimeParam.NONE

    def test_input_action_equality(self):
        """Test InputAction equality comparison"""
        action1 = InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
        action2 = InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
        action3 = InputAction(InputActionType.TURNON, InputTimeParam.T5SEC)

        assert action1 == action2
        assert action1 != action3


class TestXp24ActionTable:
    """Test cases for Xp24ActionTable model"""

    def test_create_xp24_action_table_with_defaults(self):
        """Test creating Xp24ActionTable with default values"""
        action_table = Xp24MsActionTable()

        # Verify default input actions are TOGGLE with None param
        assert action_table.input1_action.type == InputActionType.TOGGLE
        assert action_table.input1_action.param == InputTimeParam.NONE
        assert action_table.input2_action.type == InputActionType.TOGGLE
        assert action_table.input2_action.param == InputTimeParam.NONE
        assert action_table.input3_action.type == InputActionType.TOGGLE
        assert action_table.input3_action.param == InputTimeParam.NONE
        assert action_table.input4_action.type == InputActionType.TOGGLE
        assert action_table.input4_action.param == InputTimeParam.NONE

        # Verify default boolean settings
        assert action_table.mutex12 is False
        assert action_table.mutex34 is False
        assert action_table.curtain12 is False
        assert action_table.curtain34 is False

        # Verify default MS timing
        assert action_table.mutual_deadtime == Xp24MsActionTable.MS300

    def test_xp24_action_table_constants(self):
        """Test XP24 action table timing constants"""
        assert Xp24MsActionTable.MS300 == 12
        assert Xp24MsActionTable.MS500 == 20

    def test_xp24_action_table_equality(self):
        """Test Xp24ActionTable equality comparison"""
        action_table1 = Xp24MsActionTable()
        action_table2 = Xp24MsActionTable()
        action_table3 = Xp24MsActionTable(
            input1_action=InputAction(InputActionType.TURNON, InputTimeParam.T5SEC),
            mutex12=True,
        )

        assert action_table1 == action_table2
        assert action_table1 != action_table3

    def test_xp24_action_table_dataclass_fields(self):
        """Test that all expected fields are present in dataclass"""
        action_table = Xp24MsActionTable()

        # Check that all expected attributes exist
        assert hasattr(action_table, "input1_action")
        assert hasattr(action_table, "input2_action")
        assert hasattr(action_table, "input3_action")
        assert hasattr(action_table, "input4_action")
        assert hasattr(action_table, "mutex12")
        assert hasattr(action_table, "mutex34")
        assert hasattr(action_table, "curtain12")
        assert hasattr(action_table, "curtain34")
        assert hasattr(action_table, "mutual_deadtime")

    def test_input_action_type_enum_coverage(self):
        """Test that all major InputActionType enum values work"""
        # Test a selection of action types
        test_actions = [
            InputActionType.VOID,
            InputActionType.TURNON,
            InputActionType.TURNOFF,
            InputActionType.TOGGLE,
            InputActionType.LEVELSET,
            InputActionType.SCENESET,
            InputActionType.LEARN,
        ]

        for action_type in test_actions:
            action = InputAction(action_type, InputTimeParam.NONE)
            assert action.type == action_type
            assert isinstance(action_type.value, int)

    def test_input_action_with_various_param_types(self):
        """Test InputAction with various parameter formats"""
        # Test with numeric string
        action1 = InputAction(InputActionType.LEVELSET, InputTimeParam.T60MIN)
        assert action1.param == InputTimeParam.T60MIN

        # Test with zero string
        action2 = InputAction(InputActionType.TURNON, InputTimeParam.NONE)
        assert action2.param == InputTimeParam.NONE

        # Test with None
        action3 = InputAction(InputActionType.TOGGLE, InputTimeParam.NONE)
        assert action3.param == InputTimeParam.NONE
