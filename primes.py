"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from calendar import c


def primes(number_of_primes):
    
    if number_of_primes <= 0:
            raise ValueError()
    elif number_of_primes == 1:
        return [2]
    elif number_of_primes == 2:
        return [2, 3]
    elif number_of_primes == 3:
        return [2,3, 5]
    else:
        list = [2, 3, 5, 7]
        count = 4

        while len(list) < number_of_primes:
            
            if count % 2 != 0 and count % 3 != 0 and count % 5 != 0 and count % 7 != 0:
                list.append(count)
            count += 1

        return list