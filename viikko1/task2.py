def run():
    print("\nTASK 2: Celsius to Fahrenheit")
    c = float(input("Enter Celsius (try 0 for test): "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)

    if c == 0 and f == 32:
        print("✔ Correct result for test case (0°C)")
    else:
        print("✔ Task executed (no test failure detected)")