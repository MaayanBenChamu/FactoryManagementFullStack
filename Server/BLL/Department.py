from DAL.Department import Department_DB

class Department_BLL:
    def __init__(self):
        self.__department_db = Department_DB()
    
    def get_all_department(self):
        department = self.__department_db.get_all_department()
        return department

    def get_one_department(self, id):
        department = self.__department_db.get_one_department(id)
        return department

    def update_department(self, id, obj):
        department = {
            "Name": obj["Name"],
            "Manager": obj["Manager"]
        }
        stat = self.__department_db.update_department(id, department)
        return stat

    def add_department(self, obj):
        department = {
            "Name": obj["Name"],
            "Manager": obj["Manager"]
        }

        stat = self.__department_db.add_department(department)
        return stat

    def delete_department(self , id):
       stat = self.__department_db.delete_department(id)
       return stat
