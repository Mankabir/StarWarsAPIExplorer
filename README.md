# Star Wars Data Fetcher

## Overview
This Python project is designed to interact with the Star Wars API (SWAPI) to fetch starship data and save it into JSON files. Additionally, it interacts with a MongoDB database to retrieve and display information about Star Wars characters. If the MongoDB database does not have starship data, the script will import it from the saved JSON files.


## Code Explanation

### Part 1: Fetching and Saving Starship Data
- **Libraries**: The script uses `os`, `requests`, and `json` libraries.
- **get_starships(url)**: Fetches starship data from the given URL.
- **save_starship_data(starship)**: Saves a single starship's data into a JSON file.
- **fetch_all_starships()**: Continuously fetches starship data until no more pages are available.
- **main()**: Main method to start the fetching process.

### Part 2: Interacting with MongoDB and Importing Data
- **MongoDB Connection**: Uses `pymongo` to connect to a local MongoDB database.
- **import_starship_data(db)**: Imports starship data from JSON files into the MongoDB database if the database does not already contain this data.
- **Checking and Importing Data**: The script checks for the presence of starship data in the database and imports it if not found.
- **Retrieving Data**: Fetches and prints the `_id` and `name` of characters stored in the database.

## Conclusion
This project demonstrates Python scripting abilities, API interaction, data handling, and working with MongoDB. It showcases handling different aspects of data fetching, storage, retrieval, and database management in Python.

## Acknowledgments

- SWAPI for providing the Star Wars data.
