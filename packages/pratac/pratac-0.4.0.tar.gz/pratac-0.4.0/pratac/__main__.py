from argparse import Namespace
from datetime import datetime

from pratac.argparser import ArgParser
from pratac.definitions import get_person_offset, get_persons_offset, get_room_offset, get_start_date
from pratac.interactive import reset_config, run_interactive_setup, show_current_config


def calculate_week_offset(offset: int) -> int:
    start_date = get_start_date()
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    current_datetime = datetime.now()
    week_offset = (((current_datetime - start_datetime).days) + (offset * 7)) // 7
    return week_offset

def process_schedule_args(args: Namespace) -> None:
    week_num = calculate_week_offset(args.week_offset)
    get_schedule(args.person, week_num)

def get_schedule(person: str, week_num: int) -> None:
    current_person_offset = get_person_offset()
    current_room_offset = get_room_offset()

    room_type = week_num % (len(current_room_offset))
    if person == "all":
        for key in current_person_offset:
            if key != "all":
                persons_offset = get_persons_offset(key[0])
                print(f"For week {week_num} the schedule for {key[0]} is: {current_room_offset.get((room_type + persons_offset) % len(current_room_offset))}")
        return
    persons_offset = get_persons_offset(person)
    print(f"For week {week_num} the schedule for {person} is: {current_room_offset.get((room_type + persons_offset) % len(current_room_offset))}")

def main():
    args = ArgParser().parse_args()

    if args.command == 'schedule':
        process_schedule_args(args)
    elif args.command == 'init':
        run_interactive_setup()
    elif args.command == 'config':
        show_current_config()
    elif args.command == 'reset':
        reset_config()
    else:
        # This should not happen due to argparser logic, but handle gracefully
        print("Unknown command. Use 'pratac --help' for usage information.")

if __name__ == "__main__":
    main()