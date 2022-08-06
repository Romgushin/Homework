p = int(input("Type your proceeds(in$): "))
c = int(input("Type your costs(in$): "))
e = int(input("How many employers do you have?: "))
if p > c:
    print("Your company profitable")
    profit = p-c
    efficiency=(profit / p)*100
    print(f"Efficiency - {efficiency:.2f}%")
    inc = profit / e
    print(f"Every employer get increase for {inc:.2f}$")
else:
    print("Your company unprofitable")
