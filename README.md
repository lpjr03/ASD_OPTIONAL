# Vue2 Repository Mining

## Overview
This project analyzes the evolution of comment percentage in the Vue2 repository over time. The goal is to answer the following questions:

1. How has the percentage of comments in the code changed over time? (Lines of comments / Total lines of code)
2. In what percentage of commits has the comment percentage increased?

### Setup
Clone the Vue2 repository and this analysis repository, placing both on your desktop:

```sh
git clone https://github.com/vuejs/vue.git ~/Desktop/vue
git clone https://github.com/lpjr03/ASD_OPTIONAL.git ~/Desktop/ASD_OPTIONAL
cd ~/Desktop/ASD_OPTIONAL
```

### Running the Analysis
Run the script to process the commit history:

```sh
python3 main.py
```

### Visualizing the Data
After running the analysy, in order to generate a graphical representation of the results, run:

```sh
python3 gui.py
```

This will produce a plot where:
- The x-axis represents commit dates in chronological order.
- The y-axis represents the percentage of comments in each commit.

## Output
The script produces:
- A `stats.txt` file with comment percentage per commit.
- A `result.txt` file summarizing the percentage of commits where comments increased.
- A graphical visualization of how the comment percentage evolved over time.



