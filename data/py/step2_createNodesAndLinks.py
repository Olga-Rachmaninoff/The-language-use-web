'''
Create nodes and links for the network visualization based on the informants/interlocutors and languages used in the interviews.
Input: JSON file with all the data from the interviews
Output: JSON file with nodes and links for the network visualization
'''

import json
import csv

jsonFilePath = '../data/json/all_informants_interlocutors.json'
networkFilePath = '../data/json/nodes_links.json'

interlocutors = []
places = []
situations = []
media = []


######################################################################################################################

# Save the informants/interlocutors in specific lists for determining the type of the nodes later.
with open('../data/csv/raw_data/interlocutors.csv', encoding='utf-8-sig') as csvf:
    csvReader = csv.reader(csvf, delimiter=';')
    for row in csvReader:
        if row[0] != 'interlocutor':
            interlocutors.append(row[0])

with open('../data/csv/raw_data/media.csv', encoding='utf-8-sig') as csvf:
    csvReader = csv.reader(csvf, delimiter=';')
    for row in csvReader:
        if row[0] != 'informant':
            media.append(row[0])

with open('../data/csv/raw_data/places.csv', encoding='utf-8-sig') as csvf:
    csvReader = csv.reader(csvf, delimiter=';')
    for row in csvReader:
        if row[0] != 'informant':
            places.append(row[0])

with open('../data/csv/raw_data/situations.csv', encoding='utf-8-sig') as csvf:
    csvReader = csv.reader(csvf, delimiter=';')
    for row in csvReader:
        if row[0] != 'informant':
            situations.append(row[0])


######################################################################################################################

# Read the json file.
with open(jsonFilePath, 'r', encoding='utf-8') as jsonf:
    data = json.load(jsonf)
    unique_nodes = set()
    nodes = []
    links = []
    network_data = {'nodes': nodes, 'links': links}

    # Create a list of unique nodes and links.
    for key, value in data.items():
        # Add the key to the unique nodes set, e.g. partner, at the bank, instagram.
        unique_nodes.add(key)
        for k, val in value.items():
            # Add the languages to the unique nodes set, e.g. Turkish, German, Kurmanji.
            # If the value is a list of languages, split the languages and add them to the unique nodes set.
            if ',' in val:
                langList_strip = val.replace(' ', '')
                langList = langList_strip.split(',')
                for lang in langList:
                    if lang not in unique_nodes:
                        unique_nodes.add(lang)
            else:
                if val not in unique_nodes:
                    unique_nodes.add(val.replace(' ', ''))

            # Add the links to the links list except for the first key.
            first_key = list(value.keys())[0]
            if k != first_key:
                # If the value is a list of languages, split the languages and add them to the links list.
                if ',' in val:
                    lang = val.replace(' ', '').split(',')
                    for l in lang:
                        links.append({
                            'interview': k, # number of interviewee
                            'source': value[first_key], # interlocutor/informant, e.g. partner, at the bank, instagram
                            'target': l # language
                        })
                else:
                    links.append({
                        'interview': k, # number of interviewee
                        'source': value[first_key], # interlocutor/informant, e.g. partner, at the bank, instagram
                        'target': val.replace(' ', '') # language
                    })

    # Create a list of nodes.
    for node in unique_nodes:
        nodes.append({'id': node})

# Write the network data to a json file.
with open(networkFilePath, 'w', encoding='utf-8') as networkf:
    json.dump(network_data, networkf, ensure_ascii=False, indent=4)


######################################################################################################################

# Read the network data from the json file.
with open(networkFilePath, 'r', encoding='utf-8') as networkf:
    data = json.load(networkf)

for node in data['nodes']:
    if node['id'] in interlocutors:
        node.update({"type": "interlocutor"})
        node.update({"color": "#ffc107"})
    elif node['id'] in media:
        node.update({"type": "media"})
        node.update({"color": "#6a040f"})
    elif node['id'] in places:
        node.update({"type": "place"})
        node.update({"color": "#118ab2"})
    elif node['id'] in situations:
        node.update({"type": "situation"})
        node.update({"color": "#dc3545"})
    else:
        node.update({"type": "language"})
        node.update({"color": "#fd7e14"})

# Write the updated network data back to the json file.
with open(networkFilePath, 'w', encoding='utf-8') as networkf:
    json.dump(data, networkf, ensure_ascii=False, indent=4)
