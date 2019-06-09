from flask_restful import Resource, Api
from flask import request, jsonify
import sqlite3
from ubc_grades_api.api import app

from helpers import dict_factory, arr_to_dict

def general_get(db_table, subject, course, select_qty, key=None):
    if course == None:
        query = f"SELECT * FROM {db_table} WHERE subject = ?;"
        to_filter = [subject]
    else:
        query = f"SELECT * FROM {db_table} WHERE subject = ? AND course = ?;"
        to_filter = [subject, course]

    conn = sqlite3.connect(app.config['DATABASE_NAME'])
    conn.row_factory = dict_factory
    cur = conn.cursor()
    if select_qty == 'many':
        results = cur.execute(query, to_filter).fetchall()
        results = arr_to_dict(results, key)
    else:
        results = cur.execute(query, to_filter).fetchone()

    return jsonify(results) if results != None else {}

class AverageHistory(Resource):
    def get(self, subject, course=None):
        return general_get("cp_avg_hist", subject, course, 'one')

class DistributionHistory(Resource):
    def get(self, subject, course=None):
        return general_get("cp_dists", subject, course, 'many', 'yearsession')

class OfferHistory(Resource):
    def get(self, subject, course=None):
        return general_get("cp_offer_hist", subject, course, 'one')

class InstructorHistory(Resource):
    def get(self, subject, course=None):
        if course == None:
            to_filter = [subject]
            query = "SELECT * FROM cp_instr_hist_by_subject WHERE subject = ?;"
        else:
            query = "SELECT * FROM cp_instr_hist WHERE subject = ? AND course = ?;"
            to_filter = [subject, course]

        conn = sqlite3.connect(app.config['DATABASE_NAME'])
        conn.row_factory = dict_factory
        # Below is an alternative factory if we wish to omit rows with 0 entries.
        #conn.row_factory = lambda cursor, row: {col[0]:row[idx] for idx, col in enumerate(cursor.description) if row[idx] != 0}

        cur = conn.cursor()
        results = cur.execute(query, to_filter).fetchall()
        results = arr_to_dict(results, 'instructor')
        return results

class General(Resource):
    def get(self, subject, course=None):
        return general_get("cp_general", subject, course, 'one')