# Practical 9 - Cars
# tarvk002
#


def convert_items_to_int(position_from_end, data_list):
    abs_pos = abs(position_from_end)
    if len(data_list) < abs_pos:
        raise ValueError(f"List must contain atleast {abs_pos} items")
    items_to_convert = data_list[position_from_end:]
    converted_items = [int(item) for item in items_to_convert]
    data_list[position_from_end:] = converted_items
    return data_list


def load_cars():
    cars = []
    """Load and return a list of cars data using dictionary."""
    keys = ["make", "model", "year", "doors", "seats", "kms"]
    try:
        with open("cars.txt", "r") as file:
            for line in file:
                values = convert_items_to_int(-4, line.strip().split())
                zipped_pairs = zip(keys, values)
                car = dict(zipped_pairs)
                cars.append(car)
        return cars
    except Exception as e:
        print(f"Something went wrong: {e}")


def print_cars(cars):
    """Print the list of cars in a table format."""
    if len(cars) == 0:
        print("No cars available")
        return
    print("Make\tModel\t\tYear\tDoors\tSeats\tKms")
    print("===============================================")
    for car in cars:

        print(
            f"{car['make']}\t{car['model']:<10}\t{car['year']}\t{car['doors']}\t{car['seats']}\t{car['kms']}"
        )

    pass


def find_cars(cars, key, value):
    """Find and return a new list of cars with matching key value."""
    found_cars = []
    for car in cars:
        if car.get(key) == value:
            found_cars.append(car)

    return found_cars


def sort_cars(cars, key):
    """Sort cars in the list with key and return True if successful."""
    try:
        cars.sort(key=lambda car: car[key])
        return True
    except KeyError:
        return False


def main():
    """Main function to run at start."""
    cars = load_cars()  # load car records from input file

    command = ""
    while command != "quit":
        print()  # Print an empty line.

        # Get user intput of the command to run.
        command = input("Command [print, find, sort, quit]: ")

        # Print command.
        if command == "print":
            print_cars(cars)

        # Find command.
        elif command == "find":
            # Get user input of field and value for searching.
            field = input("Field: ")
            value = input("Value: ")

            # Convert the value to int if numeric.
            if value.isnumeric():
                value = int(value)

            # Find cars matching the field value and print.
            result = find_cars(cars, field.lower(), value)
            print_cars(result)

        # Sort command.
        elif command == "sort":
            # Get user input of field to sort with.
            field = input("Sort by which field? ")

            # Sort the cars in key
            success = sort_cars(cars, field.lower())
            if success:
                print("Sorted the cars in:", field.capitalize())
            else:
                print("Cannot sort the cars with:", field)

    print("Good bye!")


# Start with running the main function.
main()
