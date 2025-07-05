

class Student:
    def __init__(self,name,place):
        self.name = name
        self.place = place

s = Student("Bantee","Jewar")
print(s.name)
print(s.place)

class School(Student):
    def __init__(self, scl_name):
        self.scl_name = scl_name

scl = School()

print(scl.name)




# class Student:
#     def func(self,name,place):
#         self.name = name
#         self.place = place
#         return name,place

# s = Student()
# print(s.func("Bantee","jewar"))



# class Student:
#     @staticmethod
#     def func(name,place):
#         return name,place

# s = Student()
# print(s.func("Bantee","jewar"))