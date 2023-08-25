from flask import Flask
from injector import Module, singleton

from flask_marshmallow import Marshmallow


class AppModule(Module):
    def __init__(self, app: Flask):
        self.app = app

    def configure(self, binder):
        binder.bind(Marshmallow, to=self.getMarshmallow(), scope=singleton)

    def getMarshmallow(self) -> Marshmallow:
        return Marshmallow(self.app)