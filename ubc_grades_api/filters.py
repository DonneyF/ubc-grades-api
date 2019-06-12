from flask_restful import Resource, Api
from flask import jsonify
import sqlite3
from ubc_grades_api.api import app

from helpers import yearsessions, basic_element_factory, subjects

class Sections(Resource):
    def get(self, yearsession, subject, course):
        query = "SELECT DISTINCT section FROM grades WHERE yearsession = ? AND subject = ? AND course = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject, course]).fetchall()

        return jsonify(results)

class Courses(Resource):
    def get(self, yearsession, subject):
        query = "SELECT DISTINCT course FROM grades WHERE yearsession = ? AND subject = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject]).fetchall()

        return jsonify(results)

class CoursesNoYearsession(Resource):
    def get(self, subject):
        query = "SELECT DISTINCT course FROM grades WHERE subject = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [subject]).fetchall()

        return jsonify(results)

class Subjects(Resource):
    def get(self, yearsession=None):
        if yearsession == None:
            return jsonify(subjects)

        query = "SELECT DISTINCT subject FROM grades WHERE yearsession = ?;"

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession]).fetchall()

        return jsonify(results)

class YearSessions(Resource):
    def get(self):
        return jsonify(yearsessions)