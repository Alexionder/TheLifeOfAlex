class Sword():
    def __init__(self, durability, strength, name):
        self.durability = durability
        self.strength = strength
        self.name = name

    def inspect(self):
        print "This sword has " + str(self.durability) + " durability and " + str(self.strength) + " strength."

class Axe():
    def __init__(self, durability, strength, name):
        self.durability = durability
        self.strength = strength
        self.name = name

    def inspect(self):
        print "This axe has " + str(self.durability) + " durability and " + str(self.strength) + " strength."

class HPbottle():
    def __init__(self, amount):
        self.amount = amount
        if amount < 15:
            self.name = "weak health potion"
        elif amount < 30:
            self.name = "moderate health potion"
        else:
            self.name = "strong health potion"

    def inspect(self):
        print "This potion can heal you for " + str(self.amount) + "."

class Food():
    def __init__(self, amount, name):
        self.amount = amount
        self.name = name

    def inspect(self):
        print "This food can satisfy you hunger for " + str(self.amount) + "."
