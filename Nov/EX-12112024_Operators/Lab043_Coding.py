# Write a python program to calculate the
# area of a circle given its radius using the formula
# area = ⫪× r^2 (Take pie as 3.14)

# Logic Building Formula

# \\ Step 1 \\
# Figure out the inputs and outputs
# Input -> r -> data type -> float
# pi = 3.14
# power -> Pow or ** -> any
# o/p -> float -area , print area

# \\ Step 2 \\
# rough logic = area = 3.14 * pow(r,2)


# \\ step-3 \\
radius = float(input("Enter the radius of the circle\n"))
print(radius)
area = 3.14 * (radius ** 2)
print("Area of the circle is -> ", area)
print(f"Area of the circle is -> :, {area:.2f}")

# * -> mul
# ** -> power
import math

print(math.pi)
print(math.pow(radius,2))
area = math.pi * math.pow(radius,2)
print("Area of the circle is -> ", area)

print(math.pi)
print(math.pow(2, 2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))