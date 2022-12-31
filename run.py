from flask import Flask
from blueprints.index.views import index_blueprint


app = Flask('__name__')

app.config['JSON_AS_ASCII'] = False
@app.errorhandler(404)
def internal_server_error(e):
    return "<h1>404</h1>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500</h1>", 500



app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run(debug=True)