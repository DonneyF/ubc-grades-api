import flask
from flask_restful import Api
from flask_cors import CORS

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config["DEBUG"] = True
api = Api(app)

# Add API resources
import ubc_grades_api.course_profile as cp
import ubc_grades_api.section_view as sv
import ubc_grades_api.filters as filters

# Section View Grades
api.add_resource(sv.Section, '/api/v1/grades/<string:yearsession>/<string:subject>/<string:course>/<string:section>')
api.add_resource(sv.Course, '/api/v1/grades/<string:yearsession>/<string:subject>/<string:course>')
api.add_resource(sv.Subject, '/api/v1/grades/<string:yearsession>/<string:subject>')
api.add_resource(sv.YearSession, '/api/v1/grades/<string:yearsession>')

# Course Filters
api.add_resource(filters.Sections, '/api/v1/sections/<string:yearsession>/<string:subject>/<string:course>')
api.add_resource(filters.Courses, '/api/v1/courses/<string:yearsession>/<string:subject>')
api.add_resource(filters.CoursesNoYearsession, '/api/v1/courses/<string:subject>')
api.add_resource(filters.Subjects, '/api/v1/subjects', '/api/v1/subjects/<string:yearsession>')
api.add_resource(filters.YearSessions, '/api/v1/yearsessions')

# Course Profile
api.add_resource(cp.AverageHistory, '/api/v1/course-profile/averages/<string:subject>', '/api/v1/course-profile/averages/<string:subject>/<string:course>')
api.add_resource(cp.DistributionHistory, '/api/v1/course-profile/distributions/<string:subject>', '/api/v1/course-profile/distributions/<string:subject>/<string:course>')
api.add_resource(cp.InstructorHistory, '/api/v1/course-profile/instructors/<string:subject>', '/api/v1/course-profile/instructors/<string:subject>/<string:course>')
api.add_resource(cp.General, '/api/v1/course-profile/<string:subject>', '/api/v1/course-profile/<string:subject>/<string:course>')
api.add_resource(cp.OfferHistory, '/api/v1/course-profile/offerings/<string:subject>', '/api/v1/course-profile/offerings/<string:subject>/<string:course>')

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.errorhandler(404)
def error_handler(e): return page_not_found(e)