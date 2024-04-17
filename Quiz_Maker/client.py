from queue import Full
import source
import time 

def main():
    print("Welcome to quizmaker!")
    print()
    
    FILENAME = "testbank.csv"
    
    #Getting the user's information for writing the file (Kenny)
    while True:
        firstName = input("Please enter your first name:")
        print()
        lastName = input("Please enter your last name:")
        print()
        print("Please enter your letter id:")
        print("A valid ID must provide 'A' and 6 numbers")
        letterId = input("Enter ID: ")
        print()

        # validating the letter id and if incorrect it will ask the user to try again 
        #with a max attempt of 3 times (Kenny)
        maxIdAttempts = 3
        while source.validateId(letterId) == False and maxIdAttempts > 0:
            print("Invalid ID. Please try again.")
            letterId = input("Enter ID: ")
            maxIdAttempts -= 1
            

        #Getting the number of questions the user will want for their quiz (Luke)
        numQuestions = int(input("Would you like your quiz to have 10 or 20 questions?: "))
        while numQuestions != 10 and numQuestions != 20:
            numQuestions = int(input("Please input 10 or 20 questions: "))
    
        #Making the quiz for the user (Luke)
        questionNums = source.makeQuestions(numQuestions)
        
        # Display the quiz to the user and get the elapsed time (Kenny)
        elapsed_time = source.display_quiz(questionNums)
        

        # Creating variable for elapsed time (Kenny)
        score = round(source.calculateScore(numQuestions),1)
        print(f"Score: {score}%")
        
        
        #Writing the quiz file for the user (Luke)
        source.createStudentFile(firstName, lastName, letterId, score, elapsed_time, numQuestions)

        #Prompting the user to do another quiz or exit the program (Kenny)
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