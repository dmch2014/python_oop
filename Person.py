class Person:
    description= 'General human'

    def __init__(self, name , age):
        self.name = name
        self.age = age

    def speak(self):
        return "My name is {} i am {} years old".format(self.name, self.age)

    def eat(self, food):
        return "{} like eating {}".format(self.name,food)

    def action(self):
        return "{} spins high".format(self.name)

class Baby(Person):
    #overriding descrption attribute
    description = "Baby"

    def speak(self):
        return "ba ba ba ba ba ba ba"

    def nap(self):
        return "{} takes a nap".format(self.name)


person = Person("Desire", 41)
print(person.description)
print(person.speak())
print(person.eat("Ravioli"))
print(person.action())
print("-------------------")
baby= Baby("Alessia", 1)
print(baby.description)
print(baby.nap())
print(baby.speak())
print(baby.action())
