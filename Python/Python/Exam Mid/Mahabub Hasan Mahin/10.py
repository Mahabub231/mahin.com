input_file = "/home/student_user/Documents/input.txt"
output_file = "/home/student_user/Documents/output.txt"

with open(input_file, 'r') as file:
    text = file.read()

word_count = {}
for word in text.split():
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

with open(output_file, 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}\n")

print(f"Word frequencies written to {output_file}.")
