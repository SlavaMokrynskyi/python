class Circle:
    def __init__(self,radius):
        if(radius <= 0):
            raise ValueError("radius must be positive")
        self.radius = radius
        self.len = 2 * radius * 3.14
    
    def show(self):
        print(f"Radius : {self.radius}, Lenght : {self.len}")

    # <=
    def __le__(self, other):
        return self.len <= other.len
    # <
    def __lt__(self, other):
        return self.len < other.len
    # >=
    def __ge__(self, other):
        return self.len >= other.len
    # >
    def __gt__(self, other):
        return self.len > other.len
    # ==
    def __eq__(self, other):
        return self.radius == other.radius
    
    # +
    def __add__(self,value):
        new_radius = self.radius + value
        return Circle(new_radius)
    
    # -
    def __sub__(self,value):
        if(value > self.radius):
            raise ValueError("value must be lower than radius")
        new_radius = self.radius - value
        return Circle(new_radius)
    
    # +=
    def __iadd__(self, value):
        self.radius += value
        self.len = 2 * 3.14 * self.radius
        return self
    
    # -=
    def __isub__(self, value):
        if value > self.radius:
            raise ValueError("Value must be lower than radius")
        
        self.radius -= value
        self.len = 2 * 3.14 * self.radius
        return self
    
c1 = Circle(5)
c2 = Circle(10)

c1.show()
c2.show()

print(c1 < c2)
print(c1 <= c2)
print(c1 > c2)
print(c1 >= c2)
print(c1 == c2)
print(c1 == Circle(5))

c3 = c1 + 3
c3.show()

c4 = c2 - 4
c4.show()

c1 += 2
c1.show()

c2 -= 5
c2.show()