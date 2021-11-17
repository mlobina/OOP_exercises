class ChildSmith:
    __SURNAME = "Smith"

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def __get_name(self):
        return self.__name

    def __get_gender(self):
        return self.__gender

    def __set_name(self, value):
        self.__name = value

    def __set_gender(self, value):
        self.__gender = value

    def __get_surname(self):
        return self.__SURNAME

    def __change_surname(self, value):
        self.__SURNAME = value

    name = property(fget=__get_name, fset=__set_name)
    gender = property(fget=__get_gender, fset=__set_gender)
    surname = property(fget=__get_surname, fset=__change_surname)


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