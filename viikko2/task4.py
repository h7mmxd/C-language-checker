def run():
    print("\nTASK 4")
    total = float(input("Enter monthly purchases: "))
    if total < 100:
        discount = 10
    elif total < 300:
        discount = 15
    elif total < 500:
        discount = 20
    else:
        discount = 25

    final = total * (1 - discount / 100)

    print(f"Olet ostanut {total}€ ja saat {discount}% alennusta.")
    print(f"Lopullinen summa on {final:.2f}€")

    if final <= total:
        print("✔ Calculation correct")