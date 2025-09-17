'''
Convert CSV files to a single JSON file.
Input: Individual CSV files media, places, situations, interlocutors
Output: JSON file with all the data
'''

import csv
import json

csv_media = '../data/csv/media.csv'
csv_places = '../data/csv/places.csv'
csv_situations = '../data/csv/situations.csv'
csv_interlocutors = '../data/csv/interlocutors.csv'

json_all_data = '../data/json/all_informants_interlocutors.json'

data = {}

with open(csv_media, encoding='utf-8-sig') as csvf:
    csvReader = csv.DictReader(csvf, delimiter=';')
    for rows in csvReader:
        key = rows['informant']
        data[key] = rows

with open(csv_places, encoding='utf-8-sig') as csvf:
    csvReader = csv.DictReader(csvf, delimiter=';')
    for rows in csvReader:
        key = rows['informant']
        data[key] = rows
        data[key].update(rows)

with open(csv_situations, encoding='utf-8-sig') as csvf:
    csvReader = csv.DictReader(csvf, delimiter=';')
    for rows in csvReader:
        key = rows['informant']
        data[key] = rows
        data[key].update(rows)

with open(csv_interlocutors, encoding='utf-8-sig') as csvf:
    csvReader = csv.DictReader(csvf, delimiter=';')
    for rows in csvReader:
        key = rows['interlocutor']
        data[key] = rows
        data[key].update(rows)

with open(json_all_data, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, ensure_ascii=False, indent=4))