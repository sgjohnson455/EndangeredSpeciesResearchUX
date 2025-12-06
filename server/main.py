# (Imports) Main Python Backend File ----------------------
from flask import Flask, jsonify, request
from flask_cors import CORS

# (Imports) user data collection
import csv
from pathlib import Path

# (App setup) create app instance
app = Flask(__name__)
CORS = CORS(app, origins='*') # set to accept all origins

# Local Variables -----------------------------------------

# paths for csv data collection
data_folder = Path("collected_data")
data_folder.mkdir(exist_ok = True) # make collected_data folder 

user_demographics = Path(data_folder / "user_demographics.csv") # stores user demographic data
global_matchups = Path(data_folder / "species_matchup_data.csv") # stores global matchup data
species_scores = Path(data_folder / "species_individual_scores.csv") # stores pickrate for each species


user_demographics_headers = ["UserIndex", "Age", "Gender", "Location", "Familiar with ICUN Red List", "Endangered Species They Can Name"]
global_matchups = ["UserIndex", "SpeciesA", "SpeciesB", "Winner", "TimeTaken"]
species_scores = ["Species", "TotalMatchups", "Wins", "Losses"]

users_list = ["arpan", "zack", "jessie"]


# defines users route, permites GET and POST methods
@app.route("/api/users", methods=['GET', 'POST'])

# Returns a list of users; jsonify returns that list in json format
def users():
    if request.method == "POST":
        data = request.get_json()
        new_user = data.get("user")

        if not new_user:
            return jsonify({"error": "Missing 'user' field"}), 400

        users_list.append(new_user)
        return jsonify({"message": "User added", "users": users_list}), 201

    # GET request
    return jsonify({"users": users_list})

# run app
if __name__ == "__main__":
    app.run(debug=True, port=8080)

# use this url to access backend server
# http://localhost:8080/api/users