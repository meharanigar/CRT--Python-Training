s = input().strip()

freq = {}

# Count frequency of each character
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Count frequency occurrences
count_freq = {}

for f in freq.values():
    count_freq[f] = count_freq.get(f, 0) + 1

# Case 1: Already valid
if len(count_freq) == 1:
    print("YES")

# Case 2: More than 2 different frequencies
elif len(count_freq) > 2:
    print("NO")
