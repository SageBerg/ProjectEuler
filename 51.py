# generate primes no larger than n 
def sieve_of_eratosthenes(n):
    primes = set() 
    composites = set() 
    for i in range(2, n):
        if i not in composites:
            primes.add(i)
            j = i ** 2
            while j < n:
                composites.add(j) 
                j += i
    return primes

def main():
    n = 10 ** 6 # takes about 2 seconds for 10 ** 7
    primes = sorted(list(sieve_of_eratosthenes(n)))

    print primes[-1]

if __name__ == "__main__":
    main()
