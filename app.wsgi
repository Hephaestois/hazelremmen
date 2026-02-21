# import sys
# sys.path.insert(0, "/var/www/hazelremmen")

# from app import application

from jinja2 import Environment, FileSystemLoader
from random import random

env = Environment(
    loader=FileSystemLoader('/var/www/hazelremmen/templates'),
    auto_reload=True
)

def application(environ, start_response):
    template = env.get_template("index.html.j2")

    html = template.render(
        random_num=random()
    )

    start_response("200 OK", [("Content-Type", "text/html")])
    return [html.encode("utf-8")]