from flask_restful import Resource
from flask import jsonify
import sqlite3
from ubc_grades_api.api import app

from helpers import section_dict_factory

class Section(Resource):
    def get(self, yearsession, subject, course, section):
        query = "SELECT * FROM grades WHERE yearsession = ? AND subject = ? AND course = ? AND section = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = section_dict_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject, course, section]).fetchone()

        return jsonify(results) if results != None else {}

class Course(Resource):
    def get(self, yearsession, subject, course):
        query = "SELECT * FROM grades WHERE yearsession = ? AND subject = ? AND course = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = section_dict_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject, course]).fetchall()

        return jsonify(results)

class Subject(Resource):
    def get(self, yearsession, subject):
        query = "SELECT * FROM grades WHERE yearsession = ? AND subject = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = section_dict_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject]).fetchall()

        return jsonify(results)

class YearSession(Resource):
    def get(self, yearsession):
        query = "SELECT * FROM grades WHERE yearsession = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = section_dict_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession]).fetchall()

        return jsonify(results)