from flask import Flask
from config import Config
from injector import Injector
from flask_injector import FlaskInjector

from src.app.module import AppModule
from src.routes import test_bp

def create_config() -> Config:
    return Config()

def create_app(name: str) -> Flask:
    app = Flask(name)

    app.config.from_object(create_config())
    app.url_map.strict_slashes = False

    app.register_blueprint(test_bp, url_prefix='/test')

    with app.app_context():
        injector = Injector([AppModule(app)])

    FlaskInjector(app=app, injector=injector)

    return app
