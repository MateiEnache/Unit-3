from pathlib import Path
# from pathlib module, import Path class

path = Path("learning_python.txt")
contents = path.read_text()
lines = contents.splitlines()

print(contents)

python_string = ""
for line in lines:
    python_string += line

print(python_string)

replaced_python = contents.replace('Python','C')
print(replaced_python)