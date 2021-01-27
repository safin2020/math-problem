num = int(input('enter digit : '))
result = 0
for  i in range(len(str(num))):              #123
    digit = num%10
    result = result + digit
    num = num//10
print(result)
