from flask import Flask, render_template, jsonify
import requests

URl = "https://www.freetogame.com/api/games"


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(URl)
    if response.status_code == 200:
        games = response.json()[:10]
    else:
        games = []

    return render_template('index.html', games=games)



if __name__ == '__main__':
    app.run(debug=True)