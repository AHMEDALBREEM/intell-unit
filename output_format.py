
from caluclations import estimate_travel_time
from ai_feedback import feedback_analysis_ai_function


def save_results_to_file(results, filename="results.txt"):
    """Save the results to a file."""
    try:
        estimate_travel_times = estimate_travel_time(float(results["Distance"].split()[0]), results["Weather 2"])
        feedback_analysis_ai = feedback_analysis_ai_function(float(results["Distance"].split()[0]), results["Weather 2"])

        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Coordinate Distance and Information Finder "+"\n\n") # type: ignore
            file.write("-" * 50 + "\n")
            file.write("Coordinates 1 information \n")
            file.write(f"Location 1: {results.get('Location 1', 'N/A')}\n")
            file.write(f"Coordinates: {results.get('Coordinate 1', 'N/A')}\n")
            file.write(f"Timezone: {results.get('Timezone 1', 'N/A')}\n")
            file.write(f"Weather: {results.get('Weather 1', 'N/A')}\n")
            file.write("-" * 50 + "\n")
            file.write("Coordinates 2 information \n")
            file.write(f"Location 2: {results.get('Location 2', 'N/A')}\n")
            file.write(f"Coordinates: {results.get('Coordinate 2', 'N/A')}\n")
            file.write(f"Timezone: {results.get('Timezone 2', 'N/A')}\n")
            file.write(f"Weather: {results.get('Weather 2', 'N/A')}\n")
            file.write("-" * 50 + "\n")
            file.write("Geocoding information Over The Coordinates 2  \n")    
            file.write(f"Distance: {results.get('Distance', 'N/A')}\n")
            file.write(f"Estimated travel times:\n")
            for mode, time in estimate_travel_times.items():
                file.write(f"{mode} ({results.get('Distance', 'N/A')}/{time}): {time} hours\n")
            file.write("-" * 50 + "\n")
            file.write(f"Enginering process by linkdin. eng. : @ahmedalbreem\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results to file: {e}")