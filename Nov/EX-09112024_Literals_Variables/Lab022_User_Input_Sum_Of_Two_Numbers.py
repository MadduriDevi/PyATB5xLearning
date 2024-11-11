# Write a program to take the 2 user  input
# then sum the number
# mul -> *
# div -> /

# Logic Building
# Step 1
# I/P -> num1 , num2 -> int
# O/P -> sum - int,sub - int, div -float
num1 = int(input("Enter the num 1"))
num2 = int (input("Enter the num 2"))

#num1 = int(num1) ----> first method
#num2 = int(num2)

print (type(num1))
print (type(num2))

# Step-2/ Rough Logic
# sum + , -, / , *

# str -> int

# step-3
Sum = num1 + num2
Sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum is ->", Sum)
print("Sub is ->", Sub)
print("Mul is ->", mul)
print("Div  is ->", div)

#num1 -> 155
#num2 -> 5
