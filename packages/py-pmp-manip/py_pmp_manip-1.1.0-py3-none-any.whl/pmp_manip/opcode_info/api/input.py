from __future__ import annotations
from typing     import Literal

from pmp_manip.utility import grepr_dataclass, GEnum

from pmp_manip.important_consts         import OPCODE_POLYGON, OPCODE_FILTER_LIST_INDEX, OPCODE_FILTER_LIST_ITEM
from pmp_manip.opcode_info.api.dropdown import DropdownType, BuiltinDropdownType


@grepr_dataclass(grepr_fields=["type", "menu"])
class InputInfo:
    """
    The information about a input of a certain opcode
    """
    
    type: InputType
    menu: MenuInfo | None = None

class InputMode(GEnum):
    """
    Mostly determines the behaviour of inputs
    """

    @property
    def can_be_missing(self) -> bool:
        """
        Return wether an input of this mode is allowed to be missing. 
        (I did not come up with some inputs just disappearing when empty; go ask the Scratch Team)

        Returns:
            wether an input of this mode is allowed to be missing
        """
        return self.value[0]  
    
    # (can be missing?, index)
    BLOCK_AND_TEXT               = (False, 0)
    BLOCK_AND_MENU_TEXT          = (False, 1)
    BLOCK_AND_BOOL               = (True , 2) # can not miss anymore, but lets respect older projects
    BLOCK_ONLY                   = (True , 3)
    SCRIPT                       = (True , 4)
    BLOCK_AND_BROADCAST_DROPDOWN = (False, 5)
    BLOCK_AND_DROPDOWN           = (False, 6)
    FORCED_EMBEDDED_BLOCK        = (False, 7)

class InputType(GEnum):
    """
    The type of a block input, which can be used for one or many opcodes. It can be a Builtin or Custom one.
    The input type has only little influence, except those which can contain a dropdown. Then it will be used for dropdown validation.
    Its superior input mode mostly determines its behaviour
    """

    name: str
    value: tuple[InputMode, int|str|None, DropdownType|None, int] 
    # (InputMode, magic number or forced opcode, corresponding dropdown type, index)

    @property
    def mode(self) -> InputMode:
        """
        Get the superior input mode

        Returns:
            the input mode
        """
        return self.value[0]

    @property
    def corresponding_dropdown_type(self) -> "DropdownType":
        """
        Get the corresponding dropdown type

        Returns:
            the corresponding dropdown type
        """
        assert self.mode in {
            InputMode.BLOCK_AND_MENU_TEXT, 
            InputMode.BLOCK_AND_BROADCAST_DROPDOWN,
            InputMode.BLOCK_AND_DROPDOWN,
        }
        return self.value[2]

    @property
    def embedded_block_opcode(self) -> str:
        """
        Get the old block opcode which must exist in the input.
        """
        assert self.mode == InputMode.FORCED_EMBEDDED_BLOCK 
        return self.value[1]

    @property
    def magic_number(self) -> int | None:
        """
        Get the inner magic number used in first representation of inputs
        """
        return self.value[1]

    @property
    def outer_magic_number(self) -> Literal[1] | Literal[2]:
        """
        Get the outer magic number used in first representation of inputs if no block exists
        """
        if (self.mode in {InputMode.BLOCK_ONLY, InputMode.SCRIPT}) or (self is BuiltinInputType.NUMBER_SPECIAL):
            return 2
        else:
            return 1

    @classmethod
    def get_by_cb_default(cls, default: str) -> "InputType":
        """
        Get the input type by its corresponding default in custom blocks

        Returns:
            the input type
        """
        match default:
            case "":
                return BuiltinInputType.TEXT
            case "false":
                return BuiltinInputType.BOOLEAN

