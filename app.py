from flask import Flask
from flask_cors import CORS
from api.routers import routers
from controllers.ScreeningController import process_cv
app = Flask(__name__)
CORS(app)
app.register_blueprint(routers)

if __name__ == '__main__':
    app.run()