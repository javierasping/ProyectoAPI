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

# respuesta = requests.get(url)
# respuesta_json= respuesta.json()

@app.route('/listajuegos', methods=["POST"])
def listajuegos():
    search_query = request.form.get('search_query')
    categoria_query = request.form.get('categoria_query')

    respuesta = requests.get(url)
    juegos= respuesta.json()
    
    lista_juegos_a_mostrar = []
    for juego in juegos['data']['results']:
        if search_query and search_query.lower() not in juego['name'].lower():
            lista_juegos_a_mostrar.append(juego)

    return render_template('listajuegos.html', juegos=lista_juegos_a_mostrar)
    


@app.route('/juego/<int:id>')
def juego(id):
    with open('juegos.json') as f:
        juegos = json.load(f)
    for juego in juegos:
        if juego['id'] == id:
            return render_template('detalle.html', juego=juego)
    abort(404)



@app.route('/juegosV2', methods=['GET', 'POST'])
def juegosV2():
    search_query = request.form.get('search_query')
    respuesta = requests.get(url)
    juegos = respuesta.json()

    lista_juegos_a_mostrar = []
    for juego in juegos['data']['results']:
            lista_juegos_a_mostrar.append(juego)


    # for juego in juegos:
    #     if search_query and str(juego["nombre"]).lower().startswith(str(search_query).lower()):
    #         if categoria_query and str(juego["categoria"]).lower() == str(categoria_query).lower():
    #             lista_juegos_a_mostrar.append(juego)
    #         elif not categoria_query:
    #             lista_juegos_a_mostrar.append(juego)
    #     elif not search_query:
    #         if categoria_query and str(juego["categoria"]).lower() == str(categoria_query).lower():
    #             lista_juegos_a_mostrar.append(juego)
    #         elif not categoria_query:
    #             lista_juegos_a_mostrar.append(juego)

    return render_template('juegos_V2.html', juegos=lista_juegos_a_mostrar, search_query=search_query)




@app.route('/error')
def error():
    return abort(404)

app.run("0.0.0.0", 5000, debug=True)
