# write a program to calculate even and odd

#def find_even_odd(num):
  #  if num%2==0 :
       # print("Even")
#
   # else :
   #     print ("odd")

#find_even_odd(6)

n=  int(input("Enter a num\n"))
check_even_odd = lambda num: "Even" if num %2 ==0 else "odd"
#print (check_even_odd(17))
#print (check_even_odd(10))
print (check_even_odd(n))

