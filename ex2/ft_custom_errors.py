class PlantError(Exception):
    pass


class WaterError(Exception):
    pass


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as y:
        print("Caught PlantError:", y)

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as a:
        print("Caught WaterError:", a)

    print("Testing catching all garden errors...")
    garden_errors = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")]
    for error in garden_errors:
        try:
            raise error
        except (PlantError, WaterError) as g:
            print("Caught a garden error:", g)

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
