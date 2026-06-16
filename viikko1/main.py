import task1
import task2
import task3
import task4
import task5

def main():
    while True:
        print("\n=== WEEK 1 PYTHON PROJECT ===")
        print("1. Data types")
        print("2. Celsius to Fahrenheit")
        print("3. Triangle area")
        print("4. Calculator")
        print("5. Array task")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task1.run()

        elif choice == "2":
            task2.run()

        elif choice == "3":
            task3.run()

        elif choice == "4":
            task4.run()

        elif choice == "5":
            task5.run()

        elif choice == "0":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()