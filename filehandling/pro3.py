'''
Word Frequency Analyzer
A company wnats to analyze the text
write a python program:
1.Read contents from data.txt
2.count the frequency of each word
3.display most repeated word
4.handle the exceptions
'''


try:
    file = open("data.txt", "r")
    data = file.read()
    words = data.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    print("Word Frequency:")
    for word, count in freq.items():
        print(word, ":", count)
    max_word = max(freq, key=freq.get)
    print("Most Repeated Word:", max_word)

    file.close()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error:", e)

