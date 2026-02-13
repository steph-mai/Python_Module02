# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 09:35:18 by stmaire         #+#    #+#               #
#  Updated: 2026/02/13 14:22:14 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:

    def __init__(self, name: str) -> None:
        self.name = name


class GardenError(Exception):
    pass


class PlantError(GardenError):
    "Exception raised for errors during plant operations."
    def __init__(
            self,
            message: str = (
                "Error adding plant: "
                "Plant name cannot be empty!\n"
            )
    ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    "Exception raised for water supply issues."
    def __init__(self, message: str = ("Not enough water in tank")) -> None:
        super().__init__(message)


class GardenManager:

    def __init__(self) -> None:
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden manager."""
        if plant.name is None or plant.name == "":
            raise PlantError()
        self.plants += [plant]
        print(f"Added {plant.name} successfully")

    def water_plants(self, tank: int) -> None:
        """Water all plants if there is enough water in the tank"""
        if tank < 5:
            raise WaterError()
        try:
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self, plant: Plant,
                           water_level: int,
                           sunlight_hours: int
                           ) -> None:
        """Check water and sunlight levels for plant health"""
        if water_level < 1:
            raise ValueError(f"Error checking {plant.name}:"
                             f" Water level {water_level}"
                             f" is too low (min 1)\n")
        if water_level > 10:
            raise ValueError(f"Error checking {plant.name}:"
                             f" Water level {water_level}"
                             f" is too high (max 10)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Error checking {plant.name}:"
                             f" {sunlight_hours} is too low (min 2)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Error checking {plant.name}:"
                             f" {sunlight_hours} is too high (max 12)\n")
        print(f"{plant.name}: healthy "
              f"(water: {water_level}, sun: {sunlight_hours})")


def test_garden_management() -> None:
    """Demonstrate the garden management system and its error handling"""
    manager = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    plants = ["tomato", "lettuce", ""]
    for plant in plants:
        try:
            new_plant = Plant(plant)
            manager.add_plant(new_plant)
        except PlantError as e:
            print(e)

    print("Watering plants...")
    try:
        manager.water_plants(50)
    except WaterError as e:
        print(e)

    print("Checking plant health...")
    try:
        manager.check_plant_health(manager.plants[0], 5, 8)
    except ValueError as e:
        print(e)

    try:
        manager.check_plant_health(manager.plants[1], 15, 8)
    except ValueError as e:
        print(e)

    print("Testing error recovery...")
    try:
        manager.water_plants(2)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
