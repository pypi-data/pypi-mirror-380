import argparse
import sys

from pratac.definitions import get_person_offset


class ArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description='Cleaning schedule tool.')
        self.add_arguments()

    @staticmethod
    def valid_person(person: str) -> str:
        current_person_offset = get_person_offset()
        valid_people = ', '.join([f"{k}" for k in current_person_offset.keys()])
        value = person.lower()
        if value in valid_people:
            return value
        else:
            raise argparse.ArgumentTypeError(
                f"Invalid person: {person}.\nValid people are: {valid_people}")

    def add_arguments(self):
        # Create subparsers for different commands
        subparsers = self.parser.add_subparsers(dest='command', help='Available commands')

        # Init command
        subparsers.add_parser('init', help='Initialize interactive configuration')

        # Config command
        subparsers.add_parser('config', help='Show current configuration')

        # Reset command
        subparsers.add_parser('reset', help='Reset configuration to defaults')

        # Schedule command (explicit)
        schedule_parser = subparsers.add_parser('schedule', help='Get cleaning schedule for a person')
        schedule_parser.add_argument("person", type=self.valid_person, help="Person to generate schedule for.")
        schedule_parser.add_argument("week_offset", type=int, help="Week offset from current week.", nargs='?', default=0)

    def parse_args(self):
        # Check if first argument is a known command
        if len(sys.argv) >= 2 and sys.argv[1] in ['init', 'config', 'reset', 'schedule']:
            # Use normal subcommand parsing
            return self.parser.parse_args()

        # Handle backward compatibility: try to parse as old format
        if len(sys.argv) >= 2:
            try:
                person = self.valid_person(sys.argv[1])
                week_offset = int(sys.argv[2]) if len(sys.argv) >= 3 else 0

                # Create a namespace that matches the schedule command format
                from argparse import Namespace
                return Namespace(command='schedule', person=person, week_offset=week_offset)
            except (argparse.ArgumentTypeError, ValueError):
                # If it fails, show help
                self.parser.print_help()
                sys.exit(1)
        else:
            # No arguments provided
            self.parser.print_help()
            sys.exit(1)
