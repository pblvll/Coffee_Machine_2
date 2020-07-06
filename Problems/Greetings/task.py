class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        return print("Hello, I am {}!".format(self.name))


person = Person(input())
person.greet()
