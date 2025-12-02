def primes(nb_primes):
    if nb_primes > 1000:
        nb_primes = 1000
    
    p = []
    n = 2
    while len(p) < nb_primes:
        for i in p:
            if n % i == 0:
                break
        else:
            p.append(n)
        n += 1
    return p