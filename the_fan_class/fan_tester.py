from the_fan_class import Fan
from fan_types import *

class TestFan:

    def create_fan(self):
        print("Choose a Fan to Test")
        print("1. Normal")
        print("2. Turbo")
        print("3. Ceiling")
        print("4. Window")
        print("5. Box")
        print("6. Exhaust")
        print("7. Pedestal")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            fan = NormalFan()
        elif choice == 2:
            fan = TurboFan()
        elif choice == 3:
            fan = CeilingFan()
        elif choice == 4:
            fan = WindowFan()
        elif choice == 5:
            fan = BoxFan()
        elif choice == 6:
            fan = ExhaustFan()
        elif choice == 7:
            fan = PedestalFan()
        else:
            print("Invalid choice")
            return None

        return fan


    def run(self):
        print("Create Fan 1")
        fan1 = self.create_fan()

        print("\n=== Create Fan 2 ===")
        fan2 = self.create_fan()

          