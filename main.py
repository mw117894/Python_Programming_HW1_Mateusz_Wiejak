def printPrimeNumbers(n):
    for i in range(n + 1):
        primeNumber = True
        if i > 1:
            for a in range(i):
                if a > 1:
                    if i / a == i // a:
                        primeNumber = False
                        break
        if primeNumber and i > 1:
            print(i)
