import requests

url = "https://gateway.marvel.com/v1/public/characters?apikey=1bf075d536f284d8d6c923c4b425be90&hash=0ac16158f12e2734c5e67838045eded3&ts=1683278024.2311842"

respuesta = requests.get(url)

respuesta_json= respuesta.json()

for i in respuesta_json['data']['results']:
    print(i['name'])

