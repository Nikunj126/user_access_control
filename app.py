from flask import Flask
from Database.db import initialize_db
from flask_restful import Api
from OPS.routes import *

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/nknj'
}

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
