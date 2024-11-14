# Task
# Take a 3 input from the user
#Perform the sub,Add,mul,and div

num1 = float(input("Enter the num 1 :"))
num2 = float (input("Enter the num 2 :"))
num3 = float (input("Enter the num 3 :"))

sum = num1 + num2 + num3
sub = num1 - num2 - num3
mul = num1 * num2 * num3
div = (num1 / num2) / num3

print("sum of 3 number: ", sum)
print("sub of 3 number: ", sub)
print("mul of 3 number: ", mul)
print("div of 3 number: ", div)

print(type(sum))
print(type(sub))
print(type(mul))
print(type(div))
