# Wygeneruj 16-bitową liczbę pierwszą p i sprawdź czy „Twój” numer indeksu jest generatorem grupy . Przygotuj metodę w „Pythonie” lub „Sage” pozwalająca wygenerować ciąg wartości będących kolejnymi potęgami dla kolejnych generatorów.  
# Skomentuj właściwości takiego ciągu w kontekście wykorzystania jako „PRNG” 

import random

def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True


def prime_factors_function(n):
    factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor+= 1

    return factors

def generate_16_bit_prime():
    lower_limit = 2**15
    upper_limit = 2**16 - 1

    while True:
        potential_prime = random.randint(lower_limit, upper_limit)
        if is_prime(potential_prime):
            return prime_factors_function(potential_prime - 1) #rozłożyć na czynniki liczba - 1, rozkładamy na czynniki pierwsze, sprawdzam swój numer indeksu i czy jest jakas jedynka, (numer indeksu ^ p-1) % l.pierwsza p








print(generate_16_bit_prime())




# w drugim sprawzdić gcd i czy jest względnie pierwszy



#yafu
#rozłożyć na czynniki pierwsz es, fi od n, coś tam multipleksowaną