def run():
    print("\nTASK 1: Data Types")
    age = 20
    price = 5.5
    letter = "A"

    print("int:", age)
    print("float:", price)
    print("char:", letter)

    if type(age) == int and type(price) == float and type(letter) == str:
        print("✔ TASK 1 executed correctly")
    else:
        print("✘ TASK 1 error")