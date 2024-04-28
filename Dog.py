class Dog:
    #a class atribute
    species= 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #creating an instance method , you have to include the self parameter
    def description(self):
        #return a formatted string with dog name and age
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} speaks {}".format(self.name, sound)

    # dunder methods because they begin and end with double underscores.
    # There are many dunder methods that you can use to customize classes in Python
    def __str__(self):
        return f"{self.name} is {self.age} years old"

#instantiaing the classes, creating objects for 2 dogs

philo= Dog('cagnolino', '4')
print(philo)
mickey= Dog('mickey', '5')

print(philo.description())
print(philo.speak("gua gua"))

print(mickey.description())
print(mickey.speak("wolf wolf"))
