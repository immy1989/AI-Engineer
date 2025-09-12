# Given list of first ten prime numbers
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Extract the middle five primes
middle_five = prime_numbers[2:7]

# Get every second prime
every_second = prime_numbers[::2]

# Use negative indexing for last three primes
last_three = prime_numbers[-3:]

# Reverse the list
reversed_primes = prime_numbers[::-1]

# Descending Order
descending_order = sorted(prime_numbers, reverse=True)

# Print results
print("Original List:", prime_numbers)
print("Middle Five Primes:", middle_five)
print("Every Second Prime:", every_second)
print("Last Three Primes:", last_three)
print("Reversed List:", reversed_primes)
print("Descending Order:", descending_order)
