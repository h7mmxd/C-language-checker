import task1
import task2
import task3
import task4
import task5
import task6

def main():
    while True:
        print("\n=== WEEK 3 PROJECT (LOOPS) ===")
        print("1. Print 100 (vertical & horizontal)")
        print("2. Name printing (loops)")
        print("3. Password check")
        print("4. Multiplication table")
        print("5. Sum of even numbers")
        print("6. Menu system")
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
        elif choice == "6":
            task6.run()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()