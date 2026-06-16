import task1
import task2
import task3
import task4
import task5

def main():
    while True:
        print("\n=== WEEK 2 PROJECT ===")
        print("1. Number check (<10)")
        print("2. Larger number")
        print("3. Weekday")
        print("4. Discounts")
        print("5. Grade calculator")
        print("0. Exit")

        choice = input("Choose: ")

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
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()