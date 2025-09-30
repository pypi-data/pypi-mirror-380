from pratac.config import ConfigManager

# Default hardcoded configuration (preserved for backward compatibility)
_default_person_offset = {
    ("martin", "mato"): 0,
    ("adam", "trumtulus"): 1,
    ("dano", "danko"): 2,
    ("simona", "simi"): 3,
    ("all"): 4
}
_default_room_offset = {
    0: "shower",
    1: "toilet",
    2: "floor",
    3: "kitchen",
}
_default_start_date = "2022-09-14"

# Configuration manager
_config_manager = ConfigManager()

def get_person_offset():
    """Get person offset dictionary from config file or default hardcoded values."""
    config_person_offset = _config_manager.get_person_offset()
    return config_person_offset if config_person_offset is not None else _default_person_offset

def get_room_offset():
    """Get room offset dictionary from config file or default hardcoded values."""
    config_room_offset = _config_manager.get_room_offset()
    return config_room_offset if config_room_offset is not None else _default_room_offset

def get_start_date():
    """Get start date from config file or default hardcoded value."""
    config_start_date = _config_manager.get_start_date()
    return config_start_date if config_start_date is not None else _default_start_date

# Dynamic properties that update based on config
person_offset = get_person_offset()
room_offset = get_room_offset()

def get_persons_offset(person_name: str) -> int:
    current_person_offset = get_person_offset()
    for key in current_person_offset:
        if person_name in key:
            return current_person_offset[key]
