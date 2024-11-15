#write a program to take a user age and
#let him know if he can go the club
# 21

# Logic Building formula

#step-1
#user input i/p -> data type ->int
#o/p -> string -> user if he can go or not


# step  2 Rough logic (brute force)
# age >21 -> print  can go
# age <21 -> print can't go

#step -3 Write the logic

age = int(input("Enter your age\n"))
if age <21:
    print("Can go the club")
else:
    print("Can't go to the club)")

#step -4 check for the edge cases
# we should consider the age cases such as :
#Negative ages or extremely high values -> program will break
#Non-numeric input -ABC
#Age which is valid


#step -5 optimize the code
# Handle all the edges



