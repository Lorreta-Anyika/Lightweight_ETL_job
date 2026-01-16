import requests
import json
import os

url = "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json"

#def save_json_from_url(url, filename):
           
response = requests.get(url)

python_dict = response.json()

with open("raw_data_json", "w") as f:
  json.dump(python_dict, f, indent=2)


champions = python_dict["data"]

#for champion_name, champion_info in champions.items():
  # print(champion_name, champion_info)

filtered = []

champions = python_dict["data"]

for champion_name, champion_info in champions.items():
    attack = champion_info["info"]["attack"]
    defense = champion_info["info"]["defense"]

    if attack > 5 and defense > 5:
        filtered.append({
            "name": champion_info["name"],
            "title": champion_info["title"],
            "attack": attack,
            "defense": defense
        })
        
with open("filtered_data_json", "w") as f:
  json.dump(filtered, f, indent=2)