import requests
url = 'https://superheroapi.com/api/2619421814940190/search/'

heroes = {}


def find_smartest_hero():
    names = ['Hulk', 'Thanos', 'Captain America']
    sorted_heroes = []
    for name in names:
        id_name = url + name.strip()
        resp = requests.get(id_name).json()
        heroes[resp['results'][0]['name']] = resp['results'][0]['powerstats']['intelligence']
        sorted_heroes = (sorted(heroes.items()))
    print(f'Самый умный герой - {sorted_heroes[-1][0]}')


find_smartest_hero()
