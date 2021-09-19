from models.pokemon import Pokemon
from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/buscar", methods = ["GET", "post"])
def buscar():
    pokemon = Pokemon(request.form["nome"].lower(), "")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        result = res["sprites"]
        result = result["front_default"]
        pokemon.foto = result
    except:
        return "Nenhum Pokemon encontrado!"

    return render_template("Index.html", nome = pokemon.nome, foto = pokemon.foto)

if __name__ == "__main__":
    app.run(debug=True)