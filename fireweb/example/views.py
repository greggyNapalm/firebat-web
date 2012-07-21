# -*- encoding: utf-8 -*-

"""
firebat.console
~~~~~~~~~~~~~~

Helper script for Phantom load tool.
    * generate config files and input data.
    * runs test.
    * aggregate result data.
"""

from flask import request, jsonify, url_for, abort, redirect, flash
from flask import render_template as flask_render_template

from . import example


def render_template(template, **context):
    context['logged_user'] = session.get_user()
    context['logout_url'] = session.logout_url('/')
    return flask_render_template(template, **context)


@example.route("/check/")
def check(**kwargs):
    return 'check in example'
