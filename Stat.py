class Stat(object):
    def __init__(self, comment_lines, code_lines):
        self.comment_lines = comment_lines
        self.code_lines = code_lines
        self.perc=((comment_lines/code_lines)*100).__round__(2)

    def __str__(self):
        return f"Percentuale di commenti su linee totali di codice: {self.perc}"