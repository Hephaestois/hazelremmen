from jinja2 import Environment, FileSystemLoader

env = Environment(
    loader=FileSystemLoader('/var/www/hazelremmen'),
)

def application(environ, start_response):
    template = env.get_template('index.html')
    html = template.render(title="Hello World")
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf-8')]