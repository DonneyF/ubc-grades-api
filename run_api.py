from ubc_grades_api.api import app
import os

if __name__ == "__main__":
    app.debug = False
    app.config['DATABASE_NAME'] = 'database.db'
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)