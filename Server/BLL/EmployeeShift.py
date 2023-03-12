from DAL.EmployeeShift import Employee_Shift_DB

class Employee_Shift_BLL:
    def __init__(self):
        self.__employee_shift_db = Employee_Shift_DB()
          
    def get_all_employee_shift(self):
        employee_shift = self.__employee_shift_db.get_all_employee_shifts()
        return employee_shift

    def get_one_employee_shift(self, id):
        employee_shift = self.__employee_shift_db.get_one_employee_shift(id)
        return employee_shift

    def get_by_employee_id(self, id):
        Eshift = self.__employee_shift_db.get_shift_by_emploee(id)
        if(len(Eshift) == 0):
            return "No shifts were found for this employee"
        else:
            return Eshift
 
    def get_by_shift_id(self, id):
        Sshift = self.__employee_shift_db.get_shift_by_shift(id)
        if(len(Sshift) == 0):
            return f"No Shift were found for this Shift: {id}"
        else:
            return Sshift

    def update_employee_shift(self, id, obj):
        employee_shift = {
            "EmployeeID": obj["EmployeeID"],
            "ShiftID": obj["ShiftID"]
        }
        stat = self.__employee_shift_db.update_employee_shift(id, employee_shift)
        return stat

    def add_employee_shift(self, obj):
        employee_shift = {
            "EmployeeID": obj["EmployeeID"],
            "ShiftID": obj["ShiftID"]
        }

        stat = self.__employee_shift_db.add_employee_shift(employee_shift)
        return stat

    def delete_employee_shift(self , id):
       stat = self.__employee_shift_db.delete_employee_shift(id)
       return stat

    def Delete_shift_by_employee(self , id):
       stat = self.__employee_shift_db.Delete_by_EmployeeID(id)
       return stat

    def Delete_shift_by_shift(self , id):
       stat = self.__employee_shift_db.delete_employee_shift(id)
       return stat
        


        

