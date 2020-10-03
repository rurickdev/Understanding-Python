
numbers_quantity = 5
fibonacci_numbers = []

"""
Solution with empty list at start using ifs to check the first two values
"""

for number in range(0,numbers_quantity):
  if(len(fibonacci_numbers) == 0):
    fibonacci_numbers.append(0)
    continue
  if(len(fibonacci_numbers) == 1):
    fibonacci_numbers.append(1)
    continue
  fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])

print(fibonacci_numbers)



"""
Solution with the first two numbers already on the list
"""

numbers_quantity = 5
fibonacci_numbers = [0, 1]

for number in range(2,numbers_quantity):
  fibonacci_numbers.append(fibonacci_numbers[-2] + fibonacci_numbers[-1])

print(fibonacci_numbers)
