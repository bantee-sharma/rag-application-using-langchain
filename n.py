

# class Car:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         return a*b
    
# c = Car(5,5)
# print(c)


class Car:
    def func(self,a,b):
        self.a = a
        self.b = b
        return a*b
    
c = Car()
print(c.func(5,5))