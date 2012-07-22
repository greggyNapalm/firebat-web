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
from fireweb.database import db_session
from .models import User


@example.route('/')
def test():
    usr_count = User.query.count()
    #all_usr = User.query.all().first()
    usr = User.query.filter(User.name == 'admin').first()
    print usr_count
    #print all_usr
    return 'In example blueprint: ' + str(usr.name)
