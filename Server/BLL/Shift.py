from DAL.Shift import Shift_DB

class Shift_BLL:
    def __init__(self):
        self.__shift_db = Shift_DB()
          
    def get_all_shift(self):
        shift = self.__shift_db.get_all_shifts()
        return shift

    def get_one_shift(self, id):
        shift = self.__shift_db.get_one_shift(id)
        return shift

    def update_shift(self, id, obj):
        shift = {
            "Date": obj["Date"],
            "Start": obj["Start"],
            "End": obj["End"]

        }
        stat = self.__shift_db.update_shift(id, shift)
        return stat

    def add_shift(self, obj):
        shift = {
             "Date": obj["Date"],
            "Start": obj["Start"],
            "End": obj["End"]

        }

        stat = self.__shift_db.add_shift(shift)
        return stat

    def delete_shift(self , id):
       stat = self.__shift_db.delete_shift(id)
       return stat
