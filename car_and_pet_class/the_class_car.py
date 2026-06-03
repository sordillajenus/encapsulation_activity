class Car:

    def __init__ (self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__fuel = 100

    def accelerate(self):
        if self.__fuel > 0:
            self.__speed += 5
            self.__fuel -= 2