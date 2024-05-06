from flask import Blueprint, request
from controllers.ScreeningController import process_cv
from flask_cors import cross_origin
routers = Blueprint('routers', __name__, url_prefix="/api")

@routers.route("/upload", methods=['GET', 'POST'])
@cross_origin()
def upload_resume():
    if request.method == 'POST':
        resume_file = request.files.get('cv')
        job_file = request.files.get('job')
        return process_cv(resume_file, job_file)
    return "false", 400

@routers.route("/test", methods=['GET', 'POST'])
def test():
    return "test success"
        