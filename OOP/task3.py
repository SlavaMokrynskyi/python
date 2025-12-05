class Airplane:
    def __init__(self,name,type, passengers):
        self.name = name
        self.type = type.upper()
        self.passengers = passengers

    def show(self):
        print(f"Name : {self.name},\n type : {self.type},\n passengers : {self.passengers}")

    # <=
    def __le__(self, other):
        return self.passengers <= other.passengers
    # <
    def __lt__(self, other):
        return self.passengers < other.passengers
    # >=
    def __ge__(self, other):
        return self.passengers >= other.passengers
    # >
    def __gt__(self, other):
        return self.passengers > other.passengers
    # ==
    def __eq__(self, other):
        return self.type == other.type

     # +
    def __add__(self,value):
        passengers = self.passengers + value
        return Airplane(self.name,self.type,passengers)
    
    # -
    def __sub__(self,value):
        if(value > self.passengers):
            raise ValueError("value must be lower than number of passengers")
        passengers = self.passengers - value
        return Airplane(self.name,self.type,passengers)
    
    # +=
    def __iadd__(self, value):
        self.passengers += value
        return self
    
    # -=
    def __isub__(self, value):
        if value > self.passengers:
            raise ValueError("Value must be lower than number of passengers")
        
        self.passengers -= value
        return self
    
a1 = Airplane("Boeing", "passenger", 180)
a2 = Airplane("Airbus", "cargo", 100)

a1.show()
a2.show()

print(a1 < a2)
print(a1 <= a2)
print(a1 > a2)
print(a1 >= a2)
print(a1 == a2)
print(a1 == Airplane("Boeing", "passenger", 200))

a3 = a1 + 20
a3.show()

a4 = a2 - 30
a4.show()

a1 += 10
a1.show()

a2 -= 50
a2.show()
