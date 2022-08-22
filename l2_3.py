month = int(input("Enter the month of the year, you are interested in, from 1 to 12: "))

month_dic = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August",
             9: "September", 10: "October", 11: "November", 12: "December"}

if month in month_dic:
    print(f"{month} - month of the year is {month_dic[month]}")
else:
    print("Wrong number.")
