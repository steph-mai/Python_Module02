def garden_operations(operation: str, value=None):
    """Realize a problematic operation"""

    if (operation == "convert type"):
        return int(value)
    if (operation == "divise"):
        return 42 / value
    if (operation == "open file"):
        f = open(value, "r")
        content = f.read()
        f.close()
        return content
    if (operation == "get info"):
        plants = {"rose": "pink", "sunflower": "yellow"}
        return plants[value]


def test_error_types() -> None:
    """Show each type of error hapening"""

    print("=== Garden Error Types Demo ===")
    print()

    print("Testing ValueError...")
    try:
        garden_operations("convert type", "abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("divise", 0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    print("Testing FileNotFoundError...")
    try:
        filename = "missing.txt"
        garden_operations("open file", filename)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{filename}'\n")

    print("Testing KeyError...")
    try:
        garden_operations("get info", "peony")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("divise", 0)
    except (Exception):
        print("Caught an error, but program continues\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
