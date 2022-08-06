while True:
    days = 1
    start_km = float(input("Type count of start kilometers(>0): "))
    finish_km = float(input("Type count of finish kilometers(>start): "))
    if start_km <= 0 or finish_km < 0:
        print("Results must be more than 0!!!")
    else:
        while start_km < finish_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Sportsmen reached result for {days} days")
        break