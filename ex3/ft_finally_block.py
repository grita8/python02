def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None or not isinstance(plant, str) or not plant:
                print(f"Error: Cannot water {plant} - invalid plant!")
                success = False
                break
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")
    success = True
    if success:
        print("Watering completed successfully!")


def test_watering_system():
    print("=== Garden Watering System ===")
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
