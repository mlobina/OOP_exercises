class ChildSmith:
    __SURNAME = "Smith"

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def surname(self):
        return self.__SURNAME

    @surname.setter
    def surname(self, value):
        self.__SURNAME = value


petr = ChildSmith("Petr", "male")
print(ChildSmith.__dict__)
print(petr.__dict__)
print("___________")
print(petr.name)
print(petr.gender)
print(petr.surname)
print("___________")
petr.gender = "female"
petr.name  = "Kate"
petr.surname = "Ruster"
print("___________")
print(ChildSmith.__dict__)
print(petr.__dict__)
print("___________")
print(petr.name)
print(petr.gender)
print(petr.surname)