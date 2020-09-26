from flask import Flask, render_template
import json

app = Flask(__name__)

# Just for pytest purposes
testing = 'Network Automation Training'

# Dummy Database data call
vendors = [
    {'cisco': 'routers',
     'juniper': 'switches',
     'palo alto': 'firewall',
     'aris': ' spine switch'},
    {'country': 'USA',
     'state': 'California',
     'city': 'San Francisco',
     'author': 'Alp'}
]

vendors_to_json = json.dumps(vendors, indent=4)


@app.route("/")
def home():
    return render_template('home.html', vendor=vendors_to_json)


@app.route("/nornir")
def nornir():
    return render_template('nornir.html')


if __name__ == '__main__':
    app.run(debug=True)

