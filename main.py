import os
import requests
from flask import Flask, send_from_directory
from flask import request
from jinja2 import Template

app = Flask(__name__, static_folder='static')
app.config["DEBUG"] = True


@app.route('/')
def home():
    return send_from_directory('static', filename='index.html')


@app.route('/recipes')
def search():
    ingredient = request.args.get('ingredient')

    hits = edamam_search(ingredient)

    with open('./templates/recipes.html') as file_:
        template = Template(file_.read())
    return template.render(ingredient=ingredient, hits=hits) # `a=b` Jinja finds `a` in template, uses `b`


# Following example usage from https://developer.edamam.com/edamam-docs-recipe-api
def edamam_search(query):
    # In e.g. Heroku and Pycharm, environment variables can easily be provided
    # Pass our Edamam credentials in with env variables so they're not in source code (keep them private)
    app_id = os.environ['APP_ID']
    app_key = os.environ['APP_KEY']

    curl = f"https://api.edamam.com/search?q={query}" \
           f"&app_id={app_id}" \
           f"&app_key={app_key}"

    response = requests.get(curl)
    hits = response.json()['hits']

    return hits


if __name__ == '__main__':
    app.run()

    # edamam_search('nutritional yeast')
