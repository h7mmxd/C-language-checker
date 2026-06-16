import os
from checker import grade

folder = os.path.join(os.path.dirname(__file__), "submissions")

for file in os.listdir(folder):
    if file.endswith(".c"):
        grade(os.path.join(folder, file))