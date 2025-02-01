from git import Repo
from script import *

repo = Repo("C:/Users/lpjr0/Desktop/vue")

commits = sorted(repo.iter_commits(), key=lambda c: c.committed_date)

stats=[]

for commit in commits:
        stats.append(get_code_stats(commit.hexsha).perc)

with open("stats.txt", "w") as file:
    for stat in stats:
        file.write(str(stat) + "\n")

increased_ratio = 0
for i in range(1, len(stats)):
    if stats[i] > stats[i - 1]:
        increased_ratio += 1

percent_increased = (increased_ratio / len(stats)) * 100

with open("result.txt", "w") as file:
    file.write("La percentuale di commit in cui i commenti sono aumentati è uguale a: " + str(percent_increased))