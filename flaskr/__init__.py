import os
from flask import Flask
from . import app


def create_app():
    # return app object from app module
    return app.app
