'''
Create Sankey diagrams for interlocutors, places, situations, and media from CSV data and save them in an HTML file.
Input: CSV files with data on interlocutors, places, situations, and media
Output: HTML file with Sankey diagrams
'''

import csv
from collections import Counter
import plotly.graph_objects as go


interlocutors = []
places = []
situations = []
media = []

languages_colors_links = {
    "No language given": "rgba(0, 104, 201, 0.8)",
    "Dutch": "rgba(158, 115, 45, 0.8)",
    "Turkish": "rgba(13, 59, 102, 0.8)",
    "French": "rgba(238, 150, 75, 0.8)",
    "German": "rgba(185, 117, 39, 0.8)",
    "Şexbizinî": "rgba(249, 87, 56, 0.8)",
    "Other language": "rgba(229, 183, 16, 0.8)",
    "Kurmanji": "rgba(102, 17, 0, 0.8)",
}

#####################################################################################################
# Interlocutors

# Read the CSV file and extract language data
with open("../data/csv/interlocutors.csv", encoding="utf-8-sig") as file_obj:
    reader_obj = csv.reader(file_obj, delimiter=";")

    for row in reader_obj:
        cleaned_row = []
        for r in row:
            if "," in r:
                for lang in r.split(","):
                    lang = lang.strip()
                    cleaned_row.append(lang)
            else:
                cleaned_row.append(r.strip())
        interlocutors.append(cleaned_row)

counters_interlocutor = []

# Count occurrences of each language per interlocutor
for interlocutor in interlocutors:
    ctr = Counter(interlocutor)
    counters_interlocutor.append(ctr)

# Create dictionary
interlocutor_data = {"source": [], "target": [], "value": []}

# Counter data
for idx, counter in enumerate(
    counters_interlocutor[1:], start=1
):  # Ignore the first counter
    # The interlocutor is the key with value 1
    target = [key for key, value in counter.items() if value == 1][0]

    # Iterate over all languages (source) and their values
    for source, value in counter.items():
        if source != target:  # Ignore the interlocutor itself as source
            interlocutor_data["source"].append(source)
            interlocutor_data["target"].append(target)
            interlocutor_data["value"].append(value)


# Create unique labels
unique_labels_interlocutor = list(
    set(interlocutor_data["source"] + interlocutor_data["target"])
)

# Convert labels to numerical indices
label_to_index_interlocutor = {}

for i, label in enumerate(unique_labels_interlocutor):
    label_to_index_interlocutor[label] = i

# Generate numerical indices for 'source' and 'target'
source_indices_interlocutor = [
    label_to_index_interlocutor[src] for src in interlocutor_data["source"]
]
target_indices_interlocutor = [
    label_to_index_interlocutor[tgt] for tgt in interlocutor_data["target"]
]

languages_colors_interlocutors_nodes = {
    "No language given": "rgba(0, 104, 201, 1.0)",
    "Dutch": "rgba(158, 115, 45, 1.0)",
    "Turkish": "rgba(13, 59, 102, 1.0)",
    "French": "rgba(238, 150, 75, 1.0)",
    "German": "rgba(185, 117, 39, 1.0)",
    "Şexbizinî": "rgba(249, 87, 56, 1.0)",
    "Other language": "rgba(229, 183, 16, 1.0)",
    "Kurmanji": "rgba(102, 17, 0, 1.0)",
    "friends": "rgba(216, 198, 151, 1.0)",
    "relatives": "rgba(216, 198, 151, 1.0)",
    "siblings": "rgba(216, 198, 151, 1.0)",
    "neighbours": "rgba(216, 198, 151, 1.0)",
    "father": "rgba(216, 198, 151, 1.0)",
    "mother": "rgba(216, 198, 151, 1.0)",
    "partner": "rgba(216, 198, 151, 1.0)",
    "children": "rgba(216, 198, 151, 1.0)",
}

# Create the Sankey diagram for interlocutors
fig1 = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=25,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=unique_labels_interlocutor,
                color=[
                    languages_colors_interlocutors_nodes[label]
                    for label in unique_labels_interlocutor
                ],
            ),
            link=dict(
                source=source_indices_interlocutor,  # Indices correspond to labels
                target=target_indices_interlocutor,
                value=interlocutor_data["value"],
                color=[
                    languages_colors_links[label]
                    for label in interlocutor_data["source"]
                ],
            ),
        )
    ]
)

