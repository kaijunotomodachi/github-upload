import random
import string

phrases = []

with open('cyberpunk_slang_list.txt', 'r') as f:
	slang_definitions = f.readlines()

for line in slang_definitions:
	phrase = line.split(":")[0]
	phrases.append("".join(phrase.split()))

phrase1 = random.choice(phrases)
phrase2 = random.choice(phrases)
number = str(random.randrange(100))

password = phrase1 + phrase2 + number

print(password)