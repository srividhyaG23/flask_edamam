*flask_edamam*

A website for finding recipes that use your ingredients!

This project is a **Flask** server which:
- calls the Edamam recipe **API** to get recipes with your ingredients 
- uses **Jinja** to render a html response from a template and Edamam's response data
- is hosted on **Heroku**

Please note that I'm just using the free Heroku tier, so the website should take "seconds" to spin up.

If you want to run this locally:
- clone the source code (`git clone https://github.com/IdiosApps/flask_edamam.git`)
- Set the environment variables `APP_ID` and `APP_KEY` in e.g. Pycharm. You can get your own values for these at https://developer.edamam.com/edamam-recipe-api - keep them private!
- Install requirements