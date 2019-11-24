import json
from graphviz import Digraph
from itertools import chain


with open('predicates.json', 'r') as infile:
    data = json.load(infile)

parsed_data = Digraph(comment="Family tree")

for hash_name in data['hashes']:
    birth = [year for person, year in data['relations']['born'] if person == hash_name][0]
    death = [year for person, year in data['relations']['died'] if person == hash_name][0]
    label = f'{hash_name} \n {birth} - {death}'
    parsed_data.node(hash_name, label)

for parent, child in data['relations']['parents']:
    parsed_data.edge(parent, child)

# for partner1, partner2, year in data['relations']['marriages']:
#     parsed_data.


parsed_data.render('output/output.gv', view=True)
