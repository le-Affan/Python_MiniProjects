# Requirements:
# Questions and answers stored in a text file
# Program reads questions one by one
# User answers them
# Keeps track of the score
# Shows total score at the end
# Bonus: Handle invalid inputs gracefully

def QuizGame():

    score=0

    with open("QnA.txt","r") as file:
        Questions=file.readlines() #splits the text file into seperate lines to make iterating easier
        for lines in Questions:
            question = ""
            for char in lines.strip(): #using .strip() to get rid of any \n
                if char != "|": #can use .find() and iterate only till the index of | character using "range"
                    question = question+char #building the question
                elif char=="|":
                    user_answer = input(question)
                    correct_answer=""
                    checkpoint_index=lines.find("|") #finding the index of | character

                    for char in range(checkpoint_index+1,len(lines.strip())):
                        correct_answer=correct_answer+lines[char] #building the answer

                    if user_answer==correct_answer:
                        print(f"{correct_answer} is the right!")
                        score=score+1
                    else:
                        print(f"Wrong! The correct answer is {correct_answer}")

    print(f"Your final score is {score}")

QuizGame()

#can be done with cleaner logic but i want to fix the logic i have built it with better logic but
#but this is what i came up with
