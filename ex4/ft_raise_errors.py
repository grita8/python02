def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name or not isinstance(plant_name, str):
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError
        (f"Sunlight hours {sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name.lower()}' is healthy!"


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")
    print("Testing good values...")
    try:
        msg = check_plant_health("tomato", 5, 6)
        print(msg)
    except ValueError as e:
        print("Error:", e)

    print("Testing empty plant name...")
    try:
        msg = check_plant_health("", 5, 6)
        print("Error:", msg)
    except ValueError as e:
        print("Error:", e)

    print("Testing bad water level...")
    try:
        msg = check_plant_health("tomato", 15, 6)
        print("Error:", msg)
    except ValueError as e:
        print("Error:", e)

    print("Testing bad sunlight hours...")
    try:
        msg = check_plant_health("tomato", 5, 0)
        print("Error:", msg)
    except ValueError as e:
        print("Error:", e)

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
