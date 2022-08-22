My_list = [9, 8, 7, 7, 7, 5, 3, 3, 3, 3, 2, 1]
new_number = ""

while new_number != "q":
    i = 0
    new_number = input("enter a new rating element in the form of a natural number.\nto exit - q\n")

    if new_number.isdigit():
        for n in My_list:
            if int(new_number) <= n:
                i += 1
            else:
                break
        My_list.insert(i, int(new_number))
    print(My_list)
