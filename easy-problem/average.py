# i use try function because if someone put  string than show error
try:
    length = int(input('enter how much number for avarege : '))  #how many number you wanst to average
except:
    print('wrong keyword')
sum = 0
for i in range(length):
    try:
        number = int(input('enter your number  :  ' ))
        sum =sum + number 
    except:
        print('wrong keyword')


average = sum / length
print('average value is : '  , average)