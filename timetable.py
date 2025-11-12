# File: timetable.py
# Author: Victor Tarus
# Student ID: 1104794911
# This is my own work as defined by
# the University's Academic Misconduct Policy.


def print_header(title):
    print("=" * 70)
    print(title)
    print("=" * 70)


def print_details(
    title="Mr", author_name="Victor Tarus", email="tarvk002@mymail.unisa.edu.au"
):
    # FR1:Print out of details,title, author name and unisa email
    print_header("Timetable Manager")
    print(f"Title: {title}\nName: {author_name}\nEmail: {email}")
    print("=" * 70)


def get_valid_input(prompt):
    # Prompt user to give non empty input
    isValid = False
    value = ""
    while not isValid:
        value = input(prompt).strip()
        if value == "":
            print("Input cannot be empty.Please try again")
        else:
            isValid = True
    return value


def is_valid_time_format(time_str: str):
    """Validate time input. Accepts:
    - HH:MM (e.g., '14:30')
    - HH:MMAM/PM (e.g., '9:00am')
    - Single digit hour (e.g., '9')
    """
    time_str = time_str.strip().lower()

    if ":" in time_str:
        time_parts = time_str.split(":")
        hour_str = time_parts[0]
        minute_meridian_str = time_parts[1]

        meridian = None
        minute_str = minute_meridian_str

        # Extract meridian if present
        if minute_meridian_str.endswith("am") or minute_meridian_str.endswith("pm"):
            meridian = minute_meridian_str[-2:].upper()
            minute_str = minute_meridian_str[:-2]

        if hour_str.isdigit() and minute_str.isdigit():
            hour = convert_to_twenty_four_hour(hour_str, meridian)
            minute = int(minute_str)
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return True, f"{hour:02d}:{minute:02d}"

    elif time_str.isdigit():
        hour = int(time_str)
        if 0 <= hour <= 23:
            return True, f"{hour:02d}:00"  # Assume AM by default

    return False, None


def convert_to_twenty_four_hour(hour, meridian: str = None):
    # convert 12-hour time to 24 hour
    hour = int(hour)
    if meridian:
        meridian = meridian.upper()
        if meridian == "PM" and hour != 12:
            return hour + 12
        elif meridian == "AM" and hour == 12:
            return 0
    return hour


# return true if end_time > start_time
def is_end_time_later(start_time, end_time):
    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    return (end_hour, end_minute) > (start_hour, start_minute)


def get_time_from_user(prompt):
    # Prompt user for time
    isValid = False
    time_input = None
    time = None
    example = "(e.g, 10,10:00am,11:00pm,16:30)"

    while not isValid:
        time_input = get_valid_input(f"{prompt} {example}: ")
        isValid, time = is_valid_time_format(time_input)
        if not isValid:
            print(f"Invalid time format.Please try again")
    return time


def display_menu():
    # FR2:Display text-based menu
    print_header("📜Menu")
    print("1.🆕Create scheduled event")
    print("2.🛠️Update scheduled event ")
    print("3.🚮Delete scheduled event")
    print("4.🖨️Print timetable for the whole week")
    print("5.📇Print list of selected events for a day")
    print("6.💾Save timetable on File ")
    print("7.📥Load timetable from File")
    print("🔴Enter Q to Quit")


# Check if input is a digit between 1 and 7."
def is_valid_number(user_input: str):

    isValid: bool = False
    num = None
    if user_input.isdigit():
        num = int(user_input)
        if 1 <= num <= 7:
            isValid = True
    return isValid, num


def get_menu_choice(prompt="\nSelect from menu: Enter 1 - 7 or Q to quit: "):
    """Prompt user for choice and validate input."""
    error_msg = "Invalid input. Please enter a number between 1 - 7 or Q to quit."

    while True:
        user_input = get_valid_input(prompt)
        if user_input.upper() == "Q":
            return "Q"
        is_valid, num = is_valid_number(user_input)
        if is_valid:
            return num
        else:
            print(error_msg)


