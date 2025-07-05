# Requirements:
# User inputs a sentence
# Program counts the frequency of each word
# Display the frequency nicely using a dictionary
# Bonus: Display the most frequent word/character

text=input("Enter your text: ")
words=text.split()
frequency={}

for i in words:
    word_freq=words.count(i)
    frequency[i]=word_freq

for key,value in frequency.items():
    print(f"{key}:{value}")


