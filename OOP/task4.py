class Flat:
    def __init__(self, address, area, price):
        self.address = address
        self.area = area
        self.price = price
    
    def show(self):
        print(f"Address: {self.address}, Area: {self.area} m², Price: {self.price}$")

    # ==
    def __eq__(self, other):
        return self.area == other.area

    # !=
    def __ne__(self, other):
        return self.area != other.area

    # <
    def __lt__(self, other):
        return self.price < other.price

    # <=
    def __le__(self, other):
        return self.price <= other.price

    # >
    def __gt__(self, other):
        return self.price > other.price

    # >=
    def __ge__(self, other):
        return self.price >= other.price

f1 = Flat("Main Street 1", 50, 100000)
f2 = Flat("Central Ave 10", 70, 120000)
f3 = Flat("Main Street 5", 50, 90000)

f1.show()
f2.show()
f3.show()

print(f1 == f2)
print(f1 == f3)
print(f1 != f2)
print(f1 != f3)

print(f1 < f2)
print(f2 > f3)
print(f1 <= f3)
print(f2 >= f1)
