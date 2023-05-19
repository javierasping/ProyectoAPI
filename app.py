import requests
import json
from flask import Flask, render_template, abort, redirect, request

app = Flask(__name__)
url = "https://gateway.marvel.com/v1/public/characters?apikey=1bf075d536f284d8d6c923c4b425be90&hash=0ac16158f12e2734c5e67838045eded3&ts=1683278024.2311842"

@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")



@app.route('/listapersonajes', methods=["POST"])
def listapersonajes():
    search_query = request.form.get('busqueda')

    respuesta = requests.get(url)
    personajes = respuesta.json()

    lista_personajes_a_mostrar = []
    if search_query:
        for personaje in personajes['data']['results']:
            if search_query.lower() in personaje['name'].lower():
                lista_personajes_a_mostrar.append(personaje)
    else:
        lista_personajes_a_mostrar = personajes['data']['results']

    return render_template('listapersonajes.html', personajes=lista_personajes_a_mostrar)






@app.route('/juegosV2', methods=['GET', 'POST'])
def juegosV2():
    search_query = request.form.get('search_query')
    respuesta = requests.get(url)
    personajes = respuesta.json()

    lista_personajes_a_mostrar = []
    if search_query:
        for personaje in personajes['data']['results']:
            if search_query.lower() in personaje['name'].lower():
                lista_personajes_a_mostrar.append(personaje)
    else:
        lista_personajes_a_mostrar = personajes['data']['results']

    return render_template('juegos_V2.html', personajes=lista_personajes_a_mostrar, search_query=search_query)


@app.route('/detalle/<personaje_id>')
def detalle(personaje_id):
    detalle_url = f"https://gateway.marvel.com:443/v1/public/characters/{personaje_id}?apikey=1bf075d536f284d8d6c923c4b425be90&hash=5c4fcf5b8e5af6439488993f74000916&ts=1684239839.016359"
    respuesta = requests.get(detalle_url)
    detalle_personaje = respuesta.json()

    if detalle_personaje['data']['results']:
        personaje = detalle_personaje['data']['results'][0]

        # Obtener listas de comics, series, historias y eventos
        comics = [comic['name'] for comic in personaje['comics']['items']]
        series = [serie['name'] for serie in personaje['series']['items']]
        historias = [historia['name'] for historia in personaje['stories']['items']]
        eventos = [evento['name'] for evento in personaje['events']['items']]

        return render_template('detalle.html', personaje=personaje, comics=comics, series=series, historias=historias, eventos=eventos)
    else:
        return render_template('error.html', mensaje="No se encontró información del personaje")





@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 5000, debug=True)
