
#flake8 mypy


def check_temperature(temp_str: str) -> int | None:
    """check temperature validity."""

    print(f"Testing temperature: {temp_str}")
    try:
        temp: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        print()
        return None

    try:
        if temp < 0:
            raise ValueError(f"Error: {temp_str}\u00b0C is too cold for plants (min 0\u00b0C)")
        if temp > 40:
            raise ValueError(f"Error: {temp_str}\u00b0C is too hot for plants (max 40\u00b0C)")
        print(f"Temperature {temp_str}\u00b0C is perfect for plants!")
        print()
        return temp
    except ValueError as e:
        print(e)
        print()
        return None

def main() -> None:
    """Run temperature tests."""

    print("=== Garden Temperature Checker ===")
    print()
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()