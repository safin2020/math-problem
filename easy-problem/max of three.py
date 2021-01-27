try:
    num_one = int(input('enter first number : '))
    num_two = int(input('enter second number : '))
    num_three = int(input('enter third number : '))

    largest = num_one
    if num_two >= num_three :
        print('largest value is :  ', num_two)
    elif num_three >= num_two :
        print('largest value is :  ', num_three)
    else:
        print('largest value is : ' , num_one)
except:
    print('please enter number')