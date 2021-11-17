class ChildValue:

    def __init__(self, name):
        self.__name = name # наименование свойства

# self - ссылка на экземпляр класса ChildValue
# instance - ссылка на экземпляр класса ChildSmith
# owner - ссылка на класс ChildSmith

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value



class ChildSmith:
    __SURNAME = "Smith"
    # __slots__ = ["__name", "__gender", "__dict__"]
    name = ChildValue("name")
    gender = ChildValue("gender")
    surname = ChildValue("surname")

    def __init__(self, name, gender, surname=__SURNAME):
        self.name = name
        self.gender = gender
        self.surname = surname


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

