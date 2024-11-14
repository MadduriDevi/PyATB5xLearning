# Task
# Take a  2 input from the user
#Print the Quotient and Remainder
# 15 -> num1
# 2 ->  num2
#Q -> 7
# R -> 1

Method 1 :
num1 = int(input("Enter the num 1 :"))
num2 = int (input("Enter the num 2 :"))
div = num1/num2
print("div of the two num: " , div)

q = num1 // num2

print(" quotient  : " , q)
print(type(q))

r = num1 % num2
print("reminder  : " , r)
print(type(r))

Method 2 :
# Method 2

num1 = int(input("Enter the first number(dividend:"))
num2 = int(input("Enter the second number(divisor:"))

quotient = num1 // num2
Remainder = num1 % num2

# divmod()
print(f"Quotient (Q) -> {quotient}")
print(f"Remainder (R) -> {remainder}")
