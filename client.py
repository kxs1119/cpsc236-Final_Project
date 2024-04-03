import source


def main():
    print("Let it begin")
    
    firstName = " "
    lastName = " "
    letterId = " "
    numId = " "
    maxIdAttempts = 3
    
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