fig1.update_layout(title_text="Interlocutors", font_size=15, width=1250, height=1000)
fig1_html = fig1.to_html(full_html=False, include_plotlyjs=False)


#####################################################################################################
# Places

# Read the CSV file and extract language data
with open("../data/csv/places.csv", encoding="utf-8-sig") as file_obj:
    reader_obj = csv.reader(file_obj, delimiter=";")

    for row in reader_obj:
        cleaned_row = []
        for r in row:
            if "," in r:
                for lang in r.split(","):
                    lang = lang.strip()
                    cleaned_row.append(lang)
            else:
                cleaned_row.append(r.strip())
        places.append(cleaned_row)

counters_place = []

# Count occurrences of each language per place
for place in places:
    ctr = Counter(place)
    counters_place.append(ctr)

# Create dictionary
place_data = {"source": [], "target": [], "value": []}

# Counter data
for idx, counter in enumerate(counters_place[1:], start=1):  # Ignore the first counter
    # The interlocutor is the key with value 1
    target = [key for key, value in counter.items() if value == 1][0]

    # Iterate over all languages (source) and their values
    for source, value in counter.items():
        if source != target:  # Ignore the interlocutor itself as source
            place_data["source"].append(source)
            place_data["target"].append(target)
            place_data["value"].append(value)

# Create unique labels
unique_labels_place = list(set(place_data["source"] + place_data["target"]))

# Convert labels to numerical indices
label_to_index_place = {label: i for i, label in enumerate(unique_labels_place)}

# Generate numerical indices for 'source' and 'target'
source_indices_place = [label_to_index_place[src] for src in place_data["source"]]
target_indices_place = [label_to_index_place[tgt] for tgt in place_data["target"]]

languages_colors_place_nodes = {
    "No language given": "rgba(0, 104, 201, 1.0)",
    "Dutch": "rgba(158, 115, 45, 1.0)",
    "Turkish": "rgba(13, 59, 102, 1.0)",
    "French": "rgba(238, 150, 75, 1.0)",
    "German": "rgba(185, 117, 39, 1.0)",
    "Şexbizinî": "rgba(249, 87, 56, 1.0)",
    "Other language": "rgba(229, 183, 16, 1.0)",
    "Kurmanji": "rgba(102, 17, 0, 1.0)",
    "at the police": "rgba(216, 198, 151, 1.0)",
    "with teachers at school": "rgba(216, 198, 151, 1.0)",
    "at the bank": "rgba(216, 198, 151, 1.0)",
    "at the restaurant": "rgba(216, 198, 151, 1.0)",
    "at the doctor": "rgba(216, 198, 151, 1.0)",
    "at court": "rgba(216, 198, 151, 1.0)",
    "when shopping": "rgba(216, 198, 151, 1.0)",
    "when asking for directions": "rgba(216, 198, 151, 1.0)",
    "with customers": "rgba(216, 198, 151, 1.0)",
    "at religious ceremonies": "rgba(216, 198, 151, 1.0)",
    "at funerals": "rgba(216, 198, 151, 1.0)",
    "at weddings": "rgba(216, 198, 151, 1.0)",
}

# Create the Sankey diagram for places
fig2 = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=25,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=unique_labels_place,
                color=[
                    languages_colors_place_nodes[label] for label in unique_labels_place
                ],
            ),
            link=dict(
                source=source_indices_place,  # Indices correspond to labels
                target=target_indices_place,
                value=place_data["value"],
                color=[
                    languages_colors_links[label]
                    for label in place_data["source"]
                ],
            ),
        )
    ]
)

fig2.update_layout(title_text="Places", font_size=15, width=1250, height=1000)
fig2_html = fig2.to_html(full_html=False, include_plotlyjs=False)


#####################################################################################################
# Situations

# Read the CSV file and extract language data
with open("../data/csv/situations.csv", encoding="utf-8-sig") as file_obj:
    reader_obj = csv.reader(file_obj, delimiter=";")

    for row in reader_obj:
        cleaned_row = []
        for r in row:
            if "," in r:
                for lang in r.split(","):
                    lang = lang.strip()
                    cleaned_row.append(lang)
            else:
                cleaned_row.append(r.strip())
        situations.append(cleaned_row)

