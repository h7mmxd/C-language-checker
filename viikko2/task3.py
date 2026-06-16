def run():
    print("\nTASK 3")
    n = int(input("Weekday number (1-7): "))
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if n in days:
        print(days[n])
        print("✔ Valid weekday")
    else:
        print("Annoit sellaisen numeron, jolle ei ole viikonpäivää")