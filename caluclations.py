from getter import get_timezone,get_weather,get_location_info


transport_modes = {
    "Walking": 5,        # 5 km/h * Speed may decrease in non-normal weather conditions
    "Bicycle": 15,       # 15 km/h * Speed may decrease in non-normal weather conditions
    "Car": 80,           # 80 km/h * Speed may decrease in non-normal weather conditions
    "Train": 120,        # 120 km/h * Speed may decrease in non-normal weather conditions
    "Airplane": 900      # 900 km/h * Speed may decrease in non-normal weather conditions
}



def estimate_travel_time(distance_km, weather_description):
    """Estimate travel time for various modes of transport given the distance in km."""
    # Adjust speeds based on weather
    adjusted_speeds = adjust_speed_based_on_weather(weather_description)
    
    travel_times = {}
    for mode, speed in adjusted_speeds.items():
        if speed > 0:
            # Handle very small distances
            if distance_km < 0.5:
                travel_time = 0.01  # Assume less than 1 minute
            else:
                travel_time = distance_km / speed  # Time = Distance / Speed  
            
            travel_times[mode] = round(travel_time, 2)  # Round to 2 decimal places

    return travel_times


def adjust_speed_based_on_weather(weather_description):

    adjusted_speeds = {
        "Walking": 5,
        "Bicycle": 15,
        "Car": 80,
        "Train": 120,
        "Airplane": 900
    }
    # INCREASE THE CONDITIONS 
    if "rain" in weather_description.lower() or "storm" in weather_description.lower():
        for mode in adjusted_speeds:
            adjusted_speeds[mode] *= 0.8  # Reduce speed by 20% in bad weather
    elif "snow" in weather_description.lower():
        for mode in adjusted_speeds:
            adjusted_speeds[mode] *= 0.5  # Reduce speed by 50% in snow
    elif "fog" in weather_description.lower():
        for mode in adjusted_speeds:
            adjusted_speeds[mode] *= 0.7  # Reduce speed by 30% in fog
    elif "heat" in weather_description.lower():
        for mode in adjusted_speeds:
            adjusted_speeds[mode] *= 0.9  # Reduce speed by 10% in extreme heat

    return adjusted_speeds


def calculate_distance_and_info(coord1, coord2, unit="km"):
    """Calculate distance, fetch location, timezone, and weather information."""
    # Fetch location information for each coordinate
    info1 = get_location_info(coord1[0], coord1[1])
    info2 = get_location_info(coord2[0], coord2[1])

    # Fetch timezone and weather information
    timezone1, time1 = get_timezone(coord1[0], coord1[1])
    timezone2, time2 = get_timezone(coord2[0], coord2[1])
    weather1 = get_weather(coord1[0], coord1[1])
    weather2 = get_weather(coord2[0], coord2[1])

    print("\nInformation about Coordinates:")
    print(f"Coordinate 1: {coord1[0]}, {coord1[1]}")
    print(f"Location 1: {info1}")
    print(f"Timezone 1: {timezone1}, Current Time: {time1}")
    print(f"Weather 1: {weather1}\n")
    
    print(f"Coordinate 2: {coord2[0]}, {coord2[1]}")
    print(f"Location 2: {info2}")
    print(f"Timezone 2: {timezone2}, Current Time: {time2}")
    print(f"Weather 2: {weather2}\n")

    # Calculate the distance between the two coordinates
    distance = geodesic(coord1, coord2) # type: ignore
    if unit == "miles":
        distance = distance.miles
        print(f"The distance between the two coordinates is {distance:.2f} .")
    else:
        distance = distance.kilometers
        print(f"The distance between the two coordinates is {distance:.2f} .")

    return {
        "Coordinate 1": coord1,
        "Location 1": info1,
        "Timezone 1": timezone1,
        "Current Time 1": time1,
        "Weather 1": weather1,
        "Coordinate 2": coord2,
        "Location 2": info2,
        "Timezone 2": timezone2,
        "Current Time 2": time2,
        "Weather 2": weather2,
        "Distance": f"{distance:.2f} {unit}",
    }
