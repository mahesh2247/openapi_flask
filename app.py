# import connexion
# from openapi_spec_validator import validate_spec
# from flask import Flask
# from flask_swagger_ui import get_swaggerui_blueprint
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# app_connexion = connexion.App(__name__, specification_dir="./")
# app_connexion.add_api("swagger.yml")


# @app.route("/")
# def home():
#     return "Hello"

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app_connexion.run()
#     # app.run()


from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import connexion
import os

basedir = os.path.abspath(os.path.dirname(__file__))

application = connexion.FlaskApp(__name__)

application.add_api("swagger.yml")
app = application.app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


