def run():
    print("\nTASK 2")
    name = input("Enter name: ")
    times = int(input("How many times: "))

    print("\nWHILE loop:")
    i = 0
    while i < times:
        print(name)
        i += 1

    print("\nFOR loop:")
    for i in range(times):
        print(name)

    print("\n✔ Task completed")