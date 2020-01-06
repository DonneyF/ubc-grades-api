from config import api_v1_database_path as database
from flask import Blueprint
from flask_restful import Api
from ubc_grades_api.v1.section_view import *
from ubc_grades_api.v1.course_profile import *
from ubc_grades_api.v1.filters import *

blueprint = Blueprint('old', __name__)
api = Api(blueprint)

# Section View Grades
api.add_resource(Section, '/grades/<string:yearsession>/<string:subject>/<string:course>/<string:section>')
api.add_resource(Course, '/grades/<string:yearsession>/<string:subject>/<string:course>')
api.add_resource(Subject, '/grades/<string:yearsession>/<string:subject>')
api.add_resource(YearSession, '/grades/<string:yearsession>')

# Course Profile
api.add_resource(AverageHistory, '/course-profile/averages/<string:subject>',
                 '/course-profile/averages/<string:subject>/<string:course>')
api.add_resource(DistributionHistory, '/course-profile/distributions/<string:subject>',
                 '/api/course-profile/distributions/<string:subject>/<string:course>')
api.add_resource(InstructorHistory, '/course-profile/instructors/<string:subject>',
                 '/course-profile/instructors/<string:subject>/<string:course>')
api.add_resource(General, '/course-profile/<string:subject>',
                 '/api/course-profile/<string:subject>/<string:course>')
api.add_resource(OfferHistory, '/course-profile/offerings/<string:subject>',
                 '/course-profile/offerings/<string:subject>/<string:course>')


# Filters
api.add_resource(Sections, '/sections/<string:yearsession>/<string:subject>/<string:course>')
api.add_resource(Courses, '/courses/<string:yearsession>/<string:subject>')
api.add_resource(CoursesNoYearsession, '/courses/<string:subject>')
api.add_resource(Subjects, '/subjects', '/subjects/<string:yearsession>')
api.add_resource(YearSessions, '/yearsessions')
