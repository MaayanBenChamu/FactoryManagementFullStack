
from flask import Blueprint, jsonify, request
from BLL.EmployeeShift import Employee_Shift_BLL

employee_shift = Blueprint('Employee_Shift', __name__,  static_folder='static', template_folder='templates')



employee_shift_bll = Employee_Shift_BLL()

# Get all:
@employee_shift.route("/" , methods=["GET"])
def get_all_employee_shift():
    employee_shift = employee_shift_bll.get_all_employee_shift()
    return jsonify(employee_shift) 

# Get one by ID;
@employee_shift.route("/<id>" , methods=["GET"])
def get_one_employShift(id):
    employShift = employee_shift_bll.get_one_employee_shift(id)
    return jsonify(employShift)

# Get employee_shift by employee ID:
@employee_shift.route("/employeeId/<id>" , methods=["GET"])
def get_by_employee_id(id):
    employShift = employee_shift_bll.get_by_employee_id(id)
    return jsonify(employShift)

# Get employee_shift by shift ID:
@employee_shift.route("/shiftId/<id>" , methods=["GET"])
def get_by_shift_id(id):
    employShift = employee_shift_bll.get_by_shift_id(id)
    return jsonify(employShift)

# ________________________________________________________________________PUT__
#Update employShift:
@employee_shift.route("/<id>" , methods=["PUT"]) 
def update_employShift(id):
    obj = request.json
    stat = employee_shift_bll.update_employee_shift(id , obj)
    return jsonify(stat)

# ________________________________________________________________________POST___
# Add one:
@employee_shift.route("/" ,methods=["POST"] )
def Add_employShift():
    obj = request.json
    stat = employee_shift_bll.add_employee_shift(obj)
    return jsonify(stat)

# ________________________________________________________________________DELETE__
# DELETE one:
@employee_shift.route("<id>" , methods=["DELETE"])
def DELETE(id):
    stat = employee_shift_bll.delete_employee_shift(id)
    return jsonify(stat)

# DELETE employShift by Employee ID:
@employee_shift.route("/employeeId/<id>" , methods=["DELETE"])
def DELETE_by_Employee(id):
    stat = employee_shift_bll.Delete_shift_by_employee(id)
    return jsonify(stat)

# DELETE employShift by Shift ID:
@employee_shift.route("/shiftId/<id>" , methods=["DELETE"])
def DELETE_by_shift(id):
    stat = employee_shift_bll.Delete_shift_by_employee(id)
    return jsonify(stat)


    
 
