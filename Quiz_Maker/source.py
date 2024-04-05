import csv
import random
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
    

def quiz():
    #Read in random questions into questions dictionary, add questions dictionary in quiz dictionary
    l = []
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

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
                questions[row[0]] = row[1], row[2], row[3], row[4]
                


def displayQuiz():
    # this function should display time elapsed and the current question
    # this function will take from quiz, display a unique questions one at a time from the quiz dictionary
    # it will also show the options for each question 
    # it will ask the user for useranswer, store the useranswer in the quiz dictionary
   
    start = time.time()
    elapsed_time = 0 # variable for elapsed time 
    question_index = 1
    while question_index in quiz and time.time() - start < 600: # type: ignore
        print(f"Question {question_index}: {quiz[question_index]}") # type: ignore
        print(f"Options: {quiz[question_index]}") # type: ignore
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

def createStudentFile():
    # this function should create a new student file with the following columns:
    # first and last name, student id, score, elapsed time, answers {correct answers , student answers}
    
    pass

