def garden_operations():
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        1 // 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        plants = {"rose": 5, "tulip": 3}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("Testing ZeroDivisionError...")
    try:
        5 // 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    print("Testing KeyError...")
    try:
        plants = {"rose": 5, "tulip": 7}
        print(plants["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("Testing multiple errors together...")
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
