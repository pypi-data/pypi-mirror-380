from datetime import datetime
from typing import Dict, List, Tuple

from pratac.config import ConfigManager


def prompt_for_cleaning_areas() -> List[str]:
    """Prompt user for cleaning areas with defaults."""
    default_areas = ["shower", "toilet", "floor", "kitchen"]

    print("\nCleaning Areas Setup")
    print("Default areas: shower, toilet, floor, kitchen")
    use_defaults = input("Use default cleaning areas? (y/n): ").strip().lower()

    if use_defaults in ["y", "yes", ""]:
        return default_areas

    areas = []
    print("\nEnter cleaning areas (press Enter with empty input to finish):")
    while True:
        area = input(f"Area {len(areas) + 1}: ").strip()
        if not area:
            break
        areas.append(area)

    if not areas:
        print("No areas entered, using defaults.")
        return default_areas

    return areas


def prompt_for_participants() -> Tuple[List[str], Dict[str, List[str]]]:
    """Prompt user for participants and their aliases."""
    participants = []
    aliases = {}

    print("\nParticipants Setup")
    while True:
        participant = input(f"Participant {len(participants) + 1} name (or press Enter to finish): ").strip()
        if not participant:
            break

        participants.append(participant)

        # Ask for aliases
        participant_aliases = []
        print(f"Enter aliases for {participant} (press Enter with empty input to finish):")
        while True:
            alias = input("  Alias: ").strip()
            if not alias:
                break
            participant_aliases.append(alias)

        if participant_aliases:
            aliases[participant] = participant_aliases

    if not participants:
        raise ValueError("At least one participant is required.")

    return participants, aliases


def prompt_for_start_date() -> str:
    """Prompt user for start date with default."""
    print("\nStart Date Setup")
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"Default start date: {today}")

    use_default = input("Use today as start date? (y/n): ").strip().lower()
    if use_default in ["y", "yes", ""]:
        return today

    while True:
        date_input = input("Enter start date (YYYY-MM-DD): ").strip()
        try:
            # Validate date format
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def preview_schedule(participants: List[str], cleaning_areas: List[str], aliases: Dict[str, List[str]]) -> None:
    """Show a preview of the cleaning schedule rotation."""
    print("\nSchedule Preview (first 4 weeks):")
    print("=" * 50)

    # Sort participants for consistent ordering
    sorted_participants = sorted(participants)

    for week in range(4):
        print(f"\nWeek {week + 1}:")
        for i, participant in enumerate(sorted_participants):
            area_index = (week + i) % len(cleaning_areas)
            area = cleaning_areas[area_index]

            # Show aliases if any
            participant_aliases = aliases.get(participant, [])
            if participant_aliases:
                alias_str = f" (aliases: {', '.join(participant_aliases)})"
            else:
                alias_str = ""

            print(f"  {participant}{alias_str}: {area}")


def run_interactive_setup() -> None:
    """Run the interactive setup process."""
    print("Pratac Interactive Setup")
    print("=" * 25)

    try:
        # Get cleaning areas
        cleaning_areas = prompt_for_cleaning_areas()

        # Get participants
        participants, aliases = prompt_for_participants()

        # Get start date
        start_date = prompt_for_start_date()

        # Show preview
        preview_schedule(participants, cleaning_areas, aliases)

        # Confirm setup
        print("\nConfiguration Summary:")
        print(f"Participants: {', '.join(participants)}")
        print(f"Cleaning areas: {', '.join(cleaning_areas)}")
        print(f"Start date: {start_date}")

        confirm = input("\nSave this configuration? (y/n): ").strip().lower()
        if confirm not in ["y", "yes"]:
            print("Setup cancelled.")
            return

        # Save configuration
        config = {
            "participants": participants,
            "participant_aliases": aliases,
            "cleaning_areas": cleaning_areas,
            "start_date": start_date
        }

        config_manager = ConfigManager()
        config_manager.save_config(config)

        print(f"\nConfiguration saved to {config_manager.get_config_path()}")
        print("You can now use 'pratac <person>' to get schedules!")

    except KeyboardInterrupt:
        print("\nSetup cancelled.")
    except Exception as e:
        print(f"\nError during setup: {e}")


def show_current_config() -> None:
    """Display the current configuration."""
    config_manager = ConfigManager()

    if not config_manager.config_exists():
        print("No custom configuration found. Using default settings.")
        print("\nDefault configuration:")
        print("Participants: martin/mato, adam/trumtulus, dano/danko, samo/kori")
        print("Cleaning areas: shower, toilet, floor, kitchen")
        print("Start date: 2022-09-14")
        return

    config = config_manager.load_config()
    if not config:
        print("Error reading configuration file.")
        return

    print("Current Configuration:")
    print("=" * 20)
    print(f"Config file: {config_manager.get_config_path()}")
    print(f"Participants: {', '.join(config.get('participants', []))}")

    aliases = config.get('participant_aliases', {})
    if aliases:
        print("Aliases:")
        for participant, participant_aliases in aliases.items():
            print(f"  {participant}: {', '.join(participant_aliases)}")

    print(f"Cleaning areas: {', '.join(config.get('cleaning_areas', []))}")
    print(f"Start date: {config.get('start_date', 'Not set')}")


def reset_config() -> None:
    """Reset configuration to defaults."""
    config_manager = ConfigManager()

    if not config_manager.config_exists():
        print("No custom configuration found. Already using defaults.")
        return

    confirm = input("This will delete your custom configuration and return to defaults. Continue? (y/n): ").strip().lower()
    if confirm in ["y", "yes"]:
        config_manager.delete_config()
        print("Configuration reset to defaults.")
    else:
        print("Reset cancelled.")