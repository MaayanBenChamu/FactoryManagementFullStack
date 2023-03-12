from pymongo import MongoClient
from bson import ObjectId

class Employee_DB:
    def __init__(self):
        self.__Client = MongoClient('localhost',27017)
        self.__DB = self.__Client['Factory_Management_DB']
        self.__Employee_Coll = self.__DB['Employee']

# GET:
    def get_all_employees(self):
        employees = list( self.__Employee_Coll.find({}) )
        return employees

    def get_one_employee(self,id):
        employee = self.__Employee_Coll.find_one({"_id":ObjectId(id)})
        return employee

    def get_by_department_id(self,id):
        employees = list(  self.__Employee_Coll.find({"DepartmentID":id}) )
        return employees

# PUT:
    def update_employee(self, id, obj):
        self.__Employee_Coll.update_one({"_id": ObjectId(id)}, {"$set" : obj})
        return "The Employee has been updated successfully"

# POST:
    def add_employee(self, obj):
        self.__Employee_Coll.insert_one(obj)
        return "The Employee has been added successfully"

# DELETE:
    def delete_employee(self, id):
        self.__Employee_Coll.delete_one({"_id" : ObjectId(id)})
        return "The Employee has been deleted"


# Employee = Employee_DB()
# print(Employee.get_all_employees())
