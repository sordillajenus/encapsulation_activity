class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        
        return self.__age
    
def test():
    pet = Pet()

    print("Enter Pet Details")

    name = input("Pet name: ")
    animal_type = input("Animal type (Dog/Cat/Bird): ")
    age = int(input("Pet age: "))


    pet.set_name(name)
    pet.set_animal_type(animal_type)
    pet.set_age(age)

    
    print("\nPet Information")
    print("Name:", pet.get_name())
    print("Type:", pet.get_animal_type())
    print("Age:", pet.get_age())


test()


