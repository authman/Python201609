from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movie', methods=['POST'])
def get_movie():
    artist = request.form['user_input'].replace(' ','')
    url = 'https://itunes.apple.com/search?term='+artist+'&entity=musicVideo'
    response = requests.get(url).content
    return response

app.run(debug=True)
