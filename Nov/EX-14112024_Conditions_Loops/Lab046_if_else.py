# problem to find the max between 3 numbers
# Logic Building formula

# step-1
# user input i/p -> num1 , num2 ,num3  -> int
# o/p -> int 1  or string with max number

# Logic  ? If else - 1 condition ,

# syntax
# if condition 1 :
# print ("do 1")
# elif condition 2 :
# print ("do 2")
# elif condition 3 :
# print ("do 3")
# else :
# print (" do for else")
num1 = int(input("Enter the num 1 \n"))   #5, #10
num2 = int(input("Enter the num 2 \n"))   #3, #12
num3 = int(input("Enter the num 3 \n"))   #2, #11

# 5 > 3 and 5 > 2 -> 5
#  num1 > num 2 and num1 > num3 -> num1

# 12 > 10 and 12 > 11 -> true -> 12
#  num2 > num 1 and num2 > num3 -> num2

# num3

if num1 > num2 and num1 > num3:
    print("Max is ", num1)
elif num2 > num1 and num2 > num3:
    print("Max is ", num2)
else :
    print("Max is ", num3)