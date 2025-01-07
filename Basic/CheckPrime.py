# 3. Check Prime Number

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n% i==0:
            return "The given number is not prime"
    return "The given number is prime"
print(is_prime(8)) 


