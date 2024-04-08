import csv
from random import randint
import time # import time module for elapsing time in quiz

FILENAME = "testbank.csv"
quiz = {} # type: ignore
questions = {}

def validateId(letterId):
    # this function should validate the id
    # it will make sure the first letter is 'A' and the number of digits is 6
    if len(letterId)!= 6 or letterId[0] != 'A': # type: ignore
        return False
    for element in letterId[1:]:
        if not element.isdigit(): # type: ignore
            return False
    return True
    

def makeQuiz(numQuestions):
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
                ans = []
                ans.append(row[1])
                ans.append(row[2])
                ans.append(row[3])
                rAns = row[4]
                questions[str(questionCounter)] = row[0], ans, rAns
                questionCounter += 1

        #List to hold a list with all question numbers
        a = []
        #For loop to assign random question numbers to list a and check for duplicates
        for i in range(0, numQuestions):
            num = randint(2, 129)
            a.append(num)
            for l in range(0, len(a)):
                if a[l] == num:
                    num = randint(2, 129)
            #Putting the questions in the quiz dictionary
            quiz[str(i)] = questions[str(num)]
    #Returning a list with all the question numbers to use as keys for future programs
    return a
                


def displayQuiz():
    # this function should display time elapsed and the current question
    # this function will take from quiz, display a unique questions one at a time from the quiz dictionary
    # it will also show the options for each question 
    # it will ask the user for useranswer, store the useranswer in the quiz dictionary
   
    start = time.time()
    elapsed_time = 0 # variable for elapsed time 
    question_index = 1
    while question_index in quiz and time.time() - start < 600: # type: ignore
        print(f"Question {question_index}: {quiz[question_index][0]}") # type: ignore
        print(f"Options: {quiz[question_index][1]}") # type: ignore
        userAnswer = input("Enter your answer: ")
        quiz[question_index] = userAnswer # type: ignore
        question_index += 1
        elapsed_time = time.time() - start
        print(f"Time elapsed: {time.time() - start:.2f} seconds") # type: ignore
        
    return userAnswer # type: ignore

def calculateScore(userAnswer, correctAnswer):
    # this function should calculate the score of the student based on the quiz dictionary
    # it will compare the student answers to the correct answers in the quiz dictionary
    # then add 1 to a counter based on the number of correct answers
    score = 0
    for question_index in quiz: # type: ignore
        if quiz[question_index][correctAnswer] == quiz[question_index][userAnswer]: # type: ignore
            score += 1
        
    return score # type: ignore
    
    pass

def createStudentFile(questionNums, firstName, lastName, letterId, numId, score, time, n):
    textFile = "A" + str(numId) + "_" + lastName + "_" + firstName + ".txt"
    with open(textFile, "w") as file:
        #Writing StudentId
        file.write("Student ID: " + str(letterId) + str(numId))
        #Writing First+LastName
        file.write("\nName: " + firstName + lastName)
        #Writing user's Score
        file.write("\nScore: " + str(score) + "%")
        #Writing Elapsed Time
        file.write("\nElapsed time: " + str(time) + " seconds")
        
        #For loop to write out the questions, their correct answer and the student's answer
        for i in range(0, n):
            num = questionNums[i]
        
            q = quiz[str(i)][0]
            rightAns = quiz[str(i)][2]
            #Writing out Question
            file.write("\nQuestion " + str(i+1) + ": " + str(q))
            #Writing Student's Answer
            file.write("\n\tStudent Answer: ") #NEED THE STUDENT'S ANSWER
            #Writing the Right Answer
            file.write("\n\tRight Answer: " + rightAns)
