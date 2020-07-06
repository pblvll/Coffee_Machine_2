# our class Ship
class Ship:
    def __init__(self, name, capacity, city):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.city = city

    # the old sail method that you need to rewrite
    def sail(self):
        return print("The {} has sailed for {}!".format(self.name, self.city))


black_pearl = Ship("Black Pearl", 800, input())
black_pearl.sail()
