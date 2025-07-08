# # n = int(input("enter your input: "))
# def is_prime(n):
#     if n<1:
#         return False
#     else:
#         for i in range(2,int(n**0.5)+1):
#             if n%i == 0:
#                 return False
#     return True

# lst = [1,2,3,4,5,6,7,8,9,10,11]
# def prime(lst):
#     return [i for i in lst if is_prime(i)]
# print(prime(lst))

def func(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*func(n-1)
print(func(10))