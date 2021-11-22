print("Input how many prime numbers you would like to print")
n = int(input())
primeNumbers = []
i = 2
while len(primeNumbers) < n:
    primeNumber = True
    for a in range(2,i-1):
        if i / a == i // a:
            primeNumber = False
            break
    if primeNumber:
        primeNumbers.append(i)
    i+=1
print(primeNumbers)
