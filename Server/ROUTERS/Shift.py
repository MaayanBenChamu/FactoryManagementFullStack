from flask import Blueprint , jsonify, request
from BLL.Shift import Shift_BLL


shift = Blueprint("shift " , __name__)

shift_bll = Shift_BLL()

# [GET]
@shift.route("/" , methods=["GET"])
def get_all_shift():
    allshift = shift_bll.get_all_shift()
    return jsonify(allshift)

@shift.route("/<id>" , methods=["GET"])
def get_one_shift(id):
    shift = shift_bll.get_one_shift(id)
    return jsonify(shift)

# [PUT]
@shift.route("/<id>" , methods=["PUT"])
def update_shift(id):
    obj = request.json
    stat = shift_bll.update_shift(id , obj)
    return jsonify(stat)

# [POST]
@shift.route("/" , methods=["POST"])
def add_shift():
    obj = request.json
    stat = shift_bll.add_shift(obj)
    return jsonify(stat)


# [DELETE]
@shift.route("<id>" , methods=["DELETE"])
def delete_shift(id):
    stat = shift_bll.delete_shift(id)
    return jsonify(stat)
