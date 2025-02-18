from git import Repo
from datetime import datetime
import matplotlib.pyplot as plt

repo = Repo("C:/Users/lpjr0/Desktop/vue")

commits = sorted(repo.iter_commits(), key=lambda c: c.committed_date)

commit_dates = [datetime.fromtimestamp(commit.committed_date) for commit in commits]

file_path = "stats.txt"
with open(file_path, "r") as file:
    y_values = [float(line.strip()) for line in file]

plt.figure(figsize=(10, 6))
plt.plot(commit_dates, y_values, marker="o", linestyle="-")
plt.xlabel("Date")
plt.ylabel("Percentage")
plt.title("Percentage Change of Commits during Time")
plt.grid()
plt.tight_layout()
plt.show()
