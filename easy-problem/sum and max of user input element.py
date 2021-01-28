
number = int(input('how much number of element you want to sum : '))

lst = []
for i in range(number):
    element = int(input('enter your number : '))   #123
    lst.append(element)


print('sum of element is = ' , sum(lst))
print('max number of element is = ' , max(lst))