#!/usr/bin/python
# -*- coding: utf-8 -*-

from ul_timetable_api import get_student_timetable_json
from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify({'error': 'Internal server error'}, 500))

@app.route('/')
def home():
    return 'Homepage of APIs created and maintained by Russell Hickey'


@app.route('/timetable/v1/student/<int:id>')
def get_timetable(id):
    return jsonify(**get_student_timetable_json(id))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
