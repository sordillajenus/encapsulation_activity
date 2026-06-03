class Car:

    def __init__ (self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        self.__fuel = 100

    def accelerate(self):
        if self.__fuel > 0:
            self.__speed += 5
            self.__fuel -= 5
        else:
            print("Out of fuel! Cannot accelerate.")

    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0

    def get_speed(self):
        return self.__speed

    def get_fuel(self):
        return self.__fuel

    def refuel(self):
        self.__fuel = 100