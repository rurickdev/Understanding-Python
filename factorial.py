
main_number = 10

print(f'Factorial of {main_number} is')

for number in range(main_number-1,0,-1):
  main_number *= number

print(main_number)
