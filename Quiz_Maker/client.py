import source


def main():
    print("Welcome to quizmaker!")
    
    firstName = " "
    lastName = " "
    letterId = " "
    numId = " "
    maxIdAttempts = 3
    questionNums = []
    
    while True:
        print("Please enter your first name:")
        firstName = input()
        
        print("Please enter your last name:")
        lastName = input()
        
        print("Please enter your letter id:")
        print("A valid ID must provide 'A' and 6 numbers")
        letterId = input()
        # validating the letter id and if incorrect it will ask the user to try again with a max attempt of 3 times
        if source.validateId(letterId) == False:
            print("Please try again")
            maxIdAttempts -= 1
            if maxIdAttempts == 0:
                print("You have exceeded the maximum number of attempts")
                break

        #Getting the number of questions the user will want for their quiz
        n = int(input("Would you like your quiz to have 10 or 20 questions?: "))
        while n != 10 and n != 20:
            n = int(input("Please input 10 or 20 questions: "))

        #Making the quiz for the user
        questionNums = source.makeQuiz(n)
        
        #Completing the test
            #need the test function here

        #Writing the quiz file for the user
        #Need a variable for scores
        #Need a variable for the time it took
        source.createStudentFile(questionNums, firstName, lastName, letterId, numId, score, time, n)

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