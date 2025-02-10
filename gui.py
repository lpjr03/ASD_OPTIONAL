import numpy as np
from git import Repo
from datetime import datetime
import matplotlib.pyplot as plt

repo = Repo("C:/Users/lpjr0/Desktop/vue")

commits = sorted(repo.iter_commits(), key=lambda c: c.committed_date)
commit_dates = [datetime.fromtimestamp(commit.committed_date) for commit in commits]

comment_lines = []
total_lines = []

comment_lines_file = "output.txt"
with open(comment_lines_file, "r") as file:
    for line in file:
        parts = line.split(",")
        comment_count = int(parts[0].split(":")[1].strip())
        comment_lines.append(comment_count)
        total_count = int(parts[1].split(":")[1].strip())
        total_lines.append(total_count)

plt.figure(figsize=(10, 6))

plt.plot(commit_dates, comment_lines, marker="o", linestyle="-", label="Comment Lines", color="blue")
plt.plot(commit_dates, total_lines, marker="o", linestyle="-", label="Total Lines", color="red")

plt.xlabel("Date")
plt.ylabel("Number of Lines")
plt.title("Comment Lines vs Total Lines Over Time")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
