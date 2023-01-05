# imports

from flask import Flask
from blueprints.index.views import index_blueprint
from blueprints.bookmarks.views import bookmarks_blueprint
from blueprints.post.views import post_blueprint
from blueprints.api.views import api_blueprint

# creating instance flak

app = Flask('__name__')

app.config['JSON_AS_ASCII'] = False


# interception errors
@app.errorhandler(404)
def internal_server_error(e):
    return "<h1>404</h1>", 404


@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500</h1>", 500


# registers blueprints

app.register_blueprint(index_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(api_blueprint)

if __name__ == "__main__":
    app.run(debug=True)