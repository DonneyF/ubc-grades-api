from ubc_grades_api import app
import os
from config import *

if __name__ == "__main__":
    app.debug = False
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