def days_of_week():
    # Return list of days in the week
    return [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]


def get_day_from_user(prompt):
    # Prompt the user for choice of day and validate input.

    for index, day in enumerate(days_of_week(), start=1):
        print(f"{index} : {day}", end=" ")
    print()
    day_selected = get_menu_choice(prompt)
    if isinstance(day_selected, str) and day_selected.upper() == "Q":
        print(f"🚫 Operation cancelled")
        return None
    return days_of_week()[day_selected - 1]


def get_event_details_from_user():
    # Get event details from user
    print_header("🏗️Create a new event")
    day = get_day_from_user("🌞Select a day (1–7) or Q to cancel:")
    if not day:
        return None
    title = get_valid_input("📝Enter event title: ")
    start = get_time_from_user("⏰Enter start time ")
    flag = True
    while flag:
        end = get_time_from_user("⌛Enter end time")
        if is_end_time_later(start, end):
            flag = False
        else:
            print("❌ Error: End time must be later than start time, please try again")

    location = input("📍🗺️Enter event location:").strip()

    return {
        "day": day,
        "title": title,
        "start_time": start,
        "end_time": end,
        "location": location,
    }


# print event
def print_event_details(event, index=None):
    prefix = f"{index}. " if index else ""
    loc_str = f" at 📍🗺️ {event['location']}" if event["location"] else ""
    print(f"{prefix} ⏳ {event['start_time']} - {event['end_time']}: 📝 {event['title']}{loc_str}")


# Create an empty timetable
def create_empty_timetable():

    return {day: [] for day in days_of_week()}


# Search for events whose title or location contains the keyword
def search_events(timetable, keyword):

    keyword = keyword.lower()
    matching_events = []

    for day_name, events_on_day in timetable.items():
        for event in events_on_day:
            title = event["title"].lower()
            location = event["location"].lower()
            if keyword in title or keyword in location:
                # Add a copy of the event with the day included
                event_with_day = {"day": day_name, **event}
                matching_events.append(event_with_day)
    # Sort by day order, then start time
    day_order = {day: index for index, day in enumerate(days_of_week())}
    matching_events.sort(
        key=lambda event: (day_order[event["day"]], event["start_time"])
    )
    return matching_events


#  Check if new_event overlaps with any in existing_events.Optionally skip a specific event (used during updates).
def is_time_overlap(new_event, existing_events, skip_event=None):
    for event in existing_events:
        if skip_event and event == skip_event:
            continue
        if not (
            new_event["end_time"] <= event["start_time"]
            or new_event["start_time"] >= event["end_time"]
        ):
            return True
    return False


def add_event(timetable):
    """Add a new event to the timetable.
    Ensures no overlapping times for the same day.
    Returns the updated timetable dictionary.
    """
    new_event = get_event_details_from_user()
    if not new_event:
        return timetable
    day_name = new_event["day"]
    day_events = timetable[day_name]

    # check for time overlap
    if is_time_overlap(new_event, day_events):
        print("❌ Error: Event overlaps with an existing event")
        return timetable
    day_events.append(new_event)
    day_events.sort(key=lambda event: event["start_time"])
    print(f"🗓️Event '{new_event['title']}' added successfully on {day_name}.")
    return timetable


# print list of events briefly
def print_events_list_brief(event_matches):
    for index, event in enumerate(event_matches, start=1):
        print_event_details(event, index)



