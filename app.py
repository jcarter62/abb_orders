from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os, json
from laterals import Laterals

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/laterals')
def route_laterals():
    l = Laterals()
    return json.dumps({'laterals': l.lats})

if __name__ == '__main__':
    app.run()
