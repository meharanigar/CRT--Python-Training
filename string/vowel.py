s = input()
vowels = "aeiou"
vowels_count = 0
consonants_count = 0

for ch in s:
    if ch.isdigit():
        continue
    if ch in vowels:
        vowels_count += 1
    if ch.isalpha():
        consonants_count += 1

if (vowels_count == consonants_count):
    print("balanced")
else:
    print("not balanced")