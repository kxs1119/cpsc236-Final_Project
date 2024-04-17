Quizmaker is a code that simulates taking a test and returning its score. To run it, simply run the "client.py" file while having source.py as well as testbank.csv in the same directory. The program will then prompt the following questions:

    Prompts the user to enter first & last name 
    Prompts the user to enter an ID 
    Validates the user's ID
    Asks for 10 or 20 questions from the testbank file 
    Quiz beings, Displays 1 question at a time
        Recieves input of answer choice 
        If invalid answer, prompt to re enter a valid answer
    
    When the quiz is done, creates a text file of:
        Name of file: StudentID_Firstname_Lastname
        Student ID, First name and Last Name
        Score
        Elapsed time
        Selected questions text, and correct answers, and student answer
    
    Prompt users to Q (exit), S(clear&start again)
    The text file with the results will be located in the same directory as the "client.py" file.