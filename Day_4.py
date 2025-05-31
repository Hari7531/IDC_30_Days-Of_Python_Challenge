 ## Program to list First n Prime Numbers

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    primes = []
    num = 2  # Start checking from 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# To Get first n prime numbers
n = int(input("Enter how many prime numbers you want: "))
prime_list = first_n_primes(n)
print(f"The first {n} prime numbers are:\n{prime_list}")