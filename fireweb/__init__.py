#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
firebat-web.app
~~~~~~~~~~~~~~~

Describes WSGI application.
"""

import os

import flask
from flask import send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.contrib.fixers import ProxyFix

from example import example

app = flask.Flask(__name__)
app.config.from_envvar('FIRE_WEB_CFG')
app.wsgi_app = ProxyFix(app.wsgi_app)  # Fix for old proxyes
db = SQLAlchemy(app)

# Register different apps
app.register_blueprint(example, url_prefix='/example')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'img'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
