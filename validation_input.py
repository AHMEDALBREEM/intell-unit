def validate_coordinate_input(input_str):
    """Validate that input is in the format 'latitude,longitude' and within valid ranges."""
    try:
        lat, lon = map(float, input_str.split(","))
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return (lat, lon)
        else:
            print("Latitude must be between -90 and 90, and longitude between -180 and 180.")
    except ValueError:
        print("Invalid format. Please enter coordinates as 'latitude,longitude'.")
    return None