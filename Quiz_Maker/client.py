import source

def main():
    print("Welcome to Quizmaker!")
    
    firstName = " "
    lastName = " "
    letterId = " "
    numId = " "
    maxIdAttempts = 3
    questionNums = []
    FILENAME = "testbank.csv"
    
    while True:
        firstName = input("Please enter your first name:")
        print()
        lastName = input("Please enter your last name:")
        print()
        print("Please enter your letter id:")
        print("A valid ID must provide 'A' and 6 numbers")
        letterId = input("Enter ID: ")
        print()
        # validating the letter id and if incorrect it will ask the user to try again with a max attempt of 3 times
        maxIdAttempts = 3
        while source.validateId(letterId) == False and maxIdAttempts > 0:
            print("Invalid ID. Please try again.")
            letterId = input("Enter ID: ")
            maxIdAttempts -= 1
            

        #Getting the number of questions the user will want for their quiz
        n = int(input("Would you like your quiz to have 10 or 20 questions?: "))
        while n != 10 and n != 20:
            n = int(input("Please input 10 or 20 questions: "))
    
        #Making the quiz for the user
        questionNums = source.makeQuiz(n)
        

        # Display the quiz to the user
        source.display_quiz(questionNums)
        
        # TODO: Need a variable for scores
        # TODO: Need a variable for the time it took
        import source

def main():
    print("Welcome to quizmaker!")
    
    firstName = " "
    lastName = " "
    letterId = " "
    numId = " "
    maxIdAttempts = 3
    questionNums = []
    score = 0
    FILENAME = "testbank.csv"
    
    while True:
        firstName = input("Please enter your first name:")
        print()
        lastName = input("Please enter your last name:")
        print()
        print("Please enter your letter id:")
        print("A valid ID must provide 'A' and 6 numbers")
        letterId = input("Enter ID: ")
        print()
        # validating the letter id and if incorrect it will ask the user to try again with a max attempt of 3 times
        maxIdAttempts = 3
        while source.validateId(letterId) == False and maxIdAttempts > 0:
            print("Invalid ID. Please try again.")
            letterId = input("Enter ID: ")
            maxIdAttempts -= 1
            

        #Getting the number of questions the user will want for their quiz
        numQuestions = int(input("Would you like your quiz to have 10 or 20 questions?: "))
        while numQuestions != 10 and numQuestions != 20:
            numQuestions = int(input("Please input 10 or 20 questions: "))
    
        #Making the quiz for the user
        questionNums = source.makeQuiz(numQuestions)
        

        # Display the quiz to the user
        source.display_quiz(questionNums)
        
        # TODO: Need a variable for scores
        score = source.calculateScore(numQuestions)
        print(score)
        
        # TODO: Need a variable for the time it took
        time = 60 #TEST VALUE
        
        # TODO: Writing the quiz file for the user
        source.createStudentFile(questionNums, firstName, lastName, letterId, score, time, numQuestions)

        complete_test = input("Would you like to complete the test? (Q/S)").lower()
        # adding redo or quit conditions
        if complete_test == 'q':
            print("Thank you for using the test!")
            break
        elif complete_test =='s':
            print("We will now begin the another test!")
        else:
            print("Please enter either Q or S")

        complete_test = input("Would you like to complete the test? (Q/S)").lower()
        # adding redo or quit conditions
        if complete_test == 'q':
            print("Thank you for using the test!")
            break
        elif complete_test =='s':
            print("We will now begin the another test!")
        else:
            print("Please enter either Q or S")
        
if __name__ == "__main__":
    main()