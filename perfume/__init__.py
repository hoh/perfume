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


def route(regex, **kwds):
    'Decorates your function with a route as "function.perfume_route = ..."'
    def decorator(func):
        func.perfume_route = regex
        func.perfume_args = kwds
        return func
    return decorator


class Perfume(object):

    def __init__(self, import_name,
                 static_url_path=None,
                 static_folder="static",
                 static_host=None,
                 host_matching=False,
                 subdomain_matching=False,
                 template_folder="templates",
                 instance_path=None,
                 instance_relative_config=False,
                 root_path=None):
        self.app = Flask(import_name=import_name,
                         static_url_path=static_url_path,
                         static_folder=static_folder,
                         static_host=static_host,
                         host_matching=host_matching,
                         subdomain_matching=subdomain_matching,
                         template_folder=template_folder,
                         instance_path=instance_path,
                         instance_relative_config=instance_relative_config,
                         root_path=root_path)
        self._load()

    def _load(self):
        "Updates the app's routes with all methods."
        for name in dir(self):
            method = self.__getattribute__(name)
            try:
                route = method.perfume_route
                args = method.perfume_args
            except AttributeError:
                continue

            self.app.route(route, **args)(method)

    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        self.app.run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

