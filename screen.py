n = int(input("enter your input"))
def is_prime(n):
    if n<1:
        return False
    else:
        for i in range(len(2,int(n**.05)+1)):
            if n%i == 0:
                return True
        else:
            return True
print(is_prime(n))