from flask import render_template
from favoritefive import app

favorite_people = ["Nicki M.", "Miley Cyrus", "Selena Gomez", "Karol G", "Jay Wheeler"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorite_five')
def favorite_five():
    return render_template('favorite_five.html', favorite_people=favorite_people)