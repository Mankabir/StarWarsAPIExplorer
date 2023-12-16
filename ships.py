# Importing necessary libraries
import os
import requests
import json

# Function to fetch starships data from the specified URL
def get_starships(url):
    # Send GET request to the URL
    response = requests.get(url)
    # Convert the response to JSON
    data = response.json()
    # Return the results and the next page URL
    return data['results'], data['next']

# Function to save starship data into a JSON file
def save_starship_data(starship):
    # Get starship name
    starship_name = starship['name']
    # Define filename using starship name (replacing spaces with underscores)
    filename = f'starships/{starship_name.replace(" ", "_")}.json'
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # Open the file in write mode and dump the starship data into it
    with open(filename, 'w') as file:
        json.dump(starship, file, indent=4)

# Function to fetch all starships data
def fetch_all_starships():
    # Base URL for starships API
    url = 'https://swapi.dev/api/starships/'
    # Continue fetching as long as there is a next page URL
    while url:
        # Fetch starships data
        starships, url = get_starships(url)
        # Save each starship's data
        for starship in starships:
            save_starship_data(starship)

# Main function to kick-off the process
def main():
    fetch_all_starships()

# Run the main function when the script is run
if __name__ == '__main__':
    main()
