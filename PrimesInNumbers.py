def isPrimeNumber(number):
    i = 2
    while i < number and number%i != 0:
        i += 1
    
    return i == number

def nextPrimeNumber(primeNumber):
    while not isPrimeNumber(primeNumber + 1):
        primeNumber += 1
    return primeNumber + 1

def prime_factors(n):
    factorsList = []
    primeNumber = 2

    if not isPrimeNumber(n):
        while  n!= 1:
            if n%primeNumber != 0:
                primeNumber = nextPrimeNumber(primeNumber)
            else:
                factorsList.append(primeNumber)
                n /= primeNumber

        result = ""

        i = 0

        while i < len(factorsList):
            count = factorsList.count(factorsList[i])
            if count == 1:
                result += "(" + str(factorsList[i]) + ")"
            else:
                result += "(" + str(factorsList[i]) + "**" + str(count) + ")"
            i += count
            count = 0
            

        return result
    
    return "(" + str(n) +")"

print(prime_factors(933555431))


#This kata is not finished yet
#Kata link: https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"