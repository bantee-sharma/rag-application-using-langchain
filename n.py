

class Car:
    def func(self,a,b):
        a = self.a
        b = self.b
        return a*b
    
c = Car()
print(c.func(3,5))