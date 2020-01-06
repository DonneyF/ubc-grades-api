from flask_restful import Resource
from flask import jsonify
import sqlite3
from ubc_grades_api.v1 import database

from ubc_grades_api.helpers import yearsessions, basic_element_factory

class Sections(Resource):
    def get(self, yearsession, subject, course):
        query = "SELECT DISTINCT section FROM grades WHERE yearsession = ? AND subject = ? AND course = ?;"

        conn = sqlite3.connect(database)
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject, course]).fetchall()

        return jsonify(results)


class Courses(Resource):
    def get(self, yearsession, subject):
        query = "SELECT DISTINCT course FROM grades WHERE yearsession = ? AND subject = ?;"

        conn = sqlite3.connect(database)
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [yearsession, subject]).fetchall()

        return jsonify(results)


class CoursesNoYearsession(Resource):
    def get(self, subject):
        query = "SELECT DISTINCT course FROM grades WHERE  subject = ?;"

        conn = sqlite3.connect(database)
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, [subject]).fetchall()

        return jsonify(results)


class Subjects(Resource):
    def get(self, yearsession=None):
        if yearsession == None:
            query = "SELECT DISTINCT subject FROM grades;"
            to_filter = []
        else:
            query = "SELECT DISTINCT subject FROM grades WHERE yearsession = ?;"
            to_filter = [yearsession]

        conn = sqlite3.connect(database)
        conn.row_factory = basic_element_factory
        cur = conn.cursor()
        results = cur.execute(query, to_filter).fetchall()

        return jsonify(results)


class YearSessions(Resource):
    def get(self):
        return jsonify(yearsessions)
