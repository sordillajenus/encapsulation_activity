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


def test():
    car = Car(2024, "Mustang")

    print("Car Testing")

    for i in range(25):
        car.accelerate()
        print(f"Speed: {car.get_speed()} | Fuel: {car.get_fuel()}")

    print("\nRefueling car")
    car.refuel()

    print(f"Fuel after refill: {car.get_fuel()}")


test()