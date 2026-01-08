def water_plants(plant_list):
    print("Opening watering system")
    valid_plants = ["rose", "tomato", "oak", "bssla stin"]

    try:
        for plant in plant_list:
            if plant not in valid_plants:
                print("Error: Cannot water None - invalid plant!")
            else:
                print("Watering", plant)
    except ValueError:
        print("Some unexpected error occurred while watering!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    good_plants = ["rose", "tomato", "oak"]
    water_plants(good_plants)
    print("Watering completed successfully!")

    print("\nTesting with error...")
    bad_plants = ["tomato", "invalid_plant", "rose"]
    water_plants(bad_plants)

    print("\nAll watering completed. Cleanup always happens!")


test_watering_system()
