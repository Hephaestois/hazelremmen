from jinja2 import Environment, FileSystemLoader
from random import random

env = Environment(
    loader=FileSystemLoader('/var/www/hazelremmen/templates/'),
    auto_reload=True
)

def application(environ, start_response):
    template = env.get_template("base.html")

    html = template.render(
        random_num=random(),
        main_content="blog"
    )

    start_response("200 OK", [("Content-Type", "text/html")])
    return [html.encode("utf-8")]
