number = int(input('enter your number : '))
def divisible_by_3and5(number):
    result = []
    for i in range(1,number):
        if i%3==0 and i%5==0:
            result.append(i)
    return result
result=divisible_by_3and5(number)
print(result)