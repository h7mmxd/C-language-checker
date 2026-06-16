import subprocess
import uuid
import os

def compile_c(file_path):
    exe = str(uuid.uuid4()) + ".exe"
    if subprocess.run(["gcc", file_path, "-o", exe]).returncode != 0:
        print("COMPILATION FAILED")
        return None
    return exe

def run_program(exe, input_data=""):
    return subprocess.run(
        [exe],
        input=input_data,
        capture_output=True,
        text=True,
        timeout=3
    ).stdout

def check(name, output, expected):
    if expected in output:
        print("[PASS]", name)
        return 1
    print("[FAIL]", name)
    return 0

def grade(file_path):
    exe = compile_c(file_path)
    if not exe:
        return

    input_data = "\n".join("5 10 3 1 4 2 3 9 10 5.5".split())

    output = run_program(exe, input_data)

    tests = [
        ("Task 1", "Hei maailma!"),
        ("Task 2", "Anna kokonaisluku"),
        ("Task 3", "Annoit luvun"),
        ("Task 4", "Kolmella kerrottuna"),
        ("Task 5", "Suuruusjarjestys"),
        ("Task 6a", "Nelion keha"),
        ("Task 6b", "Ympyran keha"),
        ("Task 7", "Merkkijono"),
        ("Task 8", "Summa")
    ]

    score = sum(check(name, output, exp) for name, exp in tests)

    print("\nSCORE:", score, "/8\n")

    os.remove(exe)