# update existing event using a keyword search
def update_event(timetable):
    print_header("Update event in the timetable")
    keyword = get_valid_input("Enter keyword to search (title or location):")

    matches = search_events(timetable, keyword)
    if not matches:
        print("❌ No events found matching the given keyword")
        return timetable

    # Show matching events
    print_header("Matching events")
    print_events_list_brief(matches)

    # Select event to update
    flag = True
    while flag:
        selected = input("\nEnter number of event to update or Q to cancel: ").strip()
        if selected.upper() == "Q":
            print("Update cancelled")
            return timetable
        elif selected.isdigit() and 1 <= int(selected) <= len(matches):
            selected_event = matches[int(selected) - 1]
            flag = False
        else:
            print("❌ Invalid event selected. Try again.")

    # Prompt for new details
    print_header("Update details (leave blank to keep current values)")
    new_title = (
        input(f"New title [{selected_event['title']}]: ").strip()
        or selected_event["title"]
    )
    flag2 = True
    while flag2:
        new_start_time = (
            get_time_from_user(f"New start time [{selected_event['start_time']}]")
            or selected_event["start_time"]
        )
        new_end_time = (
            get_time_from_user(f"New end time [{selected_event['end_time']}]")
            or selected_event["end_time"]
        )
        if is_end_time_later(new_start_time, new_end_time):
            flag2 = False
        else:
            print("❌ Error: End time must be later than start time. Please try again.")

    new_location = (
        input(f"New location [{selected_event['location']}]: ").strip()
        or selected_event["location"]
    )
    day_name = selected_event["day"]
    day_events = timetable[day_name]
    # updated event
    updated_event = {
        "title": new_title,
        "start_time": new_start_time,
        "end_time": new_end_time,
        "location": new_location,
        "day": day_name,
    }

    # check for overlap
    if is_time_overlap(updated_event, day_events, skip_event=selected_event):
        print(
            "❌ Error: Updated event overlaps with an existing event. Update cancelled."
        )
        return timetable
    # Apply update

    for i, event in enumerate(day_events):
        if (
            event["title"] == selected_event["title"]
            and event["start_time"] == selected_event["start_time"]
            and event["end_time"] == selected_event["end_time"]
            and event["location"] == selected_event["location"]
        ):
            day_events[i] = {
                "title": new_title,
                "start_time": new_start_time,
                "end_time": new_end_time,
                "location": new_location,
                "day": day_name,
            }
            print("✅ Event updated successfully.")
            break

    return timetable


# delete an existing event using keyword search
def delete_event(timetable):
    print_header("🚮🚮 Delete Event From Timetable. 🚮🚮")
    keyword = get_valid_input(
        "🔍Enter keyword to search for the event (title or location):"
    )

    matches = search_events(timetable, keyword)
    if not matches:
        print("4️⃣0️⃣4️⃣ No events found matching your keyword. 4️⃣0️⃣4️⃣")
        return timetable

    # Show matching event
    print_header("🎯 Matching events🎯 ")
    print_events_list_brief(matches)

    # Select event to delete
    flag = True
    while flag:
        selected = input("\n🔢 Enter number of event to delete or Q to cancel: ").strip()
        if selected.upper() == "Q":
            print("Delete cancelled.")
            return timetable
        if selected.isdigit() and 1 <= int(selected) <= len(matches):
            event_to_delete = matches[int(selected) - 1]
            flag = False
        else:
            print("👎Invalid selection. Try again.")
    # Remove event form timetable
    day_name = event_to_delete["day"]
    day_events = timetable[day_name]

    updated_day_events = []
    event_deleted = False
    for event in day_events:
        if (
            event["title"] == event_to_delete["title"]
            and event["start_time"] == event_to_delete["start_time"]
            and event["end_time"] == event_to_delete["end_time"]
            and event["location"] == event_to_delete["location"]
            and not event_deleted
        ):
            event_deleted = True
            print(
                f"✅ Event '{event_to_delete['title']}' deleted successfully from {day_name}."
            )
        else:
            updated_day_events.append(event)
    timetable[day_name] = updated_day_events
    if not event_deleted:
        print("❌  Error: Something went wrong, event could not be deleted")

    return timetable


# Print timetable for the entire week starting from the choosen day
def print_full_timetable(timetable):
    start_day = get_day_from_user("Enter start of the week(1-7): ") 
    days = days_of_week()
    start_index = days.index(start_day)

    ordered_days = days[start_index:] + days[:start_index]
    print_header("Full Week Time Table")
    # print eveents day by day
    for day in ordered_days:
        print(f"\n📅{day}")
        print("-" * 70)
        if timetable[day]:
            for event in sorted(timetable[day], key=lambda event: event["start_time"]):
                print_event_details(event)
        else:
            print("🧐 No events scheduled for the day.")
        print()

