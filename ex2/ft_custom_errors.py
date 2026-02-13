class GardenError(Exception):
    pass


class PlantError(GardenError):
    def __init__(self, plant: str = "Unknown") -> None:
        self.message = (f"The {plant} plant is wilting!")
        super().__init__(self.message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def water_plants(tank: int) -> None:
    """Handle watering"""

    if tank < 5:
        raise WaterError()
    print("Watering plants")


def valid_plants_checker(plant: str, color: str) -> None:
    """Check plants health"""

    if color == "yellow":
        raise PlantError()
    print(f"The {plant} plant is healthy")


def test_custom_errors() -> None:
    """Test the garden errors"""

    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        valid_plants_checker("tomato", "yellow")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        water_plants(2)
    except WaterError as e:

        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        valid_plants_checker("tomato", "yellow")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        water_plants(4)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
