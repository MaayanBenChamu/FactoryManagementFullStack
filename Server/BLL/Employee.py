from DAL.Employee import Employee_DB

class Employee_BLL:
    def __init__(self):
        self.__employee_db = Employee_DB()
# GET:
    def get_all_employees(self):
        employee = self.__employee_db.get_all_employees()
        return employee

    def get_one_employee(self, id):
        employee = self.__employee_db.get_one_employee(id)
        return employee

    def get_by_department_id(self, id):
        employee = self.__employee_db.get_by_department_id(id)
        return employee


# PUT:
    def update_employee(self, id, obj):
        employee = {
            "First_Name": obj["First_Name"],
            "Last_Name": obj["Last_Name"],
            "Start_Work_Year": obj["Start_Work_Year"],
            "DepartmentID": obj["DepartmentID"]
        }
        stat = self.__employee_db.update_employee(id, employee)
        return stat

# POST:
    def add_employee(self, obj):
        employee = {
             "First_Name": obj["First_Name"],
            "Last_Name": obj["Last_Name"],
            "Start_Work_Year": obj["Start_Work_Year"],
            "DepartmentID": obj["DepartmentID"]
        }

        stat = self.__employee_db.add_employee(employee)
        return stat

# DELETE:
    def delete_employee(self , id):
       stat = self.__employee_db.delete_employee(id)
       return stat
