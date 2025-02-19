# task3

def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

def first_n_primes(n = 10):
    primes = []
    num = 2
    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes

def sum_to_100():
    num = sum(range(1, 101))
    return num
