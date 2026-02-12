def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name is None:
        raise ValueError ("Error: Plant name cannot be empty!\n")
    if water_level < 1:
        raise ValueError (f"Error: Water level {water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError (f"Error: Water level {water_level} is too high (max 10)\n")
    if sunlight_hours < 2:
        raise ValueError (f"Error: Sunlight hours {sunlight_hours} is too low (min 2)\n")
    if sunlight_hours > 12:
        raise ValueError (f"Error: Sunlight hours {sunlight_hours} is too high (max 12)\n")
    print (f"Plant {plant_name} is healthy!\n")


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 2, 8)
    except ValueError as e:
        print(e)
 
    print("Testing empty plant name...")
    try:
        check_plant_health(None, 2, 8)
    except ValueError as e:
        print(e)

    print("Testing bad water level...")
    try:
        check_plant_health("tomato", 12, 8)
    except ValueError as e:
        print(e)
    
    print("Testing bad sunlight hours...")
    try:
        check_plant_health("tomato", 2, 20)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    test_plant_checks()