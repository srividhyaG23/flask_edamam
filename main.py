import os
import requests


# Following example usage from https://developer.edamam.com/edamam-docs-recipe-api
def edamam_search(query):
    # In e.g. Heroku and Pycharm, environment variables can easily be provided
    # Pass our Edamam credentials in with env variables so they're not in source code (keep them private)
    app_id = os.environ['APP_ID']
    app_key = os.environ['APP_KEY']

    request = f"https://api.edamam.com/search?q={query}" \
              f"&app_id={app_id}" \
              f"&app_key={app_key}"

    response = requests.get(request)
    hits = response.json()['hits']

    for hit in hits:
        recipe = hit['recipe']
        print(f"---{recipe['label']}---")
        for ingredient in recipe['ingredients']:
            print(f"   {ingredient['text']}")


if __name__ == '__main__':
    edamam_search('nutritional yeast')

