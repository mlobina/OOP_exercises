class ChildSmith:
    __SURNAME = "Smith"

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_name(self, value):
        self.__name = value

    def set_gender(self, value):
        self.__gender = value

    def get_surname(self):
        return self.__SURNAME

    def change_surname(self, value):
        self.__SURNAME = value




petr = ChildSmith("Petr", "male")
print(ChildSmith.__dict__)
print(petr.__dict__)
print("___________")
print(petr.get_name())
print(petr.get_gender())
print(petr.get_surname())
print("___________")
petr.set_gender("female")
petr.set_name("Kate")
petr.change_surname("Ruster")
print("___________")
print(ChildSmith.__dict__)
print(petr.__dict__)
print("___________")
print(petr.get_name())
print(petr.get_gender())
print(petr.get_surname())