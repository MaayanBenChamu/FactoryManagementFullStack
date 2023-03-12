from pymongo import MongoClient
from bson import ObjectId

class Department_DB:
    def __init__(self):
        self.__Client = MongoClient('localhost',27017)
        self.__DB = self.__Client['Factory_Management_DB']
        self.__Department_Coll = self.__DB['Department']

# GET:
    def get_all_department(self):
        departments = list( self.__Department_Coll.find({}) )
        return departments

    def get_one_department(self,id):
        department = self.__Department_Coll.find_one({"_id":ObjectId(id)})
        return department

# PUT:
    def update_department(self, id, obj):
        self.__Department_Coll.update_one({"_id": ObjectId(id)}, {"$set" : obj})
        return "The department has been updated successfully"

# POST:
    def add_department(self, obj):
        self.__Department_Coll.insert_one(obj)
        return "The department has been added successfully"

# DELETE:
    def delete_department(self, id):
        self.__Department_Coll.delete_one({"_id" : ObjectId(id)})
        return "The department has been deleted"


# Department = Department_DB()
# print(Department.get_all_department())
