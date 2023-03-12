from flask import Blueprint , jsonify, request
from BLL.Department import Department_BLL


department = Blueprint("department " , __name__)

department_bll = Department_BLL()

# [GET]
@department.route("/" , methods=["GET"])
def get_all_department():
    allDepartment = department_bll.get_all_department()
    return jsonify(allDepartment)

@department.route("/<id>" , methods=["GET"])
def get_one_department(id):
    department = department_bll.get_one_department(id)
    return jsonify(department)

# [PUT]
@department.route("/<id>" , methods=["PUT"])
def update_department(id):
    obj = request.json
    stat = department_bll.update_department(id , obj)
    return jsonify(stat)

# [POST]
@department.route("/" , methods=["POST"])
def add_department():
    obj = request.json
    stat = department_bll.add_department(obj)
    return jsonify(stat)


# [DELETE]
@department.route("<id>" , methods=["DELETE"])
def delete_department(id):
    stat = department_bll.delete_department(id)
    return jsonify(stat)
