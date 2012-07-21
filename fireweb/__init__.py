#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import flask

# load the middleware from werkzeug
# This middleware can be applied to add HTTP proxy support to an application
# that was not designed with HTTP proxies in mind.
# It sets EMOTE_ADDRfrom werkzeug.contrib.fixers import ProxyFix
from werkzeug.contrib.fixers import ProxyFix

app = flask.Flask(__name__)
app.config.from_envvar('FIRE_WEB_CFG')

#app.config.from_object('settings')
app.wsgi_app = ProxyFix(app.wsgi_app)


# Register different apps
#app.register_blueprint(111, url_prefix='/auth')


@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
