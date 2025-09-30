# Opcodes: Variables & Lists
OPCODE_VAR_VALUE               = "data_variable"
OPCODE_LIST_VALUE              = "data_listcontents"
NEW_OPCODE_VAR_VALUE           = "&variables::value of [VARIABLE]"
NEW_OPCODE_LIST_VALUE          = "&variables::value of [LIST]"
ANY_OPCODE_IMMEDIATE_BLOCK     = {OPCODE_VAR_VALUE, OPCODE_LIST_VALUE}
ANY_NEW_OPCODE_IMMEDIATE_BLOCK = {NEW_OPCODE_VAR_VALUE, NEW_OPCODE_LIST_VALUE}

# Opcodes: Custom Block Definitions
OPCODE_CB_DEF                  = "procedures_definition"
OPCODE_CB_DEF_RET              = "procedures_definition_return"
ANY_OPCODE_CB_DEF              =  {OPCODE_CB_DEF, OPCODE_CB_DEF_RET}

OPCODE_CB_PROTOTYPE            = "procedures_prototype"

OPCODE_CB_ARG_TEXT             = "argument_reporter_string_number"
OPCODE_CB_ARG_BOOL             = "argument_reporter_boolean"
ANY_OPCODE_CB_ARG              = {OPCODE_CB_ARG_TEXT, OPCODE_CB_ARG_BOOL}

NEW_OPCODE_CB_DEF              = "&customblocks::define custom block"
NEW_OPCODE_CB_DEF_REP          = "&customblocks::define custom block reporter"
ANY_NEW_OPCODE_CB_DEF          = {NEW_OPCODE_CB_DEF, NEW_OPCODE_CB_DEF_REP}

# Opcodes: Custom Block Calls
OPCODE_CB_CALL                 = "procedures_call"
NEW_OPCODE_CB_CALL             = "&customblocks::call custom block"

# Opcodes: Other Special Blocks
OPCODE_STOP_SCRIPT             = "control_stop"
OPCODE_CHECKBOX                = "checkbox"
NEW_OPCODE_CHECKBOX            = "&special::##CHECKBOX##"
OPCODE_POLYGON                 = "polygon"
NEW_OPCODE_POLYGON             = "&special::{{POLYGON MENU}}"
OPCODE_FILTER_LIST_INDEX       = "data_filterlistindex"
OPCODE_FILTER_LIST_ITEM        = "data_filterlistitem"
OPCODE_EXPANDABLE_IF           = "control_expandableIf"
OPCODE_EXPANDABLE_MATH         = "operator_expandableMath"


# Magic Numbers
OPCODE_NUM_VAR_VALUE           = 12
OPCODE_NUM_LIST_VALUE          = 13
ANY_OPCODE_NUM_IMMEDIATE_BLOCK = {OPCODE_NUM_VAR_VALUE, OPCODE_NUM_LIST_VALUE}
ANY_TEXT_INPUT_NUM             = {4, 5, 6, 7, 8, 9, 10, 11}


# SHA256 Secondary Values
SHA256_SEC_MAIN_ARGUMENT_NAME  = "MAIN_ARGUMENT_NAME"
SHA256_SEC_LOCAL_ARGUMENT_NAME = "LOCAL_ARGUMENT_NAME"
SHA256_SEC_VARIABLE            = "VARIABLE"
SHA256_SEC_LIST                = "LIST"
SHA256_SEC_BROADCAST_MSG       = "BROADCAST_MSG"
SHA256_SEC_DROPDOWN_VALUE      = "DROPDOWN_VALUE"
SHA256_SEC_TARGET_NAME         = "TARGET_NAME"
SHA256_SEC_MONITOR_VARIABLE_ID = "MONITOR_VARIABLE_ID"
SHA256_EDITOR_BUTTON_DV        = "SHA256_EDITOR_BUTTON_DV"

# Resource Paths
BUILTIN_EXTENSIONS_SOURCE_DIRECTORY = "builtin_extension_source/builtin_extensions"


__all__ = [
    "OPCODE_VAR_VALUE", "OPCODE_LIST_VALUE", "NEW_OPCODE_VAR_VALUE", "NEW_OPCODE_LIST_VALUE",
    "ANY_OPCODE_IMMEDIATE_BLOCK", "ANY_NEW_OPCODE_IMMEDIATE_BLOCK",
    "OPCODE_CB_DEF", "OPCODE_CB_DEF_RET", "ANY_OPCODE_CB_DEF",
    "OPCODE_CB_PROTOTYPE", 
    "OPCODE_CB_ARG_TEXT", "OPCODE_CB_ARG_BOOL", "ANY_OPCODE_CB_ARG",
    "NEW_OPCODE_CB_DEF", "NEW_OPCODE_CB_DEF_REP", "ANY_NEW_OPCODE_CB_DEF",
    "OPCODE_CB_CALL", "NEW_OPCODE_CB_CALL",
    "OPCODE_STOP_SCRIPT", "OPCODE_CHECKBOX", "NEW_OPCODE_CHECKBOX", "OPCODE_POLYGON", "NEW_OPCODE_POLYGON",
    "OPCODE_FILTER_LIST_INDEX", "OPCODE_FILTER_LIST_ITEM", "OPCODE_EXPANDABLE_IF", "OPCODE_EXPANDABLE_MATH",
    "OPCODE_NUM_VAR_VALUE", "OPCODE_NUM_LIST_VALUE", "ANY_OPCODE_NUM_IMMEDIATE_BLOCK",
    "ANY_TEXT_INPUT_NUM",

    "SHA256_SEC_MAIN_ARGUMENT_NAME", "SHA256_SEC_LOCAL_ARGUMENT_NAME",
    "SHA256_SEC_VARIABLE", "SHA256_SEC_LIST", "SHA256_SEC_BROADCAST_MSG",
    "SHA256_SEC_DROPDOWN_VALUE", "SHA256_SEC_TARGET_NAME", "SHA256_EDITOR_BUTTON_DV",

    "BUILTIN_EXTENSIONS_SOURCE_DIRECTORY",
]

