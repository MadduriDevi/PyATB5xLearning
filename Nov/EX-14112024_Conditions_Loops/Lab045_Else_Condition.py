# problem to find the max between two
# Logic Building formula

#step-1
#user input i/p -> two integers
#o/p -> int 1 which ever is greater max number it will return
# 31.4 or 45.34 - float

num1 = float(input("Enter the num 1 \n"))
num2 = float (input("Enter the num 2 \n"))
if num1 > num2 :
    print ("Max is" ,num1 )
else :
    print("Max is", num2)

    # Edge cases - num1 == num2 -> Handled
    # String -> ABC , ten -> try and except - we will learn this in future
    # -ve value -> we will learn in future

