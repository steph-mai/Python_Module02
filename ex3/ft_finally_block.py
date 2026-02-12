class GardenError(Exception):
    pass


class PlantListError(GardenError):
    def __init__(
            self,
            message=("Error: Cannot water None - invalid plant!")
    ):
        super().__init__(message)


def water_plants(plant_list: list) -> None:
    print("Opening watering system")
    try:
        if not plant_list:
            raise PlantListError()
        for p in plant_list:
            if p is None:
                raise PlantListError()
            print(f"Watering {p}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    try:
        plant_list = [
            "tomato",
            "lettuce",
            "carrots",
        ]
        water_plants(plant_list)
        print("Watering completed successfully!\n")
    except PlantListError as e:
        print(e)
    finally:
        print("")

    print("Testing with error...")
    try:
        plant_list = [
            "tomato",
            None,
            "lettuce",
            "carrots",
        ]
        water_plants(plant_list)
    except PlantListError as e:
        print(e)
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
