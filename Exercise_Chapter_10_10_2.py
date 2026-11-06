from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line)