class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class Scorecard:
    def __init__(self, player, ones, toes, trees, fours):
        self.player = player
        self.ones = ones
        self.toes = toes
        self.trees = trees
        self.forus = fours


Audi = Car("R8", 100000)

Nils = Scorecard("Nils", 0, 0, 6, 0)

print(Audi.model)
print(Audi.price)
print(Nils.ones)
