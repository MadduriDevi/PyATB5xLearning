# User Defined
# 1. The can't return -> non return
# 2.They can return something
# 3.They have parameters
# 4. They don't parameters / arguments
import math


# 1. The can't return -> non return
# No Return Type and No Parameter / Argument - NRNP
def greet():
    print("Hello")


greet()


# 2 .# No Return type and with argument/parameter

def greet_by_name(name):
    print("Hello,", name)


greet_by_name("Devi")


# 3. No Return Type and with Default Argument ( # positional argument)
def say_hello_default_arg(name="Devi"):
    print("Hello", name.upper())


say_hello_default_arg("Madduri")
say_hello_default_arg()


def multiple_args(name1="A", name2="B"):
    print("Mul -> ", name1, name2)


multiple_args()
multiple_args("Reyansh")
multiple_args(name1="Devi")
multiple_args(name1="Devi", name2="praveen")




# 4. Argument + return Type
def sum_of_two(a, b):
    return  a + b

result = sum_of_two(a=4, b=56)
print(result)

def sum_of_two_default(num1 = 100, num2 = 200):
    print ("I will sum the two numbers!")
    return num1 + num2
result = sum_of_two_default (num1= 34, num2 = 45)
print (result)
result = sum_of_two_default ()
print (result)