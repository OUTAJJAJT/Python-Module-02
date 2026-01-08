class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plants(plant_name):
    garden_plants = ["rose", "flower", "oak", "hicham"]
    if plant_name not in garden_plants:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water(amount):
    if amount <= 0:
        raise WaterError("Not enough water in the tank!")


def test_garden_error():
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        check_plants("tomato")
    except PlantError as error:
        print("Caught PlantError:", error)

    print("\nTesting WaterError...")
    try:
        check_water(0)
    except WaterError as error:
        print("Caught WaterError:", error)

    print("\nTesting catching all garden errors...")
    try:
        check_plants("tomato")
    except GardenError as error:
        print("Caught a garden error:", error)

    try:
        check_water(-5)
    except GardenError as error:
        print("Caught a garden error:", error)

    print("\nAll custom error types work correctly!")


test_garden_error()
