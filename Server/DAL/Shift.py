from pymongo import MongoClient
from bson import ObjectId


class Shift_DB:
    def __init__(self):
        self.__Client = MongoClient('localhost', 27017)
        self.__DB = self.__Client['Factory_Management_DB']
        self.__Shift_Coll = self.__DB['Shift']

# GET:
    def get_all_shifts(self):
        shifts = list(self.__Shift_Coll.find({}))
        return shifts

    def get_one_shift(self, id):
        shift = self.__Shift_Coll.find_one({"_id": ObjectId(id)})
        return shift

# PUT:
    def update_shift(self, id, obj):
        self.__Shift_Coll.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "The Shift has been updated successfully"

# POST:
    def add_shift(self, obj):
        self.__Shift_Coll.insert_one(obj)
        return "The Shift has been added successfully"

# DELETE:
    def delete_shift(self, id):
        self.__Shift_Coll.delete_one({"_id": ObjectId(id)})
        return "The Shift has been deleted"

        
# Shift = Shift_DB()
# print(Shift.get_all_shifts())