# Print events for a day
def print_events_for_selected_day(timetable):
    day = get_day_from_user("Enter the day of the week (1–7):")
    print_header(f"Events for {day}")
    if not day:
        return  
    if timetable[day]:
        for event in sorted(timetable[day], key=lambda event: event["start_time"]):
            print_event_details(event)
    else:
        print("🧐 No events scheduled for the day.\n")

# Save time table to textfile
def save_timetable(timetable):
    default_filename = "timetable.txt"
    filename = input(f"Enter file name to save timetable [default: {default_filename}]: ").strip()
    if not filename:
        filename = default_filename
    elif not filename.lower().endswith(".txt"):
        filename += ".txt"

    file = None
    try:
        file = open(filename, "w",encoding="utf-8")
        for day in days_of_week():
            file.write(day+ ":\n")
            if not timetable[day]:
                file.write("No events")
            else:
                for event in timetable[day]:
                    line = f"  {event['start_time']} - {event['end_time']}, {event['title']}"
                    if event['location']:
                        line += f", {event['location']}"
                    line += "\n"
                    file.write(line)
            file.write("\n")
        print_header(f"✅ Timetable saved to {filename}")
    except Exception as e:
        print(f"❌ Something went wrong,timetable was not saved: {e}")
    finally:
        if file:
          file.close()

# Load timetable from text file
def load_timetable():
    default_filename = "timetable.txt"
    filename = input(f"Enter file name to load timetable [default: {default_filename}]: ").strip()
    if not filename:
        filename = default_filename
    elif not filename.lower().endswith(".txt"):
        filename += ".txt"
    # initialize empty timetable
    timetable = create_empty_timetable()
    file = None
    loaded_successfully = True
    try:
        file = open(filename, "r", encoding="utf-8")
        loaded_successfully = True

        current_day = None
        for line in file:
            line = line.strip()
            if not line: 
                continue #skip empty lines
            if line.endswith(":"):
                current_day = line[:-1]
            elif line.startswith("No events") or not current_day:
                continue #skip empty lines
            else:
                # line format "start_time-end_time, title, location"
                try:
                    parts = line.split(",", 2)
                    time_part = parts[0].strip()
                    title = parts[1].strip()
                    location = parts[2].strip() if len(parts)==3 else "" #location is optional

                    start_time, end_time = map(str.strip, time_part.split("-",1))
                    event = {
                        "title":title.strip(),
                        "start_time":start_time,
                        "end_time":end_time,
                        "location":location.strip(),
                        "day":current_day

                    }
                    timetable[current_day].append(event)
                  
                except ValueError as e:
                    print(f"⚠️ line could not be read : {e}")
    except FileNotFoundError:
        print("❌ File not found. Starting with an empty timetable.")
    except Exception as e:
        print(f"❌ Something went wrong.Timetable can't be loaded: {e}")
    finally:
        if file:
            file.close()
        if loaded_successfully:
            print_header(f"✅ Timetable from file {filename} loaded.")
    return timetable


def main():
    print_details()
    timetable = load_timetable()
    flag = True

    while flag:
        display_menu()
        choice = get_menu_choice()
        if choice == "Q":
            print("👋 Goodbye. Timetable Manager closed.")
            flag = False
        elif choice == 1:
            timetable = add_event(timetable)
        elif choice == 2:
            timetable = update_event(timetable)
        elif choice == 3:
            timetable = delete_event(timetable)
        elif choice == 4:
            print_full_timetable(timetable)
        elif choice == 5:
            print_events_for_selected_day(timetable)
        elif choice == 6:
            save_timetable(timetable)
        elif choice == 7:
            timetable = load_timetable()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f" ⚠️ An unexpected error occurred: {e}")
