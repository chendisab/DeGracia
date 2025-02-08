input_string = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
others = 0

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for char in input_string:
is_vowel = False
for vowel in vowel_list:
if char == vowel:
is_vowel = True
break
if is_vowel:
vowels += 1
elif ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
consonants += 1
elif char == ' ':
spaces += 1
else:
others += 1
print("\nCharacter Counts:")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Other characters: {others}")

total = 0
for char in input_string:
if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
total += int(char)

print(f"\nSum of digits in the string: {total}")
print("\nPattern a:")
for i in range(1, 6):
for j in range(5 - i):
print(" ", end="")
for k in range(1, i + 1):
print(k, end="")
print()

print("\nPattern b:")
i = 1
while i <= 7:
if i != 2:
for j in range(i):
print(i, end="")
print()
i += 1