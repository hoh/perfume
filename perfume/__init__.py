# -*- coding: utf-8 -*-

"""
    Perfume
    ~~~~~~~

    Perfume aims at making Flask-apps more Object-Oriented friendly
    by providing a base class to create them.

    :copyright: (c) 2013 by Hugo Herter
    :license: BSD, see LICENSE for more details.

    Usage:
    - inherit from Perfume
    - decorate your methods with route(path)

    Exemple:

        from perfume import route, Perfume

        class MyApp(Perfume):

            @route('/')
            def hello(self):
                return "Hello World !"

        if __name__ == "__main__":
            MyApp().run()

"""

__version__ = '0.1'

__all__ = 'route', 'Perfume'

from flask import Flask


def route(regex):
    'Decorates your function with a route as "function.route = ..."'
    def decorator(func):
        func.route = regex
        return func
    return decorator


class Perfume(object):

    def __init__(self, debug=False):
        ''
        self.app = Flask(__name__)
        self.app.debug = debug
        self._load()

    def _load(self):
        "Updates the app's routes with all methods."
        for name in dir(self):
            method = self.__getattribute__(name)
            try:
                self.app.route(method.route)(method)
            except AttributeError:
                pass

    def run(self):
        self.app.run()


