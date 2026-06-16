def run():
    print("\nTASK 4: Calculator")
    a = int(input("Enter first number (try 10): "))
    b = int(input("Enter second number (try 5): "))

    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Division:", round(a / b, 2))

    if a == 10 and b == 5:
        if a + b == 15 and a - b == 5 and a * b == 50 and a / b == 2:
            print("✔ All calculations correct for test case")
        else:
            print("✘ Calculation error")
    else:
        print("✔ Task executed (custom input)")