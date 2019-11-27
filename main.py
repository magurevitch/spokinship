import json
from graphviz import Digraph


def label_maker(hash_name: str, data: dict):
    try:
        birth = [year for person, year in data['relations']['born'] if person == hash_name][0]
    except IndexError:
        birth = ''
    try:
        death = [year for person, year in data['relations']['died'] if person == hash_name][0]
    except IndexError:
        death = ''
    if birth or death:
        label = f'{hash_name} \n {birth} - {death}'
    else:
        label = f'{hash_name}'
    return label


def main():
    with open('predicates.json', 'r') as infile:
        data = json.load(infile)

    parsed_data = Digraph(comment="Family tree")

    for hash_name in data['hashes']:
        label = label_maker(hash_name, data)
        parsed_data.node(hash_name, label)

    for parent, child in data['relations']['parents']:
        parsed_data.edge(parent, child)

    for partner1, partner2, year in data['relations']['marriages']:
        parsed_data.edge(partner1, partner2, label=f'{year}', constraint='false', arrowhead='none')


    parsed_data.render('output/output.gv', view=True)


if __name__ == '__main__':
    main()
