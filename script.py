import os, re
import subprocess
from Stat import Stat

# Imposta il percorso della directory del repository Git
REPO_PATH = "C:/Users/lpjr0/Desktop/vue/"

def get_code_stats(commit_hash):
    # Checkout specific commit nella directory specificata
    subprocess.run(
        ["git", "checkout", commit_hash],
        check=True,
        cwd=REPO_PATH,  # Directory del repository
    )
    total_comments = 0
    total_lines = 0
    inside_multi_line_comment = False

    for root, _, files in os.walk(REPO_PATH):
        for FILE in files:
            if FILE.endswith((".js", ".ts")):
                with open(os.path.join(root, FILE), 'r', encoding="utf-8") as file:
                    lines = file.readlines()
                    for line in lines:
                        line = re.sub(r'".*?"', '', line)  # Rimuove le stringhe tra virgolette doppie
                        line = re.sub(r"'.*?'", '', line)  # Rimuove le stringhe tra virgolette singole
                        total_lines += 1
                        line = line.strip()
                        if "//" in line:
                            total_comments += 1
                        if "/*" in line:
                            inside_multi_line_comment = True
                            total_comments += 1
                        elif "*/" in line:
                            inside_multi_line_comment = False
                            total_comments += 1
                        elif inside_multi_line_comment:
                            total_comments += 1

    stat = Stat(total_comments, total_lines)
    return stat
