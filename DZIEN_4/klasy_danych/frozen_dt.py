from dataclasses import dataclass

@dataclass(order=True,frozen=True)
class Point:
    x: int
    y: int

    def lenght(self):
        return (self.x**2 + self.y**2)**0.5
    
    # def set_x(self,nx):
    #     self.x = nx

p1 = Point(3,4)
p2 = Point(2,12)

print(p1.lenght())
print(p2.lenght())
print(p1>p2)
