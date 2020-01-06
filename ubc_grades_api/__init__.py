import flask
from flask_restful import Api
from flask_cors import CORS

# Add API resources
from ubc_grades_api.v1 import blueprint as v1_blueprint
from ubc_grades_api.old import blueprint as old_blueprint

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
api = Api(app)

app.register_blueprint(v1_blueprint, url_prefix="/api/v1")
app.register_blueprint(old_blueprint, url_prefix="/api")


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.errorhandler(404)
def error_handler(e):
    return '''<h1>Error 404</h1>
<p>Page not found</p>'''