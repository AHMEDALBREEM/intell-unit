from caluclations import calculate_distance_and_info
from output_format import save_results_to_file
from validation_input import validate_coordinate_input
# make it django as backend server api when you *finish* all the features 


transport_modes = {
    "Walking": 5,        # 5 km/h * Speed may decrease in non-normal weather conditions
    "Bicycle": 15,       # 15 km/h * Speed may decrease in non-normal weather conditions
    "Car": 80,           # 80 km/h * Speed may decrease in non-normal weather conditions
    "Train": 120,        # 120 km/h * Speed may decrease in non-normal weather conditions
    "Airplane": 900      # 900 km/h * Speed may decrease in non-normal weather conditions
}



if __name__ == "__main__":
    print("Coordinate Distance and Information Finder")
    print("Enter coordinates in the format: latitude,longitude")

    # Input and validate the first coordinate
    coord1 = None
    while coord1 is None:
        coord1_input = input("Enter the first coordinate: ")
        coord1 = validate_coordinate_input(coord1_input)

    # Input and validate the second coordinate
    coord2 = None
    while coord2 is None:
        coord2_input = input("Enter the second coordinate: ")
        coord2 = validate_coordinate_input(coord2_input)

    # Choose distance unit
    print("\nChoose the unit for distance calculation:")
    print("1. Kilometers (default)")
    print("2. Miles")
    unit_choice = input("Enter your choice (1 or 2): ").strip()
    unit = "miles" if unit_choice == "2" else "km"

    # Calculate distance and fetch information
    results = calculate_distance_and_info(coord1, coord2, unit)

    # Save results to a file
    save_option = input("\nWould you like to save the results to a file? (y/n): ").strip().lower()
    if save_option == "y":
        filename = input("Enter the filename (default: results.txt): ").strip()
        save_results_to_file(results, filename or "results.txt")
