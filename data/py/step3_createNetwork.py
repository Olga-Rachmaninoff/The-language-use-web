'''
Create a network graph from nodes and links data in JSON format and save it as an HTML file.
Input: JSON file with nodes and links for the network visualization
Output: HTML file with the network graph
'''

import networkx as nx
import json
from pyvis.network import Network
from IPython.display import display, HTML

G = nx.Graph()

nodes = []
links = []

# Read the nodes and links from the JSON file and add them to the graph.
with open("../data/json/nodes_links.json", encoding='utf-8') as f:
    data = json.load(f)
    for node in data['nodes']:
        nodes.append((node['id'], {"color": node['color']}))
    for link in data['links']:
        links.append((link['source'], link['target']))

G.add_nodes_from(nodes)
G.add_edges_from(links)

# Create a pyvis network graph from the networkx graph.
nt = Network(height='550px', width='100%', bgcolor='#ffffff', font_color='black', select_menu=True, cdn_resources='remote')

nt.set_options("""
const options = {
  "nodes": {
    "borderWidth": 3,
    "borderWidthSelected": 80,
    "color": {
      "border": "#2B7CE9",
      "background": "#D2E5FF",
      "highlight": {
        "border": "#2B7CE9",
        "background": "#D2E5FF"
      },
      "hover": {
        "border": "#2B7CE9",
        "background": "#D2E5FF"
      }
    },
    "font": {
      "color": "#343434",
      "size": 40
    },
    "size": 50,
    "scaling": {
      "enabled": false
    }
  },
  "edges": {
    "color": {
      "inherit": "both"
    },
    "smooth": {
      "enabled": true,
      "type": "dynamic"
    },
    "width": 10
  },
  "physics": {
    "enabled": true,
    "barnesHut": {
      "gravitationalConstant": -3000,
      "centralGravity": 0.005,
      "springLength": 500,
      "springConstant": 0.01,
      "damping": 0.8,
      "avoidOverlap": 0.7
    },
    "maxVelocity": 1,
    "minVelocity": 0,
    "solver": "barnesHut",
    "timestep": 0.001,
    "stabilization": {
      "enabled": true,
      "fit": true
    }
  }
}
""")

nt.from_nx(G)

html = nt.generate_html()


##########################################################################################################################################

# Save the network graph as an HTML file.
with open('../network.html', 'w', encoding='utf-8') as file:
    file.write(
        """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Network | The language use web</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="./css/style.css">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </head>
  <body>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Network</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <a class="nav-link active" aria-current="page" href="index.html">Home</a>
          </div>
        </div>
      </div>
    </nav>
  <div class="container-md">
    <div id="network" class="network">"""
    )
    file.write(html)
    file.write(
        """</div>
    </div>
    </body>
    </html>
    """
    )
HTML(html)