counters_situation = []

# Count occurrences of each language per situation
for situation in situations:
    ctr = Counter(situation)
    counters_situation.append(ctr)

# Create dictionary
situation_data = {"source": [], "target": [], "value": []}

# Counter data
for idx, counter in enumerate(
    counters_situation[1:], start=1
):  # Ignore the first counter
    # The interlocutor is the key with value 1
    target = [key for key, value in counter.items() if value == 1][0]

    # Iterate over all languages (source) and their values
    for source, value in counter.items():
        if source != target:  # Ignore the interlocutor itself as source
            situation_data["source"].append(source)
            situation_data["target"].append(target)
            situation_data["value"].append(value)

# Create unique labels
unique_labels_situation = list(set(situation_data["source"] + situation_data["target"]))

# Convert labels to numerical indices
label_to_index_situation = {label: i for i, label in enumerate(unique_labels_situation)}

# Generate numerical indices for 'source' and 'target'
source_indices_situation = [
    label_to_index_situation[src] for src in situation_data["source"]
]
target_indices_situation = [
    label_to_index_situation[tgt] for tgt in situation_data["target"]
]

languages_colors_situations_nodes = {
    "No language given": "rgba(0, 104, 201, 1.0)",
    "Dutch": "rgba(158, 115, 45, 1.0)",
    "Turkish": "rgba(13, 59, 102, 1.0)",
    "French": "rgba(238, 150, 75, 1.0)",
    "German": "rgba(185, 117, 39, 1.0)",
    "Şexbizinî": "rgba(249, 87, 56, 1.0)",
    "Other language": "rgba(229, 183, 16, 1.0)",
    "Kurmanji": "rgba(102, 17, 0, 1.0)",
    "when praying": "rgba(216, 198, 151, 1.0)",
    "when counting": "rgba(216, 198, 151, 1.0)",
    "explanations to children": "rgba(216, 198, 151, 1.0)",
    "when dreaming": "rgba(216, 198, 151, 1.0)",
    "shouting at children": "rgba(216, 198, 151, 1.0)",
    "when joking": "rgba(216, 198, 151, 1.0)",
    "discussing": "rgba(216, 198, 151, 1.0)",
    "playing": "rgba(216, 198, 151, 1.0)",
    "talking to a beloved person": "rgba(216, 198, 151, 1.0)",
    "when cursing": "rgba(216, 198, 151, 1.0)",
    "singing": "rgba(216, 198, 151, 1.0)",
    "speaking about private topics": "rgba(216, 198, 151, 1.0)",
}

# Create the Sankey diagram for situations
fig3 = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=25,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=unique_labels_situation,
                color=[
                    languages_colors_situations_nodes[label]
                    for label in unique_labels_situation
                ],
            ),
            link=dict(
                source=source_indices_situation,  # Indices correspond to labels
                target=target_indices_situation,
                value=situation_data["value"],
                color=[
                    languages_colors_links[label]
                    for label in situation_data["source"]
                ],
            ),
        )
    ]
)

fig3.update_layout(title_text="Situations", font_size=15, width=1250, height=1000)
fig3_html = fig3.to_html(full_html=False, include_plotlyjs=False)


#####################################################################################################
# Media

# Read the CSV file and extract language data
with open("../data/csv/media.csv", encoding="utf-8-sig") as file_obj:
    reader_obj = csv.reader(file_obj, delimiter=";")

    for row in reader_obj:
        cleaned_row = []
        for r in row:
            if "," in r:
                for lang in r.split(","):
                    lang = lang.strip()
                    cleaned_row.append(lang)
            else:
                cleaned_row.append(r.strip())
        media.append(cleaned_row)

counters_media = []

# Count occurrences of each language per media
for me in media:
    ctr = Counter(me)
    counters_media.append(ctr)

# Create dictionary
media_data = {"source": [], "target": [], "value": []}

# Counter data
for idx, counter in enumerate(counters_media[1:], start=1):  # Ignore the first counter
    # The interlocutor is the key with value 1
    target = [key for key, value in counter.items() if value == 1][0]

    # Iterate over all languages (source) and their values
    for source, value in counter.items():
        if source != target:  # Ignore the interlocutor itself as source
            media_data["source"].append(source)
            media_data["target"].append(target)
            media_data["value"].append(value)

