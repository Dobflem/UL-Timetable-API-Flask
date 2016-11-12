#!/usr/bin/python
# -*- coding: utf-8 -*-

from ul_timetable_api import get_timetable_json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World'


@app.route('/<int:id>')
def get_timetable(id):
    return jsonify(**get_timetable_json(id))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
