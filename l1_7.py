start_km = float(input("Type count of start kilometers(>0): "))
finish_km = float(input("Type count of finish kilometers(>0): "))
days = 1
while start_km < finish_km:
    start_km += start_km * 0.1
    days += 1
    print(f"Sportsmen reached result for {days} days")
    break