class BuiltinInputType(InputType):
    """
    A built-in type of a block input, which can be used for one or many opcodes.
    The input type has only little influence, except those which can contain a dropdown. Then it will be used for dropdown validation.
    Its superior input mode mostly determines its behaviour
    """

    # (InputMode, magic number or forced opcode, corresponding dropdown type, index)
    # BLOCK_AND_TEXT
    TEXT                = (InputMode.BLOCK_AND_TEXT, 10, None, 0)
    COLOR               = (InputMode.BLOCK_AND_TEXT,  9, None, 1)
    DIRECTION           = (InputMode.BLOCK_AND_TEXT,  8, None, 2)
    INTEGER             = (InputMode.BLOCK_AND_TEXT,  7, None, 3)
    POSITIVE_INTEGER    = (InputMode.BLOCK_AND_TEXT,  6, None, 4)
    POSITIVE_NUMBER     = (InputMode.BLOCK_AND_TEXT,  5, None, 5)
    NUMBER              = (InputMode.BLOCK_AND_TEXT,  4, None, 6)
    NUMBER_SPECIAL      = (InputMode.BLOCK_AND_TEXT,  4, None, 7)

    # BLOCK_AND_MENU_TEXT
    NOTE                = (InputMode.BLOCK_AND_MENU_TEXT, None, BuiltinDropdownType.NOTE, 0)

    # BLOCK_AND_BOOL
    BOOLEAN             = (InputMode.BLOCK_AND_BOOL, None, None, 0)
    
    # BLOCK_ONLY
    ROUND               = (InputMode.BLOCK_ONLY, None, None, 0)

    # SCRIPT
    SCRIPT              = (InputMode.SCRIPT, None, None, 0)

    # BLOCK_AND_BROADCAST_DROPDOWN
    BROADCAST           = (InputMode.BLOCK_AND_BROADCAST_DROPDOWN, 11, BuiltinDropdownType.BROADCAST, 0)

    # BLOCK_AND_DROPDOWN
    STAGE_OR_OTHER_SPRITE             = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.STAGE_OR_OTHER_SPRITE            ,  0)
    CLONING_TARGET                    = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.CLONING_TARGET                   ,  1)
    MOUSE_OR_OTHER_SPRITE             = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.MOUSE_OR_OTHER_SPRITE            ,  2)
    MOUSE_EDGE_OR_OTHER_SPRITE        = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.MOUSE_EDGE_OR_OTHER_SPRITE       ,  3)
    MOUSE_EDGE_MYSELF_OR_OTHER_SPRITE = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.MOUSE_EDGE_MYSELF_OR_OTHER_SPRITE,  4)
    KEY                               = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.KEY                              ,  5)
    UP_DOWN                           = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.UP_DOWN                          ,  6)
    FINGER_INDEX                      = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.FINGER_INDEX                     ,  7)
    RANDOM_MOUSE_OR_OTHER_SPRITE      = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.RANDOM_MOUSE_OR_OTHER_SPRITE     ,  8)
    COSTUME                           = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.COSTUME                          ,  9)
    BACKDROP                          = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.BACKDROP                         , 10)
    COSTUME_PROPERTY                  = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.COSTUME_PROPERTY                 , 11)
    MYSELF_OR_OTHER_SPRITE            = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.MYSELF_OR_OTHER_SPRITE           , 12)
    SOUND                             = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.SOUND                            , 13)
    MATRIX                            = (InputMode.BLOCK_AND_DROPDOWN, None, BuiltinDropdownType.MATRIX                           , 14)
    
    # FORCED_EMBEDDED_BLOCK
    POLYGON                           = (InputMode.FORCED_EMBEDDED_BLOCK, OPCODE_POLYGON          , None, 0)
    FILTER_LIST_INDEX                 = (InputMode.FORCED_EMBEDDED_BLOCK, OPCODE_FILTER_LIST_INDEX, None, 1)
    FILTER_LIST_ITEM                  = (InputMode.FORCED_EMBEDDED_BLOCK, OPCODE_FILTER_LIST_ITEM , None, 2)

@grepr_dataclass(grepr_fields=["opcode", "inner"])
class MenuInfo:
    """
    The information about a menu in an input
    """
    
    opcode: str
    inner : str

__all__ = ["InputInfo", "InputMode", "InputType", "BuiltinInputType", "MenuInfo"]
