number = int(input('enter how much number you wants to square : '))  # like i want 1 to 10 number squares sum...just put 10
result = 0
for i in range(number+1):
    sqr = i**2
    result = sqr + result
print(result)