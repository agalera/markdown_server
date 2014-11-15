import markdown
from bottle import default_app, route, run, get, request, redirect, error
import sys
import os

@get('/')
def index():
    redirect('/index.md')

@get('<path:path>')
def convert_md_to_html(path):
    try:
        with open(os.path.join('files', *path.split('/')), 'r') as md:
            return markdown.markdown(md.read())
    except:
        index()

if __name__ == "__main__":
    run(server='gunicorn',
        host=sys.argv[1],
        port=int(sys.argv[2]),
        workers=int(sys.argv[3]),
        worker_class='gevent',
        debug=bool(sys.argv[4]))
app = default_app()