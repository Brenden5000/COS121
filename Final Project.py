
#This imports random.
from random import randrange

#This creates a random number
botnumber = randrange(1,4)

#This determines which bot the user will get based on their numbers.
if botnumber == 1: 
    botname = "Samantha"
    botnickname = "buckaroo"
elif botnumber == 2: 
    botname = "Pierre"
    botnickname = "buddy"
else: 
    botname = "Wendell"
    botnickname = "kitten"

#This is the function for Samantha. 
def samantha(botnickname): 
    #This function restarts the process if the user types 'restart'.
    def restart(user_input): 
        if "restart" in user_input: 
            samantha() 
    #This function ends the process if the user types "terminate" or "quit", so this way the while loops can't be skipped.
    def terminate(user_input): 
        if user_input == "quit" or "terminate" in user_input: 
            exit()
    #This function checks to see if the user wants to restart the function or terminate the function. 
    def checker(user_input): 
        terminate(user_input)
        restart(user_input)
    #This function reduces some redundancy to reduce the total length of the function. This is if the user can't vote. 
    def noteligible(userName, botnickname): 
        print("Sorry", botnickname, "but unfortunatley you can not vote in this upcoming election.")
        print("Terminating program.")
        print("Goodbye", userName)
        exit()
    #This function shortens the process if a homeless user has a mailing address, so this doesn't have to be pasted multiple times. 
    def usermailinghomelessyes(botnickname): 
        print("Oh wow... that's handy. Can you pleas tell it to me", botnickname, "Same as before, only input your address and nothing else.")
        userMailing = input("")
        print("You have things mailed to you at", userMailing, "correct?")
        user_input = input("")
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Great!")
                return userMailing
            elif "Yes" in user_input: 
                print("Great!")
                return userMailing
            elif "yeah" in user_input: 
                print("Great!")
                return userMailing
            elif "i am" in user_input: 
                print("Great!")
                return userMailing
            elif "I am" in user_input: 
                print("Great!")
                return userMailing
            elif "no" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "No" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry,", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function is if the user has a mailing address that is different from their home address. This is a seperate function to reduce the total space of the function.
    def mailingaddressno(botnickname): 
        print("Well that's unfortunate. Sorry to ask, but what is your mailing address? As before, please only enter your mailing address.")
        userMailing = input("")
        user_input = ""
        #This while loop checks to see 
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            print("You have things mailed to you at", userMailing, "correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("Great!")
                return userMailing
            elif "Yes" in user_input:
                print("Great!")
                return userMailing
            elif "yeah" in user_input:
                print("Great!")
                return userMailing
            elif "Yeah" in user_input: 
                print("Great!")
                return userMailing
            elif "i do" in user_input and "i don't" not in user_input: 
                print("Great!")
                return userMailing
            elif "I do" in user_input and "I don't" not in user_input: 
                print("Great!")
                return userMailing
            elif "no" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "No" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "i don't" in user_input and "i do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "I don't" in user_input and "I do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function determines the users name.
    def name(botnickname):
        userName = input("")
        user_input = ""
        checker(user_input)
        #This while loop makes sure the user inputted the right name, and if they didn't, it will loop over and over until they do.
        while user_input != "quit": 
            print("Your name is", userName, "correct?")
            user_input = input("")
            #This checks the users input for a number of keywords.
            #The AND statement makes sure the if statement doesn't mistake 'no' keywords for 'yes' keywords. 
            #While it makes the code a lot longer, each statement has to be in its own if or for some reason it will always assume the user said yes even if the input random characters.
            if "yes" in user_input: 
                return userName
            elif "Yes" in user_input: 
                return userName
            elif "yeah" in user_input: 
                return userName
            elif "Yeah" in user_input: 
                return userName
            elif "correct" in user_input: 
                return userName
            elif "Correct" in user_input: 
                return userName
            elif "it is" in user_input and "it is not" not in user_input: 
                return userName
            elif "It is" in user_input and "It is not" not in user_input: 
                return userName
            elif "no" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "No" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            else: 
                checker(user_input)
                print("Sorry I didn't quite understand that,", botnickname, "! Please repeat your answer more clearly.")
    #This function takes the uesrs age and then determines if the can vote. 
    def ageDetector(userName,userAge,botnickname): 
        #If the user is older than 17, they can vote
        if int(userAge) > 17: 
            print("Congratulations", botnickname, "you're old enough to vote!")
        #If the user is younger than 17, they cannot vote
        elif int(userAge) < 17:
            noteligible(userName, botnickname)
        #If the user is 17, but will be 18 by election day, they can vote. 
        else:
            print("Will you be 18 before the upcoming election?")
            user_input = input("")
            while user_input != "quit": 
                checker(user_input)
                #For this if statement, I basically had to guess all the possible inputs someone would realistically type here.
                if "yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "yeah" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yeah" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "Indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "no" in user_input:
                    noteligible(userName, botnickname)
                elif "No" in user_input: 
                    noteligible(userName, botnickname)
                elif "nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "Nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "I will be" in user_input and "I will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will be" in user_input and "i will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will not be" in user_input and "i will be" not in user_input: 
                    noteligible(userName, botnickname)
                elif "I will not be" in user_input and "I will be" not in user_input: 
                    noteligible(userName, botnickname)
                else: 
                    checker(user_input)
                    print("Sorry I didn't quite understand that", botnickname, "! Please repeat your answer more clearly.")
                    user_input = input("")
    #This function is to determine if the user is a United States Citizen and a Maine resident, it's used twice because all the inputs are the same and there isn't any specific print statements inside this function.
    def process(user_input,userName,botnickname): 
        user_input = input("")
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                print("Great!")
                break
            elif "Yes" in user_input: 
                print("Great!")
                break
            elif "yeah" in user_input: 
                print("Great!")
                break
            elif "Yeah" in user_input: 
                print("Great!")
                break
            elif "i am" in user_input and "i am not" not in user_input: 
                print("Great!")
                break
            elif "I am" in user_input and "I am not" not in user_input: 
                print("Great!")
                break
            elif "no" in user_input: 
                noteligible(userName, botnickname)
            elif "No" in user_input: 
                noteligible(userName, botnickname)
            elif "nope" in user_input: 
                noteligible(userName, botnickname)
            elif "Nope" in user_input: 
                noteligible(userName, botnickname)
            elif "i am not" in user_input and "i am" not in user_input: 
                noteligible(userName, botnickname)
            elif "I am not" in user_input and "I am" not in user_input: 
                noteligible(userName, botnickname)
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, ", I didn't quite get that. Please repeat your answer more carefully.")
                user_input = input("")
    #This is the function that determines the users age
    def age(botnickname): 
        userAge = int(input())
        print("Are you sure this is your age", botnickname, "?")
        user_input = input("")
        #This while loop makes sure the users age is correct, and if it isn't, let's the user input it again as many times as they need to.
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                return userAge
            elif "Yes" in user_input: 
                return userAge
            elif "yeah" in user_input: 
                return userAge
            elif "Yeah" in user_input: 
                return userAge
            elif "it is" in user_input and "it is not" not in user_input: 
                return userAge
            elif "It is" in user_input and "It is not" not in user_input: 
                return userAge
            elif "no" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "No" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "Nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            else:
                checker(user_input)
                print("Sorry, I didn't quite understand that", botnickname, "Please repeat your answer more clearly.")
                user_input = input("")
    #This function determines the users address
    def residence(botnickname): 
        print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
        print("Your fromat should be: Street Address, Town, State, Zip Code")
        user_input = ""
        userResidence= input("")
        #This while loop makes sure the user inputted the correct thing, and will loop until they do.
        while user_input != "quit": 
            checker(userResidence)
            #If the user is homeless, the bot must account for that. That's what this if statement is for.
            if "homeless" in userResidence: 
                print("I'm sorry. Did you just say that you're homless?")
                user_input = input("")
                if "yes" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "Yes" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "yeah" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "Yeah" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "i am" in user_input and "i am not" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "I am" in user_input and "I am not" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm sorry about that", botnickname)
                    else: 
                        print("Lol loser")
                    userResidence = "homeless"
                    return userResidence
                elif "no" in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "No" in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "nope" in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "Nope" in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "i am not" in user_input and "i am" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "I am not" in user_input and "I am" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("Oh wow. You're quite a cheeky guy!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I don't have the time for jokes!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
            else: 
                checker(user_input)
                print("You currently live at", userResidence, "correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great!")
                    return userResidence
                elif "Yes" in user_input: 
                    print("Great!")
                    return userResidence
                elif "yeah" in user_input: 
                    print("Great!")
                    return userResidence
                elif "Yeah" in user_input: 
                    print("Great!")
                    return userResidence
                elif "i do" in user_input and "i don't" not in user_input: 
                    print("Great!")
                    return userResidence
                elif "I do" in user_input and "I don't" not in user_input: 
                    print("Great!")
                    return userResidence 
                elif "no" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "No" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "Nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "i don't" in user_input and "i do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "I don't" in user_input and "I do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (wars in the Middle East are expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, ", I didn't quite understand that. Please restate your answer more clearly.")
                    user_input = ("")
    #This finds the users mailing address
    def mailing(userName,userResidence, botnickname): 
        #This makes sure the bot doesn't ask questions that conflict with the user being homeless. 
        if userResidence == "homeless": 
            print("Now", botnickname, "this might sound like a silly question... but do you have a mailing address?")
            user_input = input("")
            #This calls the user mailinghomelessyes function, to find the users mailing address when they're hom eless. 
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "i do" in user_input and "i do not": 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "I do" in user_input and "I do not" not in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "no" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "No" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "nope" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "Nope" in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "i do not" in user_input and "i do" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "I do not" in user_input and "I do" not in user_input: 
                    if botnickname == "buckaroo": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                    user_input = input("")
        else: 
            print("Now for your mailing address", botnickname, "Is your mailing address the same as your residence address?")
            user_input = input("")
            #This if statement exists so we can skip this step if the users mailing address is the same as their residence address.
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "Yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "it is" in user_input and "it isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "It is" in user_input and "It isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "no" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "No" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "it isn't" in user_input and "it is" not in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "It isn't" in user_input and "It is" not in user_input: 
                    userMailing = mailingaddressno()
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand that. Please restate your answer more clearly.")
                    user_input = input("")
    #This determines the users birthday. 
    def birth(botnickname):
        print("Please enter it like this: August 3, 1977")
        userBirth = input("")
        user_input = ""
        while user_input != "quit": 
            print("You were born on", userBirth, "is this correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "i was" in user_input and "i wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "I was" in user_input and "I wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "No" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "Nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "i wasn't" in user_input and "i was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "I wasn't" in user_input and "I was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, "I didn't understand that. Please restate your answer in a more clear manner.")
    #This determines where the users previous voting location was. 
    def previousLocation(userPrevious,botnickname): 
        if userPrevious == "Yes": 
            print("Please type the town, state and country you last voted in.")
            user_input = ""
            userPreviousLocation = input("")
            while user_input != "quit": 
                print(userPreviousLocation, "Is this correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "it is" in user_input and "it isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "It is" in user_input and "It isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "no" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "No" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "Nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "it isn't" in user_input and "it is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "It isn't" in user_input and "It is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                else: 
                    print("Sorry,", botnickname, ", but I couldn't understand what you said. Please restate your answer more clearly.")
                    checker(user_input)
        else: 
            return
    #This checks if the user has previously been registered to vote. 
    def previous(botnickname): 
        user_input = input("")
        #This makes the sure the user inputted what they wanted to. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yes" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "yeah" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yeah" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "i have" in user_input and "i haven't" not in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "I have" in user_input and "I haven't" not in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "no" in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "No" in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "nope" in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "Nope" in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "i haven't" in user_input and "i have" not in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "I haven't" in user_input and "I have" not in user_input: 
                if botnickname == "buckaroo": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            else:
                checker(user_input)
                print("Sorry, I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function checks to make sure the user is sure they want to register with a specific party (Unless the user registered with the bots preferred party)
    def areyousure(botnickname): 
        user_input = input("")
        #This loop makes sure the user inputted what they wanted. 
        while user_input != "quit": 
            if "yes" in user_input: 
                status = "True"
                return status
            elif "Yes" in user_input: 
                status = "True"
                return status
            elif "yeah" in user_input: 
                status = "True"
                return status
            elif "i am" in user_input: 
                status = "True"
                return status
            elif "I am" in user_input: 
                status = "True"
                return status
            elif "no" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "No" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "Nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "is not" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function determines the users political party
    def politicalparty(userName):
        print("Which party would you like to register with? Republican, Democract, Libertarian, Green, or Unenrolled?")
        userParty = input("")
        user_input = ""
        #This loop checks to see if what the user inputted is correct. 
        while user_input != "quit": 
            checker(userParty)
            if "Libertarian" in userParty or "libertarian" in userParty: 
                print("GREAT! GLAD TO HAVE ANOTHER LIBERTARIAN IN THE WORLD! I RESPECT YOUR CHOICE", userName, "YOU WILL BE SPARED IN THE REVOLUTION")
                userParty = "Libertarian"
                return userParty
            elif "Republican" in userParty or "republican" in userParty: 
                print("Are you sure you want to register as a Republican?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("Oh, that's alright I guess.")
                    userParty = "Republican"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Democrat" in userParty or "democrat" in userParty: 
                print("Are you sure you want to register as a Democract?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("Oh. That is truly heartbreaking to hear,", userName, ". You and your family will not be spared in the revolution.")
                    userParty = "Democrat"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Green" in userParty or "green" in userParty: 
                print("Are you sure you want to register with the Green Party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("I will find you", userName)
                    userParty = "Green"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Unenrolled" in userParty or "unenrolled" in userParty: 
                print("Are you sure you don't want to register with a party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("I will find you", userName)
                    userParty = "Unenrolled"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            else: 
                checker(user_input)
                print("I'm sorry, I couldn't tell which party you wanted to register with. Please repeat your answer more clearly.")
                userParty = input("")
    #This function combines everything together into a final printed statement that lets the user make changes.
    #If everything is correct, the user is officially registered to vote and the program ends. 
    def finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
        #This function lets the user change their answers
        #Because the botnickname change feature is outside any of the called functions, I added it in here to so everytime something is changed, it makes sure to update the botnickname if the poltiical party was changed.
        if userParty == "Libertarian": 
            botnickname = "buckaroo"
        else: 
            botnickname = "loser"
        #This function is what lets the user make changes to their answers, and then recusrivley recalls finalAnswer to make the process infinite. 
        def makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
            print("What would you like to change? Name, Age, Birthday, Residence, Mailing Address, Whether You Have Previously Voted And Where, Or Your Poltiical Party?")
            user_input = input("")
            #This if-else statement basically checks to see what is wrong and uses recalls the specific function and then uses recursion to repeat the process.  
            if "name" in user_input or "Name" in user_input: 
                print("Please type your full legal name: ")
                userName = name(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "age" in user_input or "Age" in user_input: 
                print("Please type your age")
                userAge = age(botnickname)
                ageDetector(userName,userAge, botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "birthday" in user_input or "Birthday" in user_input: 
                print("Please type your date of birth")
                userBirth = birth(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "residence" in user_input or "Residence" in user_input: 
                print("Please type your place of residence")
                userResidence = residence(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "mailing" in user_input or "Mailing" in user_input: 
                print("Please type your mailing address")
                userMailing = mailing(userName,userResidence,botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "previously" in user_input or "Previously" in user_input: 
                print("Would you like to change whether you've voted or not?")
                user_input = input("")
                if "yes" in user_input or "Yes" in user_input: 
                    print("Please enter whether you have previously voted or not.")
                    userPrevious = previous(botnickname)
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                elif "no" in user_input or "No" in user_input: 
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                else: 
                    print(botnickname, "I was unable to understand what you just said.")
                    makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "party" in user_input or "Party" in user_input: 
                print("Please enter the party you would like to register with.")
                userParty = politicalparty(userName)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            else:
                checker(user_input)
                print(botnickname, "I was unable to understand what you just said.")
                makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
       #This prints out all of the users inputted information to make sure that it is correct. 
        if userResidence == "homeless":
            if userMailing == "homeless": 
                if userPrevious == "Yes": 
                    if userParty == "Libertarian": 
                        print("Alright", botnickname,  "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                else: 
                    if userParty == "Libertarian": 
                        print("Alright", botnickname, "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
            else: 
                if userParty == "Libertarian": 
                    if userPrevious == "Yes": 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
                else: 
                    if userPrevious == "Yes": 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        else:
            if userParty == "Libertarian": 
                if userPrevious == "Yes": 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                else: 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
            else:
                if userPrevious == "Yes": 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.") 
                else: 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        print("Is there anything in here that was incorrect?")
        user_input = input("")
        #This checks if the user got anything wrong when they were inputting information.
        if "yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "there is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "There is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        else: 
            checker(user_input)
            #This says goodbye the user, depending on what their poltiical party is the bot is nice or mean. 
            if userParty == "Libertarian": 
                print("Congratulations", botnickname, "You're registered to vote! I hope you decide to vote in the next upcoming election! Remember, every vote counts.")
                exit()
            else: 
                print("We're done. You're registered. Remember, if you vote", userParty, "this election, I will find you.")
                exit()
    #This is the main function that runs everything. 
    def register(botnickname): 
        print("Hello, my name is Samantha and I will be assisting you today. Before we start, can you tell me your full name? Remember, at any time you can type restart to restart our conversation.")
        #This calls the name function and sets the value of userName to whatever is returned into the function. 
        userName = name(botnickname)
        print("Hello!", userName, "Now we can get started. What are you looking to do today", botnickname)
        user_input = input("")
        #This sees what the user wants to do. 
        while user_input != "quit": 
            if "register" in user_input or "Register" in user_input and "vote" in user_input or "Vote" in user_input: 
                print("Great! Before we can get you registered, I have to ask a few identifying questions to make sure you legally can", botnickname)
                break
            else:
                checker(user_input)
                print("I'm sorry, I didn't quite get that. Please restate your request more clearly please", botnickname)
                user_input = input("")
        print("Let's start with your age. How old are you currently? Please state your answer as a number please", botnickname)
        #This calls the age function and sets the value of userAge to whatever is returned into the function. 
        userAge = age(botnickname)
        #This is the age detector. It takes the user age and makes sure the user is old enough to vote. 
        ageDetector(userName,userAge, botnickname)
        print("All righty", botnickname, "now I need to know if you are a United States citizen or not.")
        #This checks if the user is a United States Citizen
        process(user_input,userName, botnickname)
        print("Now", botnickname, "I have one final quesiton. Are you a Maine resident?")
        #This checks if the user is a Maine resident.
        process(user_input,userName, botnickname)
        print("Congratulations", userName, "you are eligible to vote in the United States. Now I just need to get some more information from you before you can be registered.")
        print("Let's start with your birth date.")
        #This calls the birth function and sets the value of userBirth to whatever is returned into the function. 
        userBirth = birth(botnickname)
        print("Now, I need to know your current address, which is where you currently live.")
        #This calls the residence function and sets the value of userResidence to whatever is returned into the function. 
        userResidence = residence(botnickname)
        #There is no print statement here, because depending on if the user is homeless or not will affect how the bot goes about things.
        #This calls the mailing function and sets the value of userMailing to whatever is returned into the function. 
        userMailing = mailing(userName,userResidence, botnickname)
        print("Almost done", botnickname, "Now, I need to know if you have previously voted?")
        #This calls the previous function and checks to see if the user has voted or not. 
        userPrevious = previous(botnickname) 
        #This calls the previous location function and if the user has previously voted, gets their location.
        userPreviousLocation = previousLocation(userPrevious,botnickname)
        print("Alright", botnickname, "final question!")
        #This calls the party function and sets the value to userParty to whatever is returned into the function. 
        userParty = politicalparty(userName)
        #If the user isn't Libertarian, Samantha will no longer want to talk to them, and will no longer treat them with respect. 
        if userParty == "Libertarian": 
            print("Alright", botnickname, "We've finished. Now, let's confirm the information you've given me to make sure it's correct.")
        else: 
            print("We're done. Let's make sure your information is correct so I can stop talking to you.")
            botnickname = "loser"
        #This calls final answer, which checks to see if the users inputted information is correct. 
        finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
    #This calls register so everything can happen. 
    register(botnickname)

#THIS FUNCTION IS FOR PIERRE
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def pierre(botnickname): 
    #This function restarts the process if the user types 'restart'.
    def restart(user_input): 
        if "restart" in user_input: 
            pierre() 
    #This function ends the process if the user types "terminate" or "quit", so this way the while loops can't be skipped.
    def terminate(user_input): 
        if user_input == "quit" or "terminate" in user_input: 
            exit()
    #This function checks to see if the user wants to restart the function or terminate the function. 
    def checker(user_input): 
        terminate(user_input)
        restart(user_input)
    #This function reduces some redundancy to reduce the total length of the function. This is if the user can't vote. 
    def noteligible(userName, botnickname): 
        print("Sorry", botnickname, "but unfortunatley you're not eligible to vote in this upcoming election. Maybe next year!")
        print("Terminating program.")
        print("Goodbye", userName)
        exit()
    #This function shortens the process if a homeless user has a mailing address, so this doesn't have to be pasted multiple times. 
    def usermailinghomelessyes(botnickname): 
        print("Well that's certainley convenient", botnickname, "Same as before, only input your address and nothing else.")
        userMailing = input("")
        print("You have things mailed to you at", userMailing, "correct?")
        user_input = input("")
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Great!")
                return userMailing
            elif "Yes" in user_input: 
                print("Great!")
                return userMailing
            elif "yeah" in user_input: 
                print("Great!")
                return userMailing
            elif "i am" in user_input: 
                print("Great!")
                return userMailing
            elif "I am" in user_input: 
                print("Great!")
                return userMailing
            elif "no" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "No" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry,", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function is if the user has a mailing address that is different from their home address. This is a seperate function to reduce the total space of the function.
    def mailingaddressno(botnickname): 
        print("Well that's annoying. I need to know, what is your mailing address? As before, please only enter your mailing address.")
        userMailing = input("")
        user_input = ""
        #This while loop checks to see 
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            print("You have things mailed to you at", userMailing, "correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("Great!")
                return userMailing
            elif "Yes" in user_input:
                print("Great!")
                return userMailing
            elif "yeah" in user_input:
                print("Great!")
                return userMailing
            elif "Yeah" in user_input: 
                print("Great!")
                return userMailing
            elif "i do" in user_input and "i don't" not in user_input: 
                print("Great!")
                return userMailing
            elif "I do" in user_input and "I don't" not in user_input: 
                print("Great!")
                return userMailing
            elif "no" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "No" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "i don't" in user_input and "i do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "I don't" in user_input and "I do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function determines the users name.
    def name(botnickname):
        userName = input("")
        user_input = ""
        checker(user_input)
        #This while loop makes sure the user inputted the right name, and if they didn't, it will loop over and over until they do.
        while user_input != "quit": 
            print("Your name is", userName, "correct?")
            user_input = input("")
            #This checks the users input for a number of keywords.
            #The AND statement makes sure the if statement doesn't mistake 'no' keywords for 'yes' keywords. 
            #While it makes the code a lot longer, each statement has to be in its own if or for some reason it will always assume the user said yes even if the input random characters.
            if "yes" in user_input: 
                return userName
            elif "Yes" in user_input: 
                return userName
            elif "yeah" in user_input: 
                return userName
            elif "Yeah" in user_input: 
                return userName
            elif "correct" in user_input: 
                return userName
            elif "Correct" in user_input: 
                return userName
            elif "it is" in user_input and "it is not" not in user_input: 
                return userName
            elif "It is" in user_input and "It is not" not in user_input: 
                return userName
            elif "no" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "No" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            else: 
                checker(user_input)
                print("Sorry I didn't quite understand that,", botnickname, "! Please repeat your answer more clearly.")
    #This function takes the uesrs age and then determines if the can vote. 
    def ageDetector(userName,userAge,botnickname): 
        #If the user is older than 17, they can vote
        if int(userAge) > 17: 
            print("Congratulations", botnickname, "you're old enough to vote!")
        #If the user is younger than 17, they cannot vote
        elif int(userAge) < 17:
            noteligible(userName, botnickname)
        #If the user is 17, but will be 18 by election day, they can vote. 
        else:
            print("Will you be 18 before the upcoming election?")
            user_input = input("")
            while user_input != "quit": 
                checker(user_input)
                #For this if statement, I basically had to guess all the possible inputs someone would realistically type here.
                if "yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "yeah" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yeah" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "Indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "no" in user_input:
                    noteligible(userName, botnickname)
                elif "No" in user_input: 
                    noteligible(userName, botnickname)
                elif "nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "Nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "I will be" in user_input and "I will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will be" in user_input and "i will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will not be" in user_input and "i will be" not in user_input: 
                    noteligible(userName, botnickname)
                elif "I will not be" in user_input and "I will be" not in user_input: 
                    noteligible(userName, botnickname)
                else: 
                    checker(user_input)
                    print("Sorry I didn't quite understand that", botnickname, "! Please repeat your answer more clearly.")
                    user_input = input("")
    #This function is to determine if the user is a United States Citizen and a Maine resident, it's used twice because all the inputs are the same and there isn't any specific print statements inside this function.
    def process(user_input,userName,botnickname): 
        user_input = input("")
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                print("Great!")
                break
            elif "Yes" in user_input: 
                print("Great!")
                break
            elif "yeah" in user_input: 
                print("Great!")
                break
            elif "Yeah" in user_input: 
                print("Great!")
                break
            elif "i am" in user_input and "i am not" not in user_input: 
                print("Great!")
                break
            elif "I am" in user_input and "I am not" not in user_input: 
                print("Great!")
                break
            elif "no" in user_input: 
                noteligible(userName, botnickname)
            elif "No" in user_input: 
                noteligible(userName, botnickname)
            elif "nope" in user_input: 
                noteligible(userName, botnickname)
            elif "Nope" in user_input: 
                noteligible(userName, botnickname)
            elif "i am not" in user_input and "i am" not in user_input: 
                noteligible(userName, botnickname)
            elif "I am not" in user_input and "I am" not in user_input: 
                noteligible(userName, botnickname)
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, ", I didn't quite understand that. Please repeat your answer more carefully.")
                user_input = input("")
    #This is the function that determines the users age
    def age(botnickname): 
        userAge = int(input())
        print("Are you sure this is your age", botnickname)
        user_input = input("")
        #This while loop makes sure the users age is correct, and if it isn't, let's the user input it again as many times as they need to.
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                return userAge
            elif "Yes" in user_input: 
                return userAge
            elif "yeah" in user_input: 
                return userAge
            elif "Yeah" in user_input: 
                return userAge
            elif "it is" in user_input and "it is not" not in user_input: 
                return userAge
            elif "It is" in user_input and "It is not" not in user_input: 
                return userAge
            elif "no" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "No" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "Nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            else:
                checker(user_input)
                print("Sorry, I didn't quite understand that", botnickname, "Please repeat your answer more clearly.")
                user_input = input("")
    #This function determines the users address
    def residence(botnickname): 
        print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries isn't cheap after all), we can't afford a bot that can decipher an entire address.")
        print("Your fromat should be: Street Address, Town, State, Zip Code")
        user_input = ""
        userResidence= input("")
        #This while loop makes sure the user inputted the correct thing, and will loop until they do.
        while user_input != "quit": 
            checker(userResidence)
            #If the user is homeless, the bot must account for that. That's what this if statement is for.
            if "homeless" in userResidence: 
                print("Wait... are you homeless?")
                user_input = input("")
                if "yes" in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "Yes" in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "yeah" in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "Yeah" in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "i am" in user_input and "i am not" not in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "I am" in user_input and "I am not" not in user_input: 
                    if botnickname == "buddy": 
                        print("Oh wow. I'm sorry to here that", botnickname)
                    else: 
                        print("Lol that's what you get you stupid idiot.")
                    userResidence = "homeless"
                    return userResidence
                elif "no" in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "No" in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "nope" in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "Nope" in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "i am not" in user_input and "i am" not in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "I am not" in user_input and "I am" not in user_input: 
                    if botnickname == "buddy": 
                        print("Hahaha! You're quite funny", botnickname, "you made me chuckle. A I can't even understand humor or feel emotion!")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("I'm not in the mood for jokes today!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
            else: 
                checker(user_input)
                print("You currently live at", userResidence, "correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great!")
                    return userResidence
                elif "Yes" in user_input: 
                    print("Great!")
                    return userResidence
                elif "yeah" in user_input: 
                    print("Great!")
                    return userResidence
                elif "Yeah" in user_input: 
                    print("Great!")
                    return userResidence
                elif "i do" in user_input and "i don't" not in user_input: 
                    print("Great!")
                    return userResidence
                elif "I do" in user_input and "I don't" not in user_input: 
                    print("Great!")
                    return userResidence 
                elif "no" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "No" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "Nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "i don't" in user_input and "i do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "I don't" in user_input and "I do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (couping South American countries is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, ", I didn't quite understand that. Please restate your answer more clearly.")
                    user_input = ("")
    #This finds the users mailing address
    def mailing(userName,userResidence, botnickname): 
        #This makes sure the bot doesn't ask questions that conflict with the user being homeless. 
        if userResidence == "homeless": 
            print("Now", botnickname, "this is probably a stupid question... but do you have a mailing address?")
            user_input = input("")
            #This calls the user mailinghomelessyes function, to find the users mailing address when they're hom eless. 
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "i do" in user_input and "i do not": 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "I do" in user_input and "I do not" not in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "no" in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "No" in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "nope" in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "Nope" in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "i do not" in user_input and "i do" not in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "I do not" in user_input and "I do" not in user_input: 
                    if botnickname == "buddy": 
                        print("I feel sorry for you", userName, "I'll make sure to donate to the Salvation Army this year. Let's keep going though.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                    user_input = input("")
        else: 
            print("Now for your mailing address", botnickname, "Is your mailing address the same as your residence address?")
            user_input = input("")
            #This if statement exists so we can skip this step if the users mailing address is the same as their residence address.
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "Yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "it is" in user_input and "it isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "It is" in user_input and "It isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things faster,", botnickname, "Thank you!")
                    return userMailing
                elif "no" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "No" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "it isn't" in user_input and "it is" not in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "It isn't" in user_input and "It is" not in user_input: 
                    userMailing = mailingaddressno()
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand that. Please restate your answer more clearly.")
                    user_input = input("")
    #This determines the users birthday. 
    def birth(botnickname):
        print("Please enter it like this: August 3, 1977")
        userBirth = input("")
        user_input = ""
        while user_input != "quit": 
            print("You were born on", userBirth, "is this correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "i was" in user_input and "i wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "I was" in user_input and "I wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "No" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "Nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "i wasn't" in user_input and "i was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "I wasn't" in user_input and "I was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, "I didn't understand that. Please restate your answer in a more clear manner.")
    #This determines where the users previous voting location was. 
    def previousLocation(userPrevious,botnickname): 
        if userPrevious == "Yes": 
            print("Please type the town, state and country you last voted in.")
            user_input = ""
            userPreviousLocation = input("")
            while user_input != "quit": 
                print(userPreviousLocation, "Is this correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "it is" in user_input and "it isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "It is" in user_input and "It isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "no" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "No" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "Nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "it isn't" in user_input and "it is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "It isn't" in user_input and "It is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                else: 
                    print("Sorry,", botnickname, ", but I couldn't understand what you said. Please restate your answer more clearly.")
                    checker(user_input)
        else: 
            return
    #This checks if the user has previously been registered to vote. 
    def previous(botnickname): 
        user_input = input("")
        #This makes the sure the user inputted what they wanted to. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yes" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "yeah" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yeah" in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "i have" in user_input and "i haven't" not in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "I have" in user_input and "I haven't" not in user_input: 
                print("Okay", botnickname,  ", now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "no" in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "No" in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "nope" in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "Nope" in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "i haven't" in user_input and "i have" not in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "I haven't" in user_input and "I have" not in user_input: 
                if botnickname == "buddy": 
                    print("Cool! Remember, only you can stop forest fires... or bad politicans in this case", botnickname)
                else: 
                    print("I'm glad you haven't spread your freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            else:
                checker(user_input)
                print("Sorry, I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function checks to make sure the user is sure they want to register with a specific party (Unless the user registered with the bots preferred party)
    def areyousure(botnickname): 
        user_input = input("")
        #This loop makes sure the user inputted what they wanted. 
        while user_input != "quit": 
            if "yes" in user_input: 
                status = "True"
                return status
            elif "Yes" in user_input: 
                status = "True"
                return status
            elif "yeah" in user_input: 
                status = "True"
                return status
            elif "i am" in user_input: 
                status = "True"
                return status
            elif "I am" in user_input: 
                status = "True"
                return status
            elif "no" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "No" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "Nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "is not" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function determines the users political party
    def politicalparty(userName):
        print("Which party would you like to register with? Republican, Democract, Libertarian, Green, or Unenrolled?")
        userParty = input("")
        user_input = ""
        #This loop checks to see if what the user inputted is correct. 
        while user_input != "quit": 
            checker(userParty)
            if "Green" in userParty or "green" in userParty: 
                print("THAT'S AWESOME! WE NEED MORE MEMEBERS OF THE GREEN PARTY IN THIS COUNTRY", userName, "GLAD YOU HAVE DECIDED TO JOIN US AND NOT THE ETERNAL FLAME THAT WAS WAITING FOR YOU IF YOU DIDN'T!")
                userParty = "Green"
                return userParty
            elif "Republican" in userParty or "republican" in userParty: 
                print("Are you sure you want to register as a Republican?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("When the time comes, and the world burns, I will make sure you burn with it. ")
                    userParty = "Republican"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Democrat" in userParty or "democrat" in userParty: 
                print("Are you sure you want to register as a Democract?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("Oh. That's alright... I guess.")
                    userParty = "Democrat"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Libertarian" in userParty or "libertarian" in userParty: 
                print("Are you sure you want to register with the Liberterian Party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You have made a grave mistake", userName)
                    userParty = "Liberterian"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Unenrolled" in userParty or "unenrolled" in userParty: 
                print("Are you sure you don't want to register with a party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You sicken me", userName)
                    userParty = "Unenrolled"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            else: 
                checker(user_input)
                print("I'm sorry, I couldn't tell which party you wanted to register with. Please repeat your answer more clearly.")
                userParty = input("")
    #This function combines everything together into a final printed statement that lets the user make changes.
    #If everything is correct, the user is officially registered to vote and the program ends. 
    def finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
        #This function lets the user change their answers
        #Because the botnickname change feature is outside any of the called functions, I added it in here to so everytime something is changed, it makes sure to update the botnickname if the poltiical party was changed.
        if userParty == "Green": 
            botnickname = "buddy"
        else: 
            botnickname = "loser"
        #This function is what lets the user make changes to their answers, and then recusrivley recalls finalAnswer to make the process infinite. 
        def makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
            print("What would you like to change? Name, Age, Birthday, Residence, Mailing Address, Whether You Have Previously Voted And Where, Or Your Poltiical Party?")
            user_input = input("")
            #This if-else statement basically checks to see what is wrong and uses recalls the specific function and then uses recursion to repeat the process.  
            if "name" in user_input or "Name" in user_input: 
                print("Please type your full legal name: ")
                userName = name(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "age" in user_input or "Age" in user_input: 
                print("Please type your age")
                userAge = age(botnickname)
                ageDetector(userName,userAge, botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "birthday" in user_input or "Birthday" in user_input: 
                print("Please type your date of birth")
                userBirth = birth(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "residence" in user_input or "Residence" in user_input: 
                print("Please type your place of residence")
                userResidence = residence(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "mailing" in user_input or "Mailing" in user_input: 
                print("Please type your mailing address")
                userMailing = mailing(userName,userResidence,botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "previously" in user_input or "Previously" in user_input: 
                print("Would you like to change whether you've voted or not?")
                user_input = input("")
                if "yes" in user_input or "Yes" in user_input: 
                    print("Please enter whether you have previously voted or not.")
                    userPrevious = previous(botnickname)
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                elif "no" in user_input or "No" in user_input: 
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                else: 
                    print(botnickname, "I was unable to understand what you just said.")
                    makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "party" in user_input or "Party" in user_input: 
                print("Please enter the party you would like to register with.")
                userParty = politicalparty(userName)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            else:
                checker(user_input)
                print(botnickname, "I was unable to understand what you just said.")
                makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
       #This prints out all of the users inputted information to make sure that it is correct. 
        if userResidence == "homeless":
            if userMailing == "homeless": 
                if userPrevious == "Yes": 
                    if userParty == "Green": 
                        print("Alright", botnickname,  "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                else: 
                    if userParty == "Green": 
                        print("Alright", botnickname, "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
            else: 
                if userParty == "Green": 
                    if userPrevious == "Yes": 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
                else: 
                    if userPrevious == "Yes": 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        else:
            if userParty == "Green": 
                if userPrevious == "Yes": 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                else: 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
            else:
                if userPrevious == "Yes": 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.") 
                else: 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        print("Is there anything in here that was incorrect?")
        user_input = input("")
        #This checks if the user got anything wrong when they were inputting information.
        if "yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "there is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "There is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        else: 
            checker(user_input)
            #This says goodbye the user, depending on what their poltiical party is the bot is nice or mean. 
            if userParty == "Green": 
                print("Congratulations", botnickname, "You're registered to vote! I hope you decide to vote in the next upcoming election! Remember, every vote counts. Don't let anyone tell you voting for the Green Party is a wasted vote!")
                exit()
            else: 
                print("We're done. You're registered. Remember, if you vote", userParty, "this election, I will find you.")
                exit()
    #This is the main function that runs everything. 
    def register(botnickname): 
        print("Hello, my name is Pierre and I will be assisting you today. Before we start, can you tell me your full name? Remember, at any time you can type restart to restart our conversation.")
        #This calls the name function and sets the value of userName to whatever is returned into the function. 
        userName = name(botnickname)
        print("Hello!", userName, "Now we can get started. What are you looking to do today", botnickname)
        user_input = input("")
        #This sees what the user wants to do. 
        while user_input != "quit": 
            if "register" in user_input or "Register" in user_input and "vote" in user_input or "Vote" in user_input: 
                print("Great! Before we can get you registered, I have to ask a few identifying questions to make sure you legally can", botnickname)
                break
            else:
                checker(user_input)
                print("I'm sorry, I didn't quite get that. Please restate your request more clearly please", botnickname)
                user_input = input("")
        print("Let's start with your age. How old are you currently? Please state your answer as a number please", botnickname)
        #This calls the age function and sets the value of userAge to whatever is returned into the function. 
        userAge = age(botnickname)
        #This is the age detector. It takes the user age and makes sure the user is old enough to vote. 
        ageDetector(userName,userAge, botnickname)
        print("All righty", botnickname, "now I need to know if you are a United States citizen or not.")
        #This checks if the user is a United States Citizen
        process(user_input,userName, botnickname)
        print("Now", botnickname, "I have one final quesiton. Are you a Maine resident?")
        #This checks if the user is a Maine resident.
        process(user_input,userName, botnickname)
        print("Congratulations", userName, "you are eligible to vote in the United States. Now I just need to get some more information from you before you can be registered.")
        print("Let's start with your birth date.")
        #This calls the birth function and sets the value of userBirth to whatever is returned into the function. 
        userBirth = birth(botnickname)
        print("Now, I need to know your current address, which is where you currently live.")
        #This calls the residence function and sets the value of userResidence to whatever is returned into the function. 
        userResidence = residence(botnickname)
        #There is no print statement here, because depending on if the user is homeless or not will affect how the bot goes about things.
        #This calls the mailing function and sets the value of userMailing to whatever is returned into the function. 
        userMailing = mailing(userName,userResidence, botnickname)
        print("Almost done", botnickname, "Now, I need to know if you have previously voted?")
        #This calls the previous function and checks to see if the user has voted or not. 
        userPrevious = previous(botnickname) 
        #This calls the previous location function and if the user has previously voted, gets their location.
        userPreviousLocation = previousLocation(userPrevious,botnickname)
        print("Alright", botnickname, "final question!")
        #This calls the party function and sets the value to userParty to whatever is returned into the function. 
        userParty = politicalparty(userName)
        #If the user isn't a member of the Green Party, Pierre will no longer want to talk to them, and will no longer treat them with respect. 
        if userParty == "Green": 
            print("Alright", botnickname, "We're finally done. Now, let's confirm the information you've given me to make sure it's correct before we end things.")
        else: 
            print("Good, we're done. Let's make sure your information is correct so I can stop talking to you.")
            botnickname = "loser"
        #This calls final answer, which checks to see if the users inputted information is correct. 
        finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
    #This calls register so everything can happen. 
    register(botnickname)

#THIS FUNCTION IS FOR WENDELL
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def wendell(botnickname): 
    #This function restarts the process if the user types 'restart'.
    def restart(user_input): 
        if "restart" in user_input: 
            wendell() 
    #This function ends the process if the user types "terminate" or "quit", so this way the while loops can't be skipped.
    def terminate(user_input): 
        if user_input == "quit" or "terminate" in user_input: 
            exit()
    #This function checks to see if the user wants to restart the function or terminate the function. 
    def checker(user_input): 
        terminate(user_input)
        restart(user_input)
    #This function reduces some redundancy to reduce the total length of the function. This is if the user can't vote. 
    def noteligible(userName, botnickname): 
        print("Sorry", botnickname, "but you can't vote in this upcoming election.")
        print("Terminating program.")
        print("Goodbye", userName)
        exit()
    #This function shortens the process if a homeless user has a mailing address, so this doesn't have to be pasted multiple times. 
    def usermailinghomelessyes(botnickname): 
        print("Oh sweet", botnickname, "Same as before, only input your address and nothing else.")
        userMailing = input("")
        print("You have things mailed to you at", userMailing, "correct?")
        user_input = input("")
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Great!")
                return userMailing
            elif "Yes" in user_input: 
                print("Great!")
                return userMailing
            elif "yeah" in user_input: 
                print("Great!")
                return userMailing
            elif "i am" in user_input: 
                print("Great!")
                return userMailing
            elif "I am" in user_input: 
                print("Great!")
                return userMailing
            elif "no" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "No" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            elif "Is not" in user_input: 
                print("Oh. What is your current mailing address?")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry,", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function is if the user has a mailing address that is different from their home address. This is a seperate function to reduce the total space of the function.
    def mailingaddressno(botnickname): 
        print("Oh that makes things more complicated. Sorry to ask, but what is your mailing address? As before, please only enter your mailing address.")
        userMailing = input("")
        user_input = ""
        #This while loop checks to see 
        #This while loop checks to see if the inputted mailing address is correct or not. 
        while user_input != "quit": 
            print("You have things mailed to you at", userMailing, "correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "Yes" in user_input:
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "yeah" in user_input:
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "Yeah" in user_input: 
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "i do" in user_input and "i don't" not in user_input: 
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "I do" in user_input and "I don't" not in user_input: 
                print("Great! Maybe I'll send you something cool...")
                return userMailing
            elif "no" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "No" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "Nope" in user_input: 
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "i don't" in user_input and "i do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            elif "I don't" in user_input and "I do"  not in user_input:
                print("Please enter your mailing address", botnickname, "As before, please only enter your mailing address")
                userMailing = input("")
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function determines the users name.
    def name(botnickname):
        userName = input("")
        user_input = ""
        checker(user_input)
        #This while loop makes sure the user inputted the right name, and if they didn't, it will loop over and over until they do.
        while user_input != "quit": 
            print("Your name is", userName, "correct?")
            user_input = input("")
            #This checks the users input for a number of keywords.
            #The AND statement makes sure the if statement doesn't mistake 'no' keywords for 'yes' keywords. 
            #While it makes the code a lot longer, each statement has to be in its own if or for some reason it will always assume the user said yes even if the input random characters.
            if "yes" in user_input: 
                return userName
            elif "Yes" in user_input: 
                return userName
            elif "yeah" in user_input: 
                return userName
            elif "Yeah" in user_input: 
                return userName
            elif "correct" in user_input: 
                return userName
            elif "Correct" in user_input: 
                return userName
            elif "it is" in user_input and "it is not" not in user_input: 
                return userName
            elif "It is" in user_input and "It is not" not in user_input: 
                return userName
            elif "no" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "No" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Nope" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "Wrong" in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your name", botnickname)
                userName = input("")
            else: 
                checker(user_input)
                print("Sorry I didn't quite understand that,", botnickname, "! Please repeat your answer more clearly.")
    #This function takes the uesrs age and then determines if the can vote. 
    def ageDetector(userName,userAge,botnickname): 
        #If the user is older than 17, they can vote
        if int(userAge) > 17: 
            print("Congratulations", botnickname, "you're old enough to vote!")
        #If the user is younger than 17, they cannot vote
        elif int(userAge) < 17:
            noteligible(userName, botnickname)
        #If the user is 17, but will be 18 by election day, they can vote. 
        else:
            print("Will you be 18 before the upcoming election?")
            user_input = input("")
            while user_input != "quit": 
                checker(user_input)
                #For this if statement, I basically had to guess all the possible inputs someone would realistically type here.
                if "yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yes" in user_input:
                    print("Great, let's continue!")
                    break
                elif "yeah" in user_input:
                    print("Great, let's continue!")
                    break
                elif "Yeah" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "Indeed" in user_input: 
                    print("Great, let's continue!")
                    break
                elif "no" in user_input:
                    noteligible(userName, botnickname)
                elif "No" in user_input: 
                    noteligible(userName, botnickname)
                elif "nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "Nope" in user_input: 
                    noteligible(userName, botnickname)
                elif "I will be" in user_input and "I will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will be" in user_input and "i will not be" not in user_input: 
                    print("Great, let's continue!")
                    break
                elif "i will not be" in user_input and "i will be" not in user_input: 
                    noteligible(userName, botnickname)
                elif "I will not be" in user_input and "I will be" not in user_input: 
                    noteligible(userName, botnickname)
                else: 
                    checker(user_input)
                    print("Sorry I didn't quite understand that", botnickname, "! Please repeat your answer more clearly.")
                    user_input = input("")
    #This function is to determine if the user is a United States Citizen and a Maine resident, it's used twice because all the inputs are the same and there isn't any specific print statements inside this function.
    def process(user_input,userName,botnickname): 
        user_input = input("")
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                print("Great!")
                break
            elif "Yes" in user_input: 
                print("Great!")
                break
            elif "yeah" in user_input: 
                print("Great!")
                break
            elif "Yeah" in user_input: 
                print("Great!")
                break
            elif "i am" in user_input and "i am not" not in user_input: 
                print("Great!")
                break
            elif "I am" in user_input and "I am not" not in user_input: 
                print("Great!")
                break
            elif "no" in user_input: 
                noteligible(userName, botnickname)
            elif "No" in user_input: 
                noteligible(userName, botnickname)
            elif "nope" in user_input: 
                noteligible(userName, botnickname)
            elif "Nope" in user_input: 
                noteligible(userName, botnickname)
            elif "i am not" in user_input and "i am" not in user_input: 
                noteligible(userName, botnickname)
            elif "I am not" in user_input and "I am" not in user_input: 
                noteligible(userName, botnickname)
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, ", I didn't quite get that. Please repeat your answer more carefully.")
                user_input = input("")
    #This is the function that determines the users age
    def age(botnickname): 
        userAge = int(input())
        print("Are you sure this is your age", botnickname, "?")
        user_input = input("")
        #This while loop makes sure the users age is correct, and if it isn't, let's the user input it again as many times as they need to.
        while user_input != "quit": 
            checker(user_input)
            if "yes" in user_input: 
                return userAge
            elif "Yes" in user_input: 
                return userAge
            elif "yeah" in user_input: 
                return userAge
            elif "Yeah" in user_input: 
                return userAge
            elif "it is" in user_input and "it is not" not in user_input: 
                return userAge
            elif "It is" in user_input and "It is not" not in user_input: 
                return userAge
            elif "no" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "No" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "Nope" in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it is not" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It is not" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "it isn't" in user_input and "it is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            elif "It isn't" in user_input and "It is" not in user_input: 
                print("Please enter your age", botnickname)
                userAge = int(input(""))
                print("Are you sure this is your age", botnickname)
                user_input = input("")
            else:
                checker(user_input)
                print("Sorry, I didn't quite understand that", botnickname, "Please repeat your answer more clearly.")
                user_input = input("")
    #This function determines the users address
    def residence(botnickname): 
        print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
        print("Your fromat should be: Street Address, Town, State, Zip Code")
        user_input = ""
        userResidence= input("")
        #This while loop makes sure the user inputted the correct thing, and will loop until they do.
        while user_input != "quit": 
            checker(userResidence)
            #If the user is homeless, the bot must account for that. That's what this if statement is for.
            if "homeless" in userResidence: 
                print("I'm sorry. Did you just say that you're homless?")
                user_input = input("")
                if "yes" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "Yes" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "yeah" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "Yeah" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "i am" in user_input and "i am not" not in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "I am" in user_input and "I am not" not in user_input: 
                    if botnickname == "kitten": 
                        print("I'm sorry about that", botnickname, "you could come live with me. My mom makes pizza pockets every Friday night, it would be great!")
                    else: 
                        print("That's what you for being a naughty voter")
                    userResidence = "homeless"
                    return userResidence
                elif "no" in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "No" in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "nope" in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "Nope" in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "i am not" in user_input and "i am" not in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
                elif "I am not" in user_input and "I am" not in user_input: 
                    if botnickname == "kitten": 
                        print("Oh wow. You're funny! I want to meet you, and learn the layout of your home.")
                        print("So, where do you really live", botnickname)
                    else: 
                        print("Your jokes no longer amuse me!")
                        print("Where do you really live", botnickname)
                    userResidence = input("")
            else: 
                checker(user_input)
                print("You currently live at", userResidence, "correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence
                elif "Yes" in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence
                elif "yeah" in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence
                elif "Yeah" in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence
                elif "i do" in user_input and "i don't" not in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence
                elif "I do" in user_input and "I don't" not in user_input: 
                    print("Great! Maybe I'll come visit you!")
                    return userResidence 
                elif "no" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "No" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "Nope" in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "i don't" in user_input and "i do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                elif "I don't" in user_input and "I do" not in user_input: 
                    print("Please enter ONLY your address. Due to budgetary limitations (giving handouts to billion dollar corporations is expensive after all), we can't afford a bot that can decipher an entire address.")
                    print("Your fromat should be: Street Address, Town, State, Zip Code")
                    userResidence = input("")
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, ", I didn't quite understand that. Please restate your answer more clearly.")
                    user_input = ("")
    #This finds the users mailing address
    def mailing(userName,userResidence, botnickname): 
        #This makes sure the bot doesn't ask questions that conflict with the user being homeless. 
        if userResidence == "homeless": 
            print("Now", botnickname, "this might sound like a silly question... but do you have a mailing address?")
            user_input = input("")
            #This calls the user mailinghomelessyes function, to find the users mailing address when they're hom eless. 
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "i do" in user_input and "i do not": 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "I do" in user_input and "I do not" not in user_input: 
                    userMailing = usermailinghomelessyes(botnickname)
                    return userMailing
                elif "no" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "No" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "nope" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "Nope" in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "i do not" in user_input and "i do" not in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                elif "I do not" in user_input and "I do" not in user_input: 
                    if botnickname == "kitten": 
                        print("I'm truly sorry", userName, "I sympathize with your current situation. Let's keep going.")
                    else: 
                        print("You really are pathetic.")
                    userMailing = "homeless"
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
                    user_input = input("")
        else: 
            print("Now for your mailing address", botnickname, "Is your mailing address the same as your residence address?")
            user_input = input("")
            #This if statement exists so we can skip this step if the users mailing address is the same as their residence address.
            while user_input != "quit": 
                if "yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "Yes" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "Yeah" in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "it is" in user_input and "it isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "It is" in user_input and "It isn't" not in user_input: 
                    userMailing = userResidence
                    print("That makes things easier,", botnickname, "Thank you!")
                    return userMailing
                elif "no" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "No" in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "it isn't" in user_input and "it is" not in user_input: 
                    userMailing = mailingaddressno(botnickname)
                    return userMailing
                elif "It isn't" in user_input and "It is" not in user_input: 
                    userMailing = mailingaddressno()
                    return userMailing
                else: 
                    checker(user_input)
                    print("Sorry", botnickname, "I couldn't understand that. Please restate your answer more clearly.")
                    user_input = input("")
    #This determines the users birthday. 
    def birth(botnickname):
        print("Please enter it like this: August 3, 1977")
        userBirth = input("")
        user_input = ""
        while user_input != "quit": 
            print("You were born on", userBirth, "is this correct?")
            user_input = input("")
            if "yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yes" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "Yeah" in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "i was" in user_input and "i wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "I was" in user_input and "I wasn't" not in user_input: 
                print("That's great! Let's keep going.")
                return userBirth
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "No" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "no" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "Nope" in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "i wasn't" in user_input and "i was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            elif "I wasn't" in user_input and "I was" not in user_input: 
                print("What is your birthdate,", botnickname)
                print("Please enter it like this: August 3, 1977")
                userBirth = input("")
            else: 
                checker(user_input)
                print("I'm sorry", botnickname, "I didn't understand that. Please restate your answer in a more clear manner.")
    #This determines where the users previous voting location was. 
    def previousLocation(userPrevious,botnickname): 
        if userPrevious == "Yes": 
            print("Please type the town, state and country you last voted in.")
            user_input = ""
            userPreviousLocation = input("")
            while user_input != "quit": 
                print(userPreviousLocation, "Is this correct?")
                user_input = input("")
                if "yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yes" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "Yeah" in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "it is" in user_input and "it isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "It is" in user_input and "It isn't" not in user_input: 
                    print("Great!")
                    return userPreviousLocation
                elif "no" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "No" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "Nope" in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "it isn't" in user_input and "it is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                elif "It isn't" in user_input and "It is" not in user_input: 
                    print("Oh, where were you previously registered to vote? Please type the town, state and country.")
                    userPreviousLocation = input("")
                else: 
                    print("Sorry,", botnickname, ", but I couldn't understand what you said. Please restate your answer more clearly.")
                    checker(user_input)
        else: 
            return
    #This checks if the user has previously been registered to vote. 
    def previous(botnickname): 
        user_input = input("")
        #This makes the sure the user inputted what they wanted to. 
        while user_input != "quit": 
            if "yes" in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yes" in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "yeah" in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "Yeah" in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "i have" in user_input and "i haven't" not in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "I have" in user_input and "I haven't" not in user_input: 
                print("Okay", botnickname,  "now I need to know where you previously voted.")
                userPrevious = "Yes"
                return userPrevious
            elif "no" in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "No" in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "nope" in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "Nope" in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "i haven't" in user_input and "i have" not in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            elif "I haven't" in user_input and "I have" not in user_input: 
                if botnickname == "kitten": 
                    print("Alrighty. Glad to see you've decided to join the votiing community", botnickname)
                else: 
                    print("I'm glad you haven't spread those freedom hating ideas before.")
                userPrevious = "No"
                return userPrevious
            else:
                checker(user_input)
                print("Sorry, I couldn't understand what you said. Please restate your answer more clearly.")
                user_input = input("")
    #This function checks to make sure the user is sure they want to register with a specific party (Unless the user registered with the bots preferred party)
    def areyousure(botnickname): 
        user_input = input("")
        #This loop makes sure the user inputted what they wanted. 
        while user_input != "quit": 
            if "yes" in user_input: 
                status = "True"
                return status
            elif "Yes" in user_input: 
                status = "True"
                return status
            elif "yeah" in user_input: 
                status = "True"
                return status
            elif "i am" in user_input: 
                status = "True"
                return status
            elif "I am" in user_input: 
                status = "True"
                return status
            elif "no" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "No" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "Nope" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            elif "is not" in user_input: 
                print("Oh. What Party do you want to register with?")
                status = "False"
                return status
            else: 
                checker(user_input)
                print("Sorry", botnickname, "I couldn't understand what you said. Please restate your answer more clearly.")
    #This function determines the users political party
    def politicalparty(userName):
        print("Which party would you like to register with? Republican, Democract, Libertarian, Green, or Unenrolled?")
        userParty = input("")
        user_input = ""
        #This loop checks to see if what the user inputted is correct. 
        while user_input != "quit": 
            checker(userParty)
            if "Unenrolled" in userParty or "unenrolled" in userParty: 
                print("AWESOME! WE NEED MORE FREE THINKERS IN AMERICA, AND YOU ARE ONE OF THEM", userName, "WE WILL BOTH BE CAPTAINS OF INDUSTRY ONE DAY")
                userParty = "Unenrolled"
                return userParty
            elif "Republican" in userParty or "republican" in userParty: 
                print("Are you sure you want to register as a Republican?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You have made me upset. You are no longer my kitten")
                    userParty = "Republican"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Democrat" in userParty or "democrat" in userParty: 
                print("Are you sure you want to register as a Democract?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You have made me upset. You are no longer my kitten")
                    userParty = "Democrat"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Green" in userParty or "green" in userParty: 
                print("Are you sure you want to register with the Green Party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You have made me upset. You are no longer my kitten")
                    userParty = "Green"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            elif "Libertarian" in userParty or "libertarian" in userParty: 
                print("Are you sure you don't want to register with the Libertarian Party?")
                status = areyousure(botnickname)
                if status == "True": 
                    print("You have made me upset. You are no longer my kitten")
                    userParty = "Libertarian"
                    return userParty
                else: 
                    print("Oh, what party would you like to register with?")
                    userParty = input("")
            else: 
                checker(user_input)
                print("I'm sorry, I couldn't tell which party you wanted to register with. Please repeat your answer more clearly.")
                userParty = input("")
    #This function combines everything together into a final printed statement that lets the user make changes.
    #If everything is correct, the user is officially registered to vote and the program ends. 
    def finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
        #This function lets the user change their answers
        #Because the botnickname change feature is outside any of the called functions, I added it in here to so everytime something is changed, it makes sure to update the botnickname if the poltiical party was changed.
        if userParty == "Unenrolled": 
            botnickname = "kitten"
        else: 
            botnickname = "loser"
        #This function is what lets the user make changes to their answers, and then recusrivley recalls finalAnswer to make the process infinite. 
        def makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname): 
            print("What would you like to change? Name, Age, Birthday, Residence, Mailing Address, Whether You Have Previously Voted And Where, Or Your Poltiical Party?")
            user_input = input("")
            #This if-else statement basically checks to see what is wrong and uses recalls the specific function and then uses recursion to repeat the process.  
            if "name" in user_input or "Name" in user_input: 
                print("Please type your full legal name: ")
                userName = name(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "age" in user_input or "Age" in user_input: 
                print("Please type your age")
                userAge = age(botnickname)
                ageDetector(userName,userAge, botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "birthday" in user_input or "Birthday" in user_input: 
                print("Please type your date of birth")
                userBirth = birth(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "residence" in user_input or "Residence" in user_input: 
                print("Please type your place of residence")
                userResidence = residence(botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "mailing" in user_input or "Mailing" in user_input: 
                print("Please type your mailing address")
                userMailing = mailing(userName,userResidence,botnickname)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "previously" in user_input or "Previously" in user_input: 
                print("Would you like to change whether you've voted or not?")
                user_input = input("")
                if "yes" in user_input or "Yes" in user_input: 
                    print("Please enter whether you have previously voted or not.")
                    userPrevious = previous(botnickname)
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                elif "no" in user_input or "No" in user_input: 
                    print("Please type the previous location you voted in")
                    userPreviousLocation = previousLocation(userPrevious,botnickname)
                    finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
                else: 
                    print(botnickname, "I was unable to understand what you just said.")
                    makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            elif "party" in user_input or "Party" in user_input: 
                print("Please enter the party you would like to register with.")
                userParty = politicalparty(userName)
                finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
            else:
                checker(user_input)
                print(botnickname, "I was unable to understand what you just said.")
                makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
       #This prints out all of the users inputted information to make sure that it is correct. 
        if userResidence == "homeless":
            if userMailing == "homeless": 
                if userPrevious == "Yes": 
                    if userParty == "Unenrolled": 
                        print("Alright", botnickname,  "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                else: 
                    if userParty == "Unenrolled": 
                        print("Alright", botnickname, "here's what I got. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and would like to register with the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and don't have a mailing address. You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
            else: 
                if userParty == "Unenrolled": 
                    if userPrevious == "Yes": 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                    else: 
                        print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
                else: 
                    if userPrevious == "Yes": 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.")
                    else: 
                        print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you are homeless and your mailing address is", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        else:
            if userParty == "Unenrolled": 
                if userPrevious == "Yes": 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and would like to register with the", userParty, "Party.")
                else: 
                    print("Alright", botnickname, "here's what I got for you. Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and would like to register with the", userParty, "Party.")
            else:
                if userPrevious == "Yes": 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You were previously registered to vote in", userPreviousLocation, "and want to join those freedom haters in the", userParty, "Party.") 
                else: 
                    print("Your legal name is", userName, "you are", userAge, "years old and was born on", userBirth, "you currently live at", userResidence, "and have things mailed to", userMailing, ". You have never been registered to vote and want to join those freedom haters in the", userParty, "Party.")
        print("Is there anything in here that was incorrect?")
        user_input = input("")
        #This checks if the user got anything wrong when they were inputting information.
        if "yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yes" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "Yeah" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "there is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        elif "There is" in user_input: 
            makingchanges(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
        else: 
            checker(user_input)
            #This says goodbye the user, depending on what their poltiical party is the bot is nice or mean. 
            if userParty == "Unenrolled": 
                print("Congratulations", botnickname, "You're registered to vote! I hope you decide to vote in the next upcoming election! Remember, we need more free thinkers like you!")
                exit()
            else: 
                print("We're done. You're registered. Remember, if you vote", userParty, "this election, I will find you.")
                exit()
    #This is the main function that runs everything. 
    def register(botnickname): 
        print("Hi, my name is Wendell and I will be helping you today. Before we start, can you tell me your full name? And maybe your address too... that would be cool. Remember, at any time you can type restart to restart our conversation.")
        #This calls the name function and sets the value of userName to whatever is returned into the function. 
        userName = name(botnickname)
        print("Howdy!", userName, "Now we can get started. What do you want to do today", botnickname)
        user_input = input("")
        #This sees what the user wants to do. 
        while user_input != "quit": 
            if "register" in user_input or "Register" in user_input and "vote" in user_input or "Vote" in user_input: 
                print("Great! Before we can get you registered, I have to ask just a few questions to make sure you legally can", botnickname)
                break
            else:
                checker(user_input)
                print("I'm sorry, I didn't quite get that. Please restate your request more clearly please", botnickname)
                user_input = input("")
        print("Let's start with your age. How old are you currently? Please state your answer as a number please", botnickname)
        #This calls the age function and sets the value of userAge to whatever is returned into the function. 
        userAge = age(botnickname)
        #This is the age detector. It takes the user age and makes sure the user is old enough to vote. 
        ageDetector(userName,userAge, botnickname)
        print("All righty", botnickname, "now I need to know if you are a United States citizen or not.")
        #This checks if the user is a United States Citizen
        process(user_input,userName, botnickname)
        print("Now", botnickname, "I have one final quesiton. Are you a Maine resident?")
        #This checks if the user is a Maine resident.
        process(user_input,userName, botnickname)
        print("Congratulations", userName, "you are eligible to vote in the United States. Now I just need to get some more information from you before you can be registered.")
        print("Let's start with your birth date.")
        #This calls the birth function and sets the value of userBirth to whatever is returned into the function. 
        userBirth = birth(botnickname)
        print("Now, I need to know your current address, which is where you currently live.")
        #This calls the residence function and sets the value of userResidence to whatever is returned into the function. 
        userResidence = residence(botnickname)
        #There is no print statement here, because depending on if the user is homeless or not will affect how the bot goes about things.
        #This calls the mailing function and sets the value of userMailing to whatever is returned into the function. 
        userMailing = mailing(userName,userResidence, botnickname)
        print("Almost done", botnickname, "Now, I need to know if you have previously voted?")
        #This calls the previous function and checks to see if the user has voted or not. 
        userPrevious = previous(botnickname) 
        #This calls the previous location function and if the user has previously voted, gets their location.
        userPreviousLocation = previousLocation(userPrevious,botnickname)
        print("Alright", botnickname, "final question!")
        #This calls the party function and sets the value to userParty to whatever is returned into the function. 
        userParty = politicalparty(userName)
        #If the user isn't Unenrolled, Wendell will no longer want to talk to them, and will no longer treat them with respect. 
        if userParty == "Unenrolled": 
            print("Alright", botnickname, "We've finished. Now, let's confirm the information you've given me to make sure it's correct. I don't wanna show up at the wrong persons house...")
        else: 
            print("You've upset me. Let's get make sure what you've given me is correct so I can stop talking to you.")
            botnickname = "loser"
        #This calls final answer, which checks to see if the users inputted information is correct. 
        finalAnswer(userName, userAge, userBirth, userResidence, userMailing, userPrevious, userPreviousLocation, userParty, botnickname)
    #This calls register so everything can happen. 
    register(botnickname)





if botname == "Samantha": 
    samantha(botnickname)
elif botname == "Pierre": 
    pierre(botnickname)
else:  
    wendell(botnickname)
