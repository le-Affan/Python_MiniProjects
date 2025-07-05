# Requirements:
# User inputs a sentence or paragraph
# Program counts and displays the number of words
# Words are separated by spaces
# Bonus Idea:
# Also count characters (with and without spaces)

content=(input("Enter the content: "))
word_count=1
char_count_1=0
char_count_2=0

for char in content:
    char_count_1+=1
    char_count_2+=1
    if char==" ":
        word_count+=1
        char_count_2-=1

print(f"word count={word_count}")
print(f"character count={char_count_1}")
print(f"character count without spaces={char_count_2}")




