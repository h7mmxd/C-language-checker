def run():
    print("\nTASK 5")
    student_id = input("ID number: ")
    name = input("Nam: ")

    p1 = float(input("Score 1: "))
    p2 = float(input("Score 2: "))
    p3 = float(input("Score 3: "))

    total = p1 + p2 + p3
    avg = total / 3

    if avg >= 80:
        grade = "Kiitettävä"
    elif avg >= 60:
        grade = "Hyvä"
    elif avg >= 40:
        grade = "Välttävä"
    else:
        grade = "Hylätty"

    print("\nRESULTS")
    print("ID:", student_id)
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Grade:", grade)
    print("✔ Task executed correctly")