def check_plant_health(plant_name, water_level, sunlight_hours):
    if plant_name == "":
        print("\nTesting empty plant name...")
        raise ValueError(
            "Error: Plant name is empty"
            )

    if water_level < 1 or water_level > 10:
        print("\nTesting bad water level...")
        raise ValueError(
            "Error: Water level " + str(water_level) + " is too high (max 10)"
            )

    if sunlight_hours < 2 or sunlight_hours > 12:
        print("\nTesting bad sunlight hours...")
        raise ValueError(
            "Error: Sunlight hours " + str(sunlight_hours) + " is too low (min\
 2)"
            )

    return "Testing good values...\nPlant " + plant_name + " is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===\n")
    Tests = [
        ("rose", 5, 6),
        ("", 15, 20),
        ("oak", 20, 8),
        ("tomato", 5, 1)
    ]
    for plant, water, sun in Tests:
        try:
            result = check_plant_health(plant, water, sun)
            print(result)
        except ValueError as e:
            print(e)
    print("\nAll error raising tests completed!")


test_plant_checks()
