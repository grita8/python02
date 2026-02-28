class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, plant_name):
        try:
            if (
                not plant_name
                or not isinstance(plant_name, str)
                or not plant_name.strip()
            ):
                raise PlantError("Plant name cannot be empty!")
            self.plants[plant_name] = {
                "water": 5,
                "sun": 8
            }
            print(f"Added {plant_name} successfully")
        except PlantError as pe:
            print(f"Error adding plant: {pe}")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in self.plants:
                if self.plants[plant]["water"] <= 0:
                    raise WaterError("Not enough water in tank")
                print(f"Watering {plant} - success")
            watering_successful = True
        except WaterError:
            watering_successful = False
            raise
        finally:
            print("Closing watering system (cleanup)")
        return watering_successful

    def check_plant_health(self, plant_name):
        try:
            if plant_name not in self.plants:
                raise PlantError("Unknown plant!")
            water = self.plants[plant_name]["water"]
            sun = self.plants[plant_name]["sun"]
            if water < 1:
                raise ValueError(f"Water level {water} is too low (min 1)")
            if water > 10:
                raise ValueError(f"Water level {water} is too high (max 10)")
            if sun < 2:
                raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
            if sun > 12:
                raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
            print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except ValueError as ve:
            print(f"Error checking {plant_name}: {ve}")
        except PlantError as pe:
            print(f"Error checking {plant_name}: {pe}")


def test_garden_management():
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    manager.add_plant("tomato")
    manager.add_plant("lettuce")
    manager.add_plant("")

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as we:
        print(f"Caught GardenError: {we}")

    manager.plants["lettuce"]["water"] = 15

    print("Checking plant health...")
    manager.check_plant_health("tomato")
    manager.check_plant_health("lettuce")

    print("Testing error recovery...")
    manager.plants["lettuce"]["water"] = 0
    try:
        manager.water_plants()
    except GardenError as we:
        print(f"Caught GardenError: {we}")
        print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
