import pymongo
import os
import json

# Function to import starship data into MongoDB
def import_starship_data(db):
    starship_dir = 'starships/'
    for filename in os.listdir(starship_dir):
        if filename.endswith('.json'):
            with open(starship_dir + filename, 'r') as file:
                starship_data = json.load(file)
                db.starships.insert_one(starship_data)

# Create a MongoDB client
client = pymongo.MongoClient()
db = client['starwars']

# Check if the starships collection exists and has data
if 'starships' in db.list_collection_names() and db.starships.count_documents({}) > 0:
    print("Starship data already exists in the database.")
else:
    print("No starship data found in the database. Importing data...")
    import_starship_data(db)

# Use find() to get _id and name of characters
characters = db.characters.find({}, {"_id": 1, "name": 1})

# Print the _id and name for each character
for character in characters:
    print(character)
