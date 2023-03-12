from ROUTERS.Department import department
from ROUTERS.Employee import employee
from ROUTERS.Shift import shift
from ROUTERS.EmployeeShift import employee_shift 

from flask import Flask
import json
from bson import ObjectId
from flask_cors import CORS

class JSONEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self,obj)


app = Flask(__name__)

CORS(app ,supports_credentials=True)
app.json_encoder = JSONEncoder

app.register_blueprint(department , url_prefix="/department")
app.register_blueprint(employee , url_prefix="/employee")
app.register_blueprint(shift , url_prefix="/shift")
app.register_blueprint(employee_shift , url_prefix="/employee_shift")

app.run()