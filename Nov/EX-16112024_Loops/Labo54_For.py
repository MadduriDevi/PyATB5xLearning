for i in range(0, 10):  # 0 to 9, times -> 10
    if i == 5:
        print("Five")
    else:
        print(i)


# |i| condition | o/p
# |0| 0 == 5 -> false | o/p = 0
# |1| 1== 5 -> false | o/p = 1
# |2| 2 == 5 -> false | o/p = 2
# |3| 3 == 5 -> false | o/p = 3
# |4| 4 == 5 -> false | o/p = 4
# |5| 5 == 5 -> true | o/p = Five
# |6| 6 == 5 -> false | o/p = 6
# |7| 7 == 5 -> false | o/p = 7
# |8| 8 == 5 -> false | o/p = 8
# |9| 9 == 5 -> false | o/p = 9
# |10| 10 == 5 -> false | for loop finished  - o/p = Exit
