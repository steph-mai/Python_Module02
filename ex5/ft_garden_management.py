# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: stmaire <stmaire@student.42.fr>           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/13 09:35:18 by stmaire         #+#    #+#               #
#  Updated: 2026/02/13 12:24:35 by stmaire         ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:

    def __init__(self, name):
        self.name = name

class GardenError(Exception):
    pass

class PlantError(GardenError):
    def __init__(self, message =("Error adding plant: Plant name cannot be empty!\n")):
        super().__init__(message)     

class WaterError(GardenError):
    def __init__(self, message =("Not enough water in tank")):
        super().__init__(message)
    
class GardenManager:
    
    def __init__(self) -> None:
        self.plants = []
        
    def add_plant(self, plant: Plant) -> None:
        if plant.name == None or plant.name == "":
            raise PlantError() 
        self.plants += [plant]
        print(f"Added {plant.name} successfully")

    def water_plants(self, tank: int) -> None:
        if tank < 5:
                raise WaterError()
        try: 
            print("Opening watering system")
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)\n")
            
  
    def check_plant_health(self, plant: Plant, water_level: int, sunlight_hours: int) -> None:
        if water_level < 1:
            raise ValueError(f"Error checking {plant.name}: Water level {water_level} is too low (min 1)\n")
        if water_level > 10:
            raise ValueError(f"Error checking {plant.name}: Water level {water_level} is too high (max 10)\n")
        if sunlight_hours < 2:
            raise ValueError(f"Error checking {plant.name}:"
                             f" {sunlight_hours} is too low (min 2)\n")
        if sunlight_hours > 12:
            raise ValueError(f"Error checking {plant.name}:"
                             f" {sunlight_hours} is too high (max 12)\n")
        print(f"{plant.name}: healthy (water: {water_level}, sun: {sunlight_hours})")
 
  
def test_garden_management() -> None:
        
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
        
    
    
    