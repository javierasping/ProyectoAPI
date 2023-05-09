import requests

url = "https://gateway.marvel.com:443/v1/public/creators?&apikey=1bf075d536f284d8d6c923c4b425be90&hash=9b48d9ee2ab77083b0e90f00e7549b90&ts=1683568770.2235572"

respuesta = requests.get(url)

respuesta_json= respuesta.json()

for i in respuesta_json['data']['results']:
    for comic in i['comics']['items']:
        print(comic['name'])




# https://gateway.marvel.com/v1/public/characters?apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=I&orderBy=name&limit=5&apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/series?apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/characters?limit=1&apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/comics?limit=1&apikey=1bf075d536f284d8d6c923c4b425be90&hash=e563065eef6867ef34c141a04500e0b6&ts=1683568390.0844688