from string import ascii_letters
class Person:
    S_RUS = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя-'
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, age: int, passport:str, weight: float):
        self.verify_fio(fio)
        self.verify_passport(passport)
        self.__fio = fio.split()
        self.age = age
        self.__passport = passport
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("fio must be a string")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("incorrect fio")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:
            if len(s) < 0:
                raise TypeError("fio must contain at least 1 character")
            if len(s.strip(letters)) != 0:
                raise TypeError("fio must contain only letters and '-'")

    @classmethod
    def verify_age(cls, age):
        if type(age) != int or age < 14 or age > 120:
            raise TypeError("fio must be integer in [14; 120]")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("weight must be a float more than 20")

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("passport should be series")
        passport = passport.split()
        if len(passport) != 2 or len(passport[0]) != 4 or len(passport[1]) != 6:
            raise TypeError("invalid passport type")

        for elem in passport:
            if not elem.isdigit():
                raise TypeError("passport should be numbers")


    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.verify_age(age)
        self.__age = age

    @property
    def passport(self):
        return self.__passport

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


person = Person('Ilia Dybal Sianisovich', 20, '1234 123456', 80.0)
print(person.__dict__)
