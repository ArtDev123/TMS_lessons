numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
# Результат: [1, 4, 9, 16, 25]

raw_names = ["  ivan ", " mArIa", "Oleg  ", "  aNNa  "]
clean_names = [name.strip().capitalize() for name in raw_names]

print(clean_names)
# Результат: ['Ivan', 'Maria', 'Oleg', 'Anna']


numbers = [1, 2, 3]
sq_dict = {n: n**2 for n in numbers}
# Результат: {1: 1, 2: 4, 3: 9}
print(sq_dict)

words = ["apple", "banana", "cherry"]
word_lengths = {w: len(w) for w in words}

print(word_lengths)
# Результат: {'apple': 5, 'banana': 6, 'cherry': 6}


files = ["image.png", "data.csv", "script.py", "photo.png", "style.css", "notes.csv"]
extensions = {f.split(".")[-1] for f in files}

print(extensions)
# Результат: {'png', 'csv', 'py', 'css'}
