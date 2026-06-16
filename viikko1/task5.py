def run():
    print("\nTASK 5: Array")

    table = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    a = table[0][2]
    b = table[1][1]
    c = table[2][0]

    print("1st:", a)
    print("2nd:", b)
    print("3rd:", c)

    if a == 3 and b == 5 and c == 7:
        print("✔ Correct indexing")
    else:
        print("✘ Index error")