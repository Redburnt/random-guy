# Random Location Generator

This Python script generates random latitude and longitude coordinates within a specified bounding box and saves them to CSV and JSON files.

## What it Does

* Generates random latitude and longitude coordinates using Python's `random` library.
* Allows you to define a bounding box (minimum and maximum latitude and longitude) to limit the generated locations.
* Saves the generated locations to both `random_locations.csv` and `random_locations.json` files.

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone [your-repository-url]
    ```
2.  **Run the Script:**
    ```bash
    python random_locations.py
    ```
3.  **View the Results:**
    * The generated locations will be saved in `random_locations.csv` and `random_locations.json` in the project directory.

## Customization

* **Bounding Box:** Modify the `min_lat`, `max_lat`, `min_lon`, and `max_lon` variables in the `random_locations.py` file to change the area where locations are generated.
* **Number of locations:** Modify the `num_locations` variable in the `random_locations.py` file to change the amount of locations that are generated.

## Libraries Used

* `random` (Python standard library)
* `csv` (Python standard library)
* `json` (Python standard library)

## Author

Girls Rajuno David Uchenna Ekoh/Redburnt

## License

MIT
