from flask import Flask
from blueprints.index.views import index_blueprint

app = Flask('__name__')


app.register_blueprint(index_blueprint)

if __name__ == "__main__":
    app.run(debug=True)