import csv
import json
import random

def generate_random_location(min_lat, max_lat, min_lon, max_lon):
    """Generates a random latitude and longitude within a bounding box."""
    latitude = random.uniform(min_lat, max_lat)
    longitude = random.uniform(min_lon, max_lon)
    return latitude, longitude

def main():

    min_lat = 30.0
    max_lat = 40.0
    min_lon = -100.0
    max_lon = -90.0

    # Generate and save 10 random locations
    num_locations = 10
    locations = []

    for _ in range(num_locations):
        lat, lon = generate_random_location(min_lat, max_lat, min_lon, max_lon)
        locations.append({"latitude": lat, "longitude": lon})

    # Save to CSV
    save_to_csv(locations, "random_locations.csv")

    # Save to JSON
    save_to_json(locations, "random_locations.json")

def save_to_csv(locations, filename):
    """Saves locations to a CSV file."""
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["latitude", "longitude"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for location in locations:
            writer.writerow(location)

def save_to_json(locations, filename):
    """Saves locations to a JSON file."""
    with open(filename, "w") as jsonfile:
        json.dump(locations, jsonfile, indent=4)

if __name__ == "__main__":
    main()