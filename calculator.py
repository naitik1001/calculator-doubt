print("WELCOME TO THE CALCULATOR ,YOU CAN ADD,SUBTRACT,MULTIPLY OR DIVIDE")

number1 = int(input("please write the number 1"))
number2 = int(input("please write the number 2"))
print("the first number is - "+number1)
print("the second number is - "+number2)
operation = input("please chooste the operation - '1' for addition, '2 'for subtraction ,'3' for multiplication , '4' for division")
if operation==1:
    print(number1+number2)
elif operation==2:
    question2 = int(input("please write '1'if you want to subtract number 1 - number 2 ,please write '2' if you want to subtract number 2 - number1"))
    if question2==1:
        print(number1 - number2)
    elif question2==2:
        print(number2-number1)
    else:
        print("there is a error please try running the program again")
elif operation==3:
    print(number1*number2)
elif operation==4:
    question4 = int(input("please write '1' if you want to divide number1 /number 2 ,please write '2 ' if you want to divide number2/number1")) 
    if question4==1:
        print(number1/number2)
    elif question4==2:
        print(number2/number1)
    else:
        print("an error occured,please restart the program")
else:
    print("an error occured please restart the program")
print("Thank you for using calculator")