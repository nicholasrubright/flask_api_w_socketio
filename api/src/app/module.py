from flask import Flask
from injector import Module, singleton

class AppModule(Module):
    def __init__(self, app: Flask):
        self.app = app

    def configure(self, binder):
        pass