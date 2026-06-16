def run():
    print("\nTASK 5")
    n = int(input("Enter number: "))
    total = 0
    i = 0

    while i <= n:
        if i % 2 == 0:
            total += i
        i += 1

    print("Sum of even numbers:", total)
    print("✔ Task completed")