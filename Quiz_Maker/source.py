import csv
from random import randint
import time # import time module for elapsing time in quiz

FILENAME = "testbank.csv"
quiz = {} # type: ignore
questions = {}

def validateId(id):
    # this function should validate the id and give the user n attempts to retry to enter
    # it will make sure the first letter is 'A' and the number of digits is 6
    
    if len(id)!= 6 and id[0] != 'A': # type: ignore
        return False
    for element in id[1:]:
        if not element.isdigit(): # type: ignore
            return False
        return True

def makeQuiz(numQuestions):
    # TODO: Make the dictionary of questions into keys so we can iterate through them 
#Read in random questions into questions dictionary, add questions dictionary in quiz dictionary
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        questionCounter = 1
        for row in reader:
            if row[0] == "Question text":
                continue
            elif row[1] == "Option A":
                continue
            elif row[2] == "Option B":
                continue
            elif row[3] == "Option C":
                continue
            elif row[4] == "Correct Answer":
                continue
            else:
                questions[str(questionCounter)] = {
                    "QuestionText":row[0],
                    "A":row[1],
                    "B":row[2],
                    "C":row[3],
                    "Answer":row[4]
                }
                questionCounter += 1
        #List to hold a list with all question numbers
        chosen_question = []
        #For loop to assign random question numbers to list a and check for duplicates
        for i in range(0, numQuestions):
            num = randint(1, 129)
            while num in chosen_question: # needs to be a while loop so that it doesnt duplicate questions
                num = randint(1, 129)
            #Putting the questions in the quiz dictionary
            chosen_question.append(num)
    #Returning a list with all the question numbers to use as keys for future programs
    return chosen_question # type: ignore

def display_quiz(chosen_question):
    # this function should display time elapsed and the current question
    # this function will take from quiz, display a unique questions one at a time from the quiz dictionary
    # it will also show the options for each question 
    # it will ask the user for useranswer, store the useranswer in the quiz dictionary
    userAnswer = ""
    start = time.time()
    # index = chosen_question # type: ignore
    print(chosen_question) # type: ignore
    for index in range(0, len(chosen_question)):
        print("working?")
        #if time.time() > 600:
            #break
        #else:
        print("\nQuestion " + str(index+1) + ": " + questions[str(chosen_question[index])]["QuestionText"]) # type: ignore
        print("Options: ")
        print("\tA: " + questions[str(chosen_question[index])]["A"])
        print("\tB: " + questions[str(chosen_question[index])]["B"])
        print("\tC: " + questions[str(chosen_question[index])]["C"])
        userAnswer = str(input("Enter your answer: ")).upper() # type: ignore
        while userAnswer != "A" and userAnswer != "B" and userAnswer != "C":
            userAnswer = str(input("Please enter A, B, or C: ")).upper()
        quiz[str(index)] = {
            "Question":questions[str(chosen_question[index])]["QuestionText"],
            "A":questions[str(chosen_question[index])]["A"],
            "B":questions[str(chosen_question[index])]["B"],
            "C":questions[str(chosen_question[index])]["C"],
            "rightAnswer":questions[str(chosen_question[index])]["Answer"],
            "userAnswer":userAnswer }# type: ignore
        #elapsed_time = time.time() - start
        #print(f"Time elapsed: {time.time() - start:.2f} seconds") # type: ignore
    
    # setting end and elapsed time 
    end = time.time() 
    elapsed_time = end - start 
        
    return userAnswer # type: ignore

def calculateScore(totalQuestions):
    # this function should calculate the score of the student based on the quiz dictionary
    # it will compare the student answers to the correct answers in the quiz dictionary
    # then add 1 to a counter based on the number of correct answers
    score = 0
    for question_index in range(0, totalQuestions): # type: ignore
        userAns = quiz[str(question_index)]["userAnswer"]
        rightAns = quiz[str(question_index)]["rightAnswer"]
        if userAns == rightAns: # type: ignore
            score += 1 
    grade = (score/totalQuestions)*100
    return grade # type: ignore
    
    
def createStudentFile(questionNums, firstName, lastName, letterId, score, time, numQuestions):
    textFile = str(letterId) + "_" + lastName + "_" + firstName + ".txt"
    with open(textFile, "w") as file:
        #Writing StudentId
        file.write("Student ID: " + str(letterId))
        #Writing First+LastName
        file.write("\nName: " + firstName + " " + lastName)
        #Writing user's Score
        file.write("\nScore: " + str(score) + "%")
        #Writing Elapsed Time
        file.write("\nElapsed time: " + str(time) + " seconds\n")
        
        #For loop to write out the questions, their correct answer and the student's answer
        for i in range(0, numQuestions):
            #Assigning Variables to make writing easier
            userAns = quiz[str(i)]["userAnswer"]
            rightAns = quiz[str(i)]["rightAnswer"]
            text = quiz[str(i)]["Question"]
            
            #Writing out Question
            file.write("\nQuestion " + str(i+1) + ": " + str(text))
            #Writing Student's Answer
            file.write("\n\tStudent Answer: " + userAns) #NEED THE STUDENT'S ANSWER
            #Writing the Right Answer
            file.write("\n\tRight Answer: " + rightAns)