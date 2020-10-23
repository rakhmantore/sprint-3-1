import random


class Product():
    def __init__(self, name=None, price=10, weight=20,
                 flammability=0.5, identifier=None):
        self.name = name if name is not None else ""
        self.price = price
        self.weight = weight
        self.flammability = flammability
        if identifier is not None:
            self.identifier = identifier
        else:
            self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        stlbt = self.price / self.weight

        if stlbt < 0.5:
            return "Not so stealable..."
        elif stlbt >= 0.5 and stlbt < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        expl = self.flammability * self.weight

        if expl < 10:
            return "...fizzle."
        elif expl >= 10 and expl < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    def __init__(self, name=None, price=10, weight=10,
                 flammability=0.5, identifier=None):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
