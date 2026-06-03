from the_fan_class import Fan

class NormalFan(Fan):
    def sound(self):
        return ".... */silent"
    
class TurboFan(Fan):
    def sound(self):
        return "WHOOOOOSH!!!"
    
class CeilingFan(Fan):
    def sound(self):
        return "Whoosh!"
    
class WindowFan(Fan):
    def sound(self):
        return "Brrrrrr!"
    
class BoxFan(Fan):
    def sound(self):
        return "Frrrrrr!"
    
class ExhaustFan(Fan):
    def sound(self):
        return "Rrrrrrrr!"
    
class PedestalFan(Fan):
    def sound(self):
        return "Whirrrrrr!"
