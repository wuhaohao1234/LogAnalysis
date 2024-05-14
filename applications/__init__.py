import os

from flask import Flask

from applications.extensions import init_plugins
from applications.views import init_bps


def create_app(config_class):
    app = Flask(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    app.config.from_object(config_class)

    init_bps(app)
    init_plugins(app)

    return app
