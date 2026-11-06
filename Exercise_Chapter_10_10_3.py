from pathlib import Path

path = Path('Exercise_Chapter_10_10_1.txt')
contents = path.read_text(encoding='utf-8')

for line in contents.splitlines():
    print(line)