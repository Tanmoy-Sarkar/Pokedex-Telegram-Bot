import json
import requests


def pokedex(id_name):

    output= {}
    url = "https://pokeapi.co/api/v2/pokemon/{}/"
    #get request for API information retrieval
    final_url = url.format(id_name)
    response = requests.get(final_url)
    response = response.content
    #json to python dictionary convertion
    information=json.loads(response)
    #getting all the information 
    output['id'] = information['id']
    output['name'] = information['name']
    output['height'] = information['height']
    output['weight'] = information['weight']
    all_types=information['types']
    types = []
    for type_ in all_types:
        types.append(type_['type']['name'])
    output['types'] = types
    all_moves=information['moves']
    moves = []
    #getting 5 moves of the pokemon
    for i in range(6):
        moves.append(all_moves[i]['move']['name'])
    output['moves'] = moves
    return output

