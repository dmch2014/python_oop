class Employee:
   # to  declare which attributes each instance of  the  class should have:
   #A class can have: Instance attributes and class atributes
   #classes attributes are the same for every instance

   company = 'house'

   #init in the function to initialize the class
   #this function is called when the class is instantiated
   #a class can be created empty too, which in this case we will use the reserved word pass
def __init__(self, name, age):
        self.name = name
        self.age = age

