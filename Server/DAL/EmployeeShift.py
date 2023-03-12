from pymongo import MongoClient
from bson import ObjectId

class Employee_Shift_DB:
    def __init__(self):
        self.__Client = MongoClient('localhost',27017)
        self.__DB = self.__Client['Factory_Management_DB']
        self.__Employee_Shift_Coll = self.__DB['EmployeeShift']

# GET:
    def get_all_employee_shifts(self):
        employee_shift = list( self.__Employee_Shift_Coll.find({}) )
        return employee_shift

    def get_one_employee_shift(self,id):
        employee_shift = self.__Employee_Shift_Coll.find_one({"_id":ObjectId(id)})
        return employee_shift

    def get_shift_by_emploee(self,Eid):
        employee_shift = list( self.__Employee_Shift_Coll.find({"EmployeeID" :Eid }) )
        return employee_shift

    def get_shift_by_shift(self,Sid):
        employee_shift = list( self.__Employee_Shift_Coll.find({"ShiftID" :Sid}) )
        return employee_shift


# PUT:
    def update_employee_shift(self, id, obj):
        self.__Employee_Shift_Coll.update_one({"_id": ObjectId(id)}, {"$set" : obj})
        return "The Employee Shift has been updated successfully"

# POST:
    def add_employee_shift(self, obj):
        self.__Employee_Shift_Coll.insert_one(obj)
        return "The Employee Shift has been added successfully"

# DELETE:
    def delete_employee_shift(self, id):
        self.__Employee_Shift_Coll.delete_one({"_id" : id})
        return "The Employee Shift has been deleted"


    def Delete_by_EmployeeID(self , id):
        self.__Employee_Shift_Coll.delete_many({"EmployeeID":id})
        return "Shift Deleted!"

    def Delete_by_ShiftID(self , id):
        self.__Employee_Shift_Coll.delete_many({"ShiftID":ObjectId(id)})
        return "Purchase Deleted!"





# ES = Employee_Shift_DB()
# print(ES.get_all_employee_shifts())