# Create unique labels
unique_labels_media = list(set(media_data["source"] + media_data["target"]))

# Convert labels to numerical indices
label_to_index_media = {label: i for i, label in enumerate(unique_labels_media)}

# Generate numerical indices for 'source' and 'target'
source_indices_media = [label_to_index_media[src] for src in media_data["source"]]
target_indices_media = [label_to_index_media[tgt] for tgt in media_data["target"]]

languages_colors_media_nodes = {
    "No language given": "rgba(0, 104, 201, 1.0)",
    "Dutch": "rgba(158, 115, 45, 1.0)",
    "Turkish": "rgba(13, 59, 102, 1.0)",
    "French": "rgba(238, 150, 75, 1.0)",
    "German": "rgba(185, 117, 39, 1.0)",
    "Şexbizinî": "rgba(249, 87, 56, 1.0)",
    "Other language": "rgba(229, 183, 16, 1.0)",
    "Kurmanji": "rgba(102, 17, 0, 1.0)",
    "music": "rgba(216, 198, 151, 1.0)",
    "sms": "rgba(216, 198, 151, 1.0)",
    "television": "rgba(216, 198, 151, 1.0)",
    "books": "rgba(216, 198, 151, 1.0)",
    "email": "rgba(216, 198, 151, 1.0)",
    "facebook": "rgba(216, 198, 151, 1.0)",
    "whatsapp": "rgba(216, 198, 151, 1.0)",
    "instagram": "rgba(216, 198, 151, 1.0)",
    "youtube": "rgba(216, 198, 151, 1.0)",
    "twitter": "rgba(216, 198, 151, 1.0)",
    "tiktok": "rgba(216, 198, 151, 1.0)",
    "jokes": "rgba(216, 198, 151, 1.0)",
    "shopping list": "rgba(216, 198, 151, 1.0)",
    "diaries": "rgba(216, 198, 151, 1.0)",
    "other media": "rgba(216, 198, 151, 1.0)",
    "telegram": "rgba(216, 198, 151, 1.0)",
    "discord": "rgba(216, 198, 151, 1.0)",
    "songs": "rgba(216, 198, 151, 1.0)",
    "poems": "rgba(216, 198, 151, 1.0)",
    "stories": "rgba(216, 198, 151, 1.0)",
    "letters": "rgba(216, 198, 151, 1.0)",
}

# Create the Sankey diagram for media
fig4 = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=25,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=unique_labels_media,
                color=[
                    languages_colors_media_nodes[label] for label in unique_labels_media
                ],
            ),
            link=dict(
                source=source_indices_media,  # Indices correspond to labels
                target=target_indices_media,
                value=media_data["value"],
                color=[
                    languages_colors_links[label]
                    for label in media_data["source"]
                ],
            ),
        )
    ]
)

fig4.update_layout(title_text="Media", font_size=15, width=1250, height=1000)
fig4_html = fig4.to_html(full_html=False, include_plotlyjs=False)


#####################################################################################################
# Write HTML file

with open("../sankey.html", "w") as f:
    f.write(
        """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sankey Diagram | The language use web</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="./css/style.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </head>
  <body>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Sankey Diagram</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="nav-link active" aria-current="page" href="index.html">Home</a>
            <a class="nav-link" href="#interlocutors">Interlocutors</a>
            <a class="nav-link" href="#places">Places</a>
            <a class="nav-link" href="#situations">Situations</a>
            <a class="nav-link" href="#media">Media</a>
          </div>
        </div>
      </div>
    </nav>
  <div class="container-md">
    <div id="interlocutors" class="diagram">"""
    )
    f.write(fig1_html)
    f.write(
        """</div>
    <div id="places" class="diagram">"""
    )
    f.write(fig2_html)
    f.write(
        """</div>
    <div id="situations" class="diagram">"""
    )
    f.write(fig3_html)
    f.write(
        """</div>
    <div id="media" class="diagram">"""
    )
    f.write(fig4_html)
    f.write(
        """</div>
    </div>
    </body>
    </html>
    """
    )
