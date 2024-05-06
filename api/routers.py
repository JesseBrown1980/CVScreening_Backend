from flask import Blueprint, request
from controllers.ScreeningController import process_cv

routers = Blueprint('routers', __name__, url_prefix="/api")

@routers.route("/upload", methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        resume_file = request.files.get('cv')
        job_file = request.files.get('job')
        return process_cv(resume_file, job_file)
    return "false", 400
        