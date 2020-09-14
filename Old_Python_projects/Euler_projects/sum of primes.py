
def fast_nth_prime(n, limit=2000000):
    if limit % 2 != 0: limit += 1
    primes = [True] * limit
    primes[0], primes[1] = [None] * 2
    count = 0  # how many primes have we found?
    for ind, val in enumerate(primes):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
            count += 1
        if count == n: return ind
    return primes
def sumprimes(list):
    output=0
    for ind, val in enumerate(list):
        if val == True:
            output+=ind
    return output
print(sumprimes(fast_nth_prime(2e6)))


