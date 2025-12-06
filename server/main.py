# Tutorial Code vv ////////////////////////
# (Imports) Main Python Backend File 
from flask import Flask, jsonify, request
from flask_cors import CORS

# (Imports) user data collection
import csv
from pathlib import Path

# (App setup) create app instance
app = Flask(__name__)
CORS = CORS(app, origins='*') # set to accept all origins

# End of Tutorial Code ^^ ////////////////////////

# Local Variables -----------------------------------------

# paths for csv data collection
data_folder = Path("collected_data")
data_folder.mkdir(exist_ok = True) # make collected_data folder 

user_demographics = Path(data_folder / "user_demographics.csv") # stores user demographic data
global_matchups = Path(data_folder / "species_matchup_data.csv") # stores global matchup data
global_species_scores = Path(data_folder / "species_individual_scores.csv") # stores pickrate for each species


user_demographics_headers = ["UserIndex", "Age", "Gender", "Location", "Familiar with ICUN Red List", "Endangered Species They Can Name"]
species_matchups = ["UserIndex", "SpeciesA", "SpeciesB", "Winner", "TimeTaken"]
species_scores = ["Species", "TotalMatchups", "Wins", "Losses"]

# (Edited Tutorial Code) Defines users route, permites GET and POST methods
@app.route("/api/users", methods=['GET', 'POST'])

# Main FUNCTIONS ////////////////////////////////////////

# saving data 
def save_user_demographics(row): # where row is a list
    with open(user_demographics, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_species_matchups(row):
    with open(species_matchups, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)

def save_species_scores(row):
    with open(species_scores, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)


# fetch data from backend - work in prog
def grab_species_from_csv(index): # picks a random species from the query csv
    # Set species file
    species_file = Path("query.csv")
    with open(species_file,'rt', encoding='utf-8') as infile:
        headers, *data = csv.reader(infile)
    return jsonify(data[index])

# print(grab_species_from_csv(1)) find beter way to call this

# Tutorial Code vv ////////////////////////

# run app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

# use this url to access backend server
# http://localhost:8080/api/users

# End of Tutorial Code ////////////////////////