def run():
    print("\nTASK 2")
    a = int(input("First number: "))
    b = int(input("Second number: "))

    if a > b:
        bigger = a
    else:
        bigger = b

    print(f"Annoit luvut {a} ja {b}, joista {bigger} on suurempi.")

    if bigger == max(a, b):
        print("✔ Correct")