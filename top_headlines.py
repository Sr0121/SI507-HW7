from flask import Flask, render_template
import secrets
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Welcome!</h1>'


@app.route('/name/<input_name>')
def name(input_name):
    return render_template('name.html', name=input_name)


@app.route('/headlines/<input_name>')
def headline(input_name):
    para_dict = {"api-key": secrets.api_key}
    resp = requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json", para_dict)
    results = resp.json()["results"]
    titles = []
    for res in results:
        titles.append(res["title"])
    return render_template('headlines.html', titles=titles, name=input_name)


@app.route('/links/<input_name>')
def links(input_name):
    para_dict = {"api-key": secrets.api_key}
    resp = requests.get("https://api.nytimes.com/svc/topstories/v2/technology.json", para_dict)
    results = resp.json()["results"]
    urls = []
    titles = []
    for res in results:
        urls.append(res["url"])
        titles.append(res["title"])
    return render_template('links.html', titles=titles, urls=urls, name=input_name)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
