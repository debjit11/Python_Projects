with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# Extract words enclosed in < and >
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    elif char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}

# Get user input for each unique word
for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

# Replace placeholders with the corresponding inputs
for word, replacement in answers.items():
    story = story.replace(word, replacement)

# Print the final story
print(story)
