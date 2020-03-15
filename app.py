from flask import Flask, jsonify, redirect, render_template, request
from flask_bootstrap import Bootstrap
from datetime import *


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["expires"] = 0
    response.headers["pragma"] = "no-cache"
    return response


if __name__ == '__main__':
    app.run()
