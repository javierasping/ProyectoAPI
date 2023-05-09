import requests

url = "https://gateway.marvel.com:443/v1/public/stories?limit=10&apikey=1bf075d536f284d8d6c923c4b425be90&hash=9318f4a5dbf8d484a9ca6d7982a2306f&ts=1683570269.7742023"

respuesta = requests.get(url)

respuesta_json= respuesta.json()

for i in respuesta_json['data']['results']:
    print(i['title'])




# https://gateway.marvel.com/v1/public/characters?apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=I&orderBy=name&limit=5&apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/series?apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/characters?limit=1&apikey=1bf075d536f284d8d6c923c4b425be90&hash=71fc8f2c795e90c55924a4de0c858519&ts=1683568166.7326257
# https://gateway.marvel.com:443/v1/public/comics?limit=1&apikey=1bf075d536f284d8d6c923c4b425be90&hash=e563065eef6867ef34c141a04500e0b6&ts=1683568390.0844688