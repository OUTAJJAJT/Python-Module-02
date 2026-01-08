class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class HealthError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        if plant_name == "":
            raise PlantError("Plant name cannot be empty!")

        self.plants.append(plant_name)
        print("Added", plant_name, "successfully")

    def water_plant(self, plant_name, water_level):
        try:
            if water_level <= 0:
                raise WaterError("Not enough water in tank")

            if water_level > 10:
                raise WaterError("Water level " + str(water_level) + " is too\
high")

        finally:
            print("Watering", plant_name, "- success")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        if water_level < 1 or water_level > 10:
            raise HealthError(
                "Water level " + str(water_level) + " is too high (max 10)")

        print(
            plant_name + ": healthy (water: "
            + str(water_level)
            + ", sun: "
            + str(sunlight_hours)
            + ")"
        )


def test_garden_manager():
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato")
        garden.add_plant("lettuce")
        garden.add_plant("")
    except PlantError as e:
        print("Error adding plant:", e)

    print("\nWatering plants...")
    print("Opening watering system")
    try:
        garden.water_plant("tomato", 5)
        garden.water_plant("lettuce", 5)
    except WaterError as e:
        print(e)
    print("Closing watering system (cleanup)")

    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
        garden.check_plant_health("lettuce", 15, 8)
    except HealthError as e:
        print("Error checking lettuce:", e)

    print("\nTesting error recovery...")
    try:
        garden.water_plant("tomato", 0)
    except GardenError as e:
        print("Caught GardenError:", e)

    print("System recovered and continuing...")
    print("\nGarden management system test complete!")


test_garden_manager()
