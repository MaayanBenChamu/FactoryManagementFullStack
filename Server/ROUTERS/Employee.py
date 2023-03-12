from flask import Blueprint , jsonify, request
from BLL.Employee import Employee_BLL


employee = Blueprint("employee " , __name__,  static_folder='static', template_folder='templates')

employee_bll = Employee_BLL()

# [GET]
@employee.route("/" , methods=["GET"])
def get_all_employee():
    allEmployee = employee_bll.get_all_employees()
    return jsonify(allEmployee)

@employee.route("/<id>" , methods=["GET"])
def get_one_employee(id):
    employee = employee_bll.get_one_employee(id)
    return jsonify(employee)

@employee.route("/departmentId/<id>" , methods=["GET"])
def get_by_depart_id(id):
    emploees = employee_bll.get_by_department_id(id)
    return jsonify(emploees)



# [PUT]
@employee.route("/<id>" , methods=["PUT"])
def update_employee(id):
    obj = request.json
    stat = employee_bll.update_employee(id , obj)
    return jsonify(stat)

# [POST]
@employee.route("/" , methods=["POST"])
def add_employee():
    obj = request.json
    stat = employee_bll.add_employee(obj)
    return jsonify(stat)


# [DELETE]
@employee.route("<id>" , methods=["DELETE"])
def delete_employee(id):
    stat = employee_bll.delete_employee(id)
    return jsonify(stat)
