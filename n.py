class Car():
    def __init__(self,brand,color):
        self.brand_name = brand
        self.color_name = color


c = Car("BMW","Black")
# print(c.brand_name)
# print(c.color_name)

class Specs(Car):
    def __init__(self, brand, color,gear, seat, dash_cam):
        super().__init__(brand, color)
        self.gear = gear
        self.seat = seat
        self.dash_cam = dash_cam
    
s = Specs("BMW","Black",6,5,"Yes")
print(s.brand_name)
print(s.dash_cam)
print(s.color_name)
print(s.gear)
print(s.seat)
        