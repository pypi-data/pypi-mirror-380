import json
from pathlib import Path
from typing import Dict, Optional, Tuple, Union


class ConfigManager:
    def __init__(self):
        self.config_dir = Path.home() / ".pratac"
        self.config_file = self.config_dir / "config.json"

    def get_config_path(self) -> Path:
        return self.config_file

    def config_exists(self) -> bool:
        return self.config_file.exists()

    def load_config(self) -> Optional[Dict]:
        if not self.config_exists():
            return None

        try:
            with open(self.config_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

    def save_config(self, config: Dict) -> None:
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, "w") as f:
            json.dump(config, f, indent=2)

    def delete_config(self) -> None:
        if self.config_exists():
            self.config_file.unlink()

    def get_person_offset(self) -> Dict[Union[Tuple[str, ...], str], int]:
        config = self.load_config()
        if not config:
            return None

        participants = config.get("participants", [])
        aliases = config.get("participant_aliases", {})

        # Sort participants alphabetically for consistent ordering
        sorted_participants = sorted(participants)

        person_offset = {}
        for i, participant in enumerate(sorted_participants):
            # Create tuple with participant and their aliases
            participant_aliases = aliases.get(participant, [])
            if participant_aliases:
                key = tuple([participant.lower()] + [alias.lower() for alias in participant_aliases])
            else:
                key = (participant.lower(),)
            person_offset[key] = i

        # Add "all" key
        person_offset["all"] = len(sorted_participants)

        return person_offset

    def get_room_offset(self) -> Dict[int, str]:
        config = self.load_config()
        if not config:
            return None

        cleaning_areas = config.get("cleaning_areas", [])
        return {i: area for i, area in enumerate(cleaning_areas)}

    def get_start_date(self) -> Optional[str]:
        config = self.load_config()
        if not config:
            return None

        return config.get("start_date")