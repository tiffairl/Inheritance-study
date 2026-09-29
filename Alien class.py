class Alien:
   def __init__(self, name):
     self.name = name

   def speak(self): 
     print(self.name)

class Namekian(Alien):
    pass

a1 = Namekian("Piccolo")

a1.speak()


