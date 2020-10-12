"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __init__(self, name, flavor, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.qty = 0

        self.cache[self.name] = self

    def add_stock(self, amount):
        self.qty = amount

    def sell(self, amount):
        if self.qty == 0:
            print('Sorry, these cupcakes are sold out')
        else:
            if not self.qty <= amount:
                self.qty = self.qty - amount
            else:
                self.qty = 0

    @staticmethod
    def scale_recipe(ingredients, amount):
        list_of_new_ingredients = []
        for ingredient, qty in ingredients:
            new_qty = qty * amount 
            list_of_new_ingredients.append((ingredient, new_qty))
        return list_of_new_ingredients

    @classmethod
    def get(cls, name):
        if name in cls.cache:
            return cls.cache[name]
        else:
            print("Sorry, that cupcake doesn't exist")

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

class Brownie(Cupcake):
    def __init__(self, name, price):
        super().__init__(name, "chocolate", price)



if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
