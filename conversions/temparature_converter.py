print('Temperature conversion program')
print(' press 1 for convert from celcius to another \n press 2 for convert from faremhit to another \n press 3 for convert from kelvin to another')

choice = int(input('enter your choice number : '))

if choice >3:
    print('invalid choice optino...please enter from 1 to 3')
# celcius converter
if choice==1:
    temp = float(input('please enter temparature in celcius : '))

    # rounding to 2 decumal places

    farenhit = round((((9/5)*temp)+32),2)
    kelvin = round((temp +273.15),2)

    print('temparature in farenhit is ', farenhit , ' deg F')
    print('temparature in kelvin is ', kelvin , ' deg K')
# farenhit converter
elif choice==2:
    temp = float(input('please enter temparature in farenhit : '))

    # rounding to 2 decumal places

    celcius = round(((5/9)*(temp-32)),2)
    kelvin = round(((temp +459.67)*(5/9)),2)

    print('temparature in farenhit is ', celcius , ' deg C')
    print('temparature in kelvin is ', kelvin , ' deg K')
# kelvin converter
elif choice==3:
    temp = float(input('please enter temparature in kelvin : '))

    # rounding to 2 decumal places

    celcius = round((temp-273.15),2)
    farenhit = round(((temp*(9/5))-459.67),2)

    print('temparature in farenhit is ', celcius , ' deg C')
    print('temparature in kelvin is ', farenhit , ' deg F')