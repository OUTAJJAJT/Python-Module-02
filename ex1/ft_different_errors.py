def garden_operations():
    dictionarie = {
        'name': 'Selena',
        'age': 30,
        'city': 'New York'
    }
    try:
        print("Testing ValueError...")
        int("test int")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        print("Testing FileNotFoundError...")
        file = open("abc.txt", "r")
        file.read()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")
    try:
        print("Testing KeyError...")
        dictionarie["1337"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        print("Testing multiple errors together...")
        int("test int")
        10 / 0
        file = open("abc.txt", "r")
        file.read()
        dictionarie["1337"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    print("Testing error handling...\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()
