from flask import Flask, current_app
from twilio.rest import Client
from fastapi import FastAPI

from config import config

FastAPI = FastAPI()
client = Client(current_app.config["ACCOUNT_SID"], current_app.congfig["AUTH_TOKEN"])

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    FastAPI.init_app(app)
    client.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app