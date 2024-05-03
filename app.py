from flask import Flask
from flask_cors import CORS
from api.routers import routers
app = Flask(__name__)
CORS(app)
app.register_blueprint(routers)

if __name__ == '__main__':
    app.run()