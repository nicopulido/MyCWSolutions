def prime_factors(n):
    factors = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    result = ""
    for prime in sorted(factors):
        count = factors[prime]
        if count == 1:
            result += f"({prime})"
        else:
            result += f"({prime}**{count})"
    return result

print(prime_factors(75))

#kata link: https://www.codewars.com/kata/54d512e62a5e54c96200019e