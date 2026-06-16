def run():
    print("\nTASK 6")
    while True:
        print("\nMENU")
        print("1. Square perimeter")
        print("2. Circle perimeter")
        print("9. Exit")
        choice = input("Choose: ")

        if choice == "1":
            print("Valittu Neliön kehän pituus")

        elif choice == "2":
            print("Valittu Ympyrän kehän pituus")

        elif choice == "9":
            print("Exiting...")
            break

        else:
            print("Invalid choice")