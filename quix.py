def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
        
    
score = 0
print("Guess the puzzle")
guess1 = input("What does HTML stand for?")
check_guess(guess1, "HyperText Markup Language")
guess2 = input("Which programming language is often used for client-side web development?")
check_guess(guess2, "JavaScript")
guess3 = input("What does CSS stand for?")
check_guess(guess3, "Cascading Style Sheets")
guess4 = input("What is the purpose of a web server?r")
check_guess(guess4, "Hosting")
guess5 = input("Which protocol is used for secure data transmission on the web")
check_guess(guess5,"HTTPS")
guess6 = input("What is the role of a Content Management System (CMS) in web development?")
check_guess(guess6,"content management")
guess7 = input("What's the purpose of the 'DOCTYPE' declaration in an HTML document?")
check_guess(guess7,"document type collection")
guess8 = input("what is the primary function of a web browser")
check_guess(guess8,"rendering")
guess9("Which HTTP method is used for retrieving data from a web server?")
check_guess(guess9,"GET")
guess10(" What is the role of a web framework in web development?")
check_guess(guess10,"simplification")
guess11 = input("what is the expanssion of cpu")
check_guess(guess,"control processing unit")
print("Your Score is "+ str(score))