import subprocess
import os

BASE = os.path.dirname(__file__)
SUBMISSIONS = os.path.join(BASE, "submissions")

# COMPILE
def compile_code(c_file, exe_file):
    result = subprocess.run(
        ["gcc", c_file, "-o", exe_file],
        capture_output=True,
        text=True
    )
    return result.returncode == 0



# RUNNING PROGRAM WITH TASK ID
def run_task(exe_file, task_id, input_data=""):
    try:
        result = subprocess.run(
            [exe_file, str(task_id)],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=2
        )
        return result.stdout.strip()
    except:
        return None


# SIMPLE CHECK RULES
def check_task(task_id, output):
    if output is None:
        return False

    if task_id == 1:
        return "OK" in output or len(output) > 0

    if task_id == 2:
        return len(output) > 0

    if task_id == 3:
        return "Rivejä" in output or "Sanoja" in output

    if task_id == 4 or task_id == 5:
        return len(output) > 0

    if task_id == 6:
        return "ei löydy" in output.lower() or len(output) > 0

    return False


# MAIN GRADER
def grade_student(student_folder):
    student_path = os.path.join(SUBMISSIONS, student_folder)
    c_file = os.path.join(student_path, f"{student_folder}.c")
    exe_file = os.path.join(student_path, f"{student_folder}.exe")

    print("\nGrading:", student_folder)

    if not compile_code(c_file, exe_file):
        print("Compile FAILED")
        return

    score = 0
    total = 6

    for task_id in range(1, 7):
        output = run_task(exe_file, task_id)

        if check_task(task_id, output):
            print(f"Task {task_id}: PASS")
            score += 1
        else:
            print(f"Task {task_id}: FAIL")

    print("FINAL SCORE:", score, "/", total)


# RUN ALL STUDENTS
def main():
    students = os.listdir(SUBMISSIONS)

    for s in students:
        grade_student(s)


if __name__ == "__main__":
    main()