def isPrime(broj):
    if broj <= 1:
        return False

    for i in range(2, broj):
        if broj % i == 0:
            return False

    return True
def primes_in_range(start, end):
    prosti = []
    for n in range(start, end+1):
        if isPrime(n):
            prosti.append(n)
    return prosti
print(isPrime(7))   
print(isPrime(10))  

print(primes_in_range(1, 10)) 
