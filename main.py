def printFirstNNumbers(n):
    for i in range(n + 1):
        primeNumber = False
        if i > 1:
            for a in range(i):
                if a > 1:
                    if i / a == i // a:
                        primeNumber = False
                        break
                primeNumber = True
        if primeNumber:
            print(i)
        else:
            continue
printFirstNNumbers(9)

