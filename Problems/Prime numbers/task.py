prime_numbers = [number for number in range(2, 1001) if all(number % div for div in range(2, number))]
