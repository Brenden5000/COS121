#This is my class. It has all the details the program needs to know about the car to function. 
class Car:
    vehicle = "car"
    def __init__(self, model, mpg, decceleration, gasTank, currentTankAmount, driveSide): 
        self.model = model 
        self.mpg = mpg 
        self.decceleration = decceleration 
        self.gasTank = gasTank 
        #This drive side variable exists because I couldn't really figure out how to make a "drive on the right side 
        #of the road" function. This way, the car also works in England. 
        self.driveSide = driveSide 
        self.currentTankAmount = currentTankAmount  

#This is the everything function. It has all my sub-functions in it, and exists so when it comes time to run everything
#The program only has to call one function and everything works. 
def everything(): 
    #This is assinging the variable car to the class. 
    car = Car(input("What kind of car do you have?: "), int(input("What is the cars miles per gallon?: ")), int(input("How long does it take to deccelerate?: ")), int(input("How large is the gas tank?: ")), int(input("How many gallons of gas are left in the tank?: ")), input("What side of the road do you drive on?: "))
    travelDistance = int(input("How far is your journey? (In Miles): "))
    desiredTravelTime = int(input("How quickly would you like to get there? (In Hours): "))
    #This program does not account for speed limit (I actually tried, and had the worst else-if statement you could imagine).
    vehicleSpeed = travelDistance // desiredTravelTime 
    #How long does it take to stop. Does not account for weather. 
    stopTime = vehicleSpeed // car.decceleration 
    #This function caclulates all 5 of the right of way laws I chose to do. 
    def fiveRightofWayLaws():     
        #This function is for Law 1
        def keepingRight(): 
            if car.driveSide == "Right" or car.driveSide == "right": 
                print("You drive on the right side of the yellow line for the duration of your journey.")
            elif car.driveSide == "Left" or car.driveSide == "left": 
                print("You drive on the left side of the yellow line for the duration of your journey")
        #This function is for Law 6. 
        def roundAboutFunction():
            #This variable is so the car can figure out of police exist.
            police = input("Is there law enforcement directing traffic? Y/N: ")
            #This else-if statement checks for law enforcement at the round-about.
            if police == "Y":
                print("You follow the direction of law enforcment.")
            else: 
                exit = input("Which roundabout exit do you need to go through?: ")
                leftVehicle = input("Is there a vehicle coming from the left? Y/N: ")
                #This else-if statement checks for oncoming traffic in the roundabout. 
                if leftVehicle == "Y":
                    print("You yield to the traffic coming from the left. Once it is safe, you enter the roundabout and leave through exit", exit)
                elif leftVehicle == "N":
                    print("You enter the roundabout and leave through exit", exit)
        #This function is for Law 3
        def publicIntersection():
            print("You reach a public intersection. It takes", stopTime, "seconds to come to a stop.")
            roundAbout = input("Is this a roundabout? Y/N: ")
            if roundAbout == "Y": 
                #Because the intersection law mentioned roundAbouts as an exception, I included the round about law
                #as a potentional outcome of the intersection situation. It's function-inception 
                roundAboutFunction()
            elif roundAbout == "N": 
                #This variable is so the car can figure out of police exist.
                police = input("Is there law enforcement directing traffic? Y/N: ") 
                #This else-if statement checks to see if their is law-enforcment directing traffic. 
                if police == "Y":
                    print("You follow the direction of law enforcment")
                elif police == "N":
                    rightVehicle = input("Is there a vehicle to your right?: Y/N: ")
                    leftVehicle = input("Is there a vehicle to you left?: Y/N: ")
                    #This else-if statement checks to see if the car needs to yield or if it has the right of way. 
                    if rightVehicle == "Y" and leftVehicle == "N": 
                        print("The car on your right has the right of way. You wait for them to go by so you can go.")
                    elif rightVehicle == "N" and leftVehicle == "Y": 
                        print("You have the right of way, so you go.")
                    elif rightVehicle == "Y" and leftVehicle == "Y": 
                        print("The car on your right has the right of way. You wait for them to go by. You have the right of way over the car on your left, so you go.")
                    elif rightVehicle == "N" and leftVehicle == "N": 
                        print("With no one in the intersection, you go.")
        #This function is for Law 4
        def privateToPublicIntersection(stopTime): 
            print("You reach the end of a private road. It takes", stopTime, "seconds to come to a stop at the stop sign.")
            vehicle = input("Is there a car approaching? Y/N: ")
            pedestrian = input("Is there a pedestrian approaching? Y/N: ")
            #This else if statement is to check if the driver needs to yield to pedestrians or oncoming traffic. 
            if vehicle == "Y" and pedestrian == "N": 
                print("You yield to the oncoming car, and then turn onto the public road.")
            elif vehicle == "N" and pedestrian == "Y":
                print("You wait for the pedestrian to cross the road, and then turn onto the public road.")
            elif vehicle == "Y" and pedestrian == "Y": 
                print("You yield to the oncoming car and wait for the pedestrian to cross the road, then turn onto the public road.")
            elif vehicle == "N" and pedestrian == "N":
                print("You turn onto the public road cautiously.")
        #This is the function for Law 9
        def transitBus(vehicleSpeed): 
            print("As you are driving, you see a transit bus is sitting on the side of the road")
            yieldSign = input("Is the left yield sign illuminated? Y/N: ")
            turnSignal = input("Is the left turn signal blinking? Y/N: ")
            #This else-if statement checks the conditions of the bus and the speed to see if the car needs to yield to the bus.
            if yieldSign == "Y" and turnSignal == "Y" and vehicleSpeed <= 35:
                print("Because your current speed is", vehicleSpeed, "you must yield to the bus and allow it to re-enter traffic.")
            elif yieldSign == "Y" and turnSignal == "Y" and vehicleSpeed >= 35:
                print("Because your current speed is", vehicleSpeed, "you do not need to yield to the bus. You continue on your journey")
            elif yieldSign == "N" and turnSignal == "N":
                print("Because the bus is not attempting to re-enter traffic, there is no need to yield to it and you continue on your journey.")
            elif yieldSign == "Y" and turnSignal == "N":
                print("The bus driver is confused. You do not yield andcontinue on your journey.")
            elif yieldSign == "N" and turnSignal == "Y":
                print("The bus driver is confused. You do not yield andcontinue on your journey.")
        #These calls all of the differnt right of way laws. 
        keepingRight()
        privateToPublicIntersection(stopTime) 
        publicIntersection()
        transitBus(vehicleSpeed) 
    #This figures out what's going on with the gas tank.
    def gasTank(): 
        #This figures out when the car will need to refill. 
        nextFillUp = car.currentTankAmount * car.mpg
        #I really couldn't think of any reason to make this any more complicated, so 
        if car.currentTankAmount == car.gasTank : 
                print("You have a full tank of gas and will not to need to refuel for", nextFillUp, "miles")
        elif car.currentTankAmount == 0: 
            print("You have", car.currentTankAmount, "gallons of gas left in the tank, and will need to refuel in", nextFillUp, "miles")
    
    #This makes sure that if the car has no gas, the car can't drive.
    if car.currentTankAmount == 0:
        print("Without any gas in the tank, you are unable to make your journey. You have become a figure of ridicule within the community.")
    else:
        #This print statement just puts out the general information we figured out earlier in this main function.
        print("The", car.model, "travels at a speed of", vehicleSpeed, "mph")
        #This prints all the gas tank information.
        gasTank() 
        #This prints all of the right of way information. 
        fiveRightofWayLaws() 

#This calls the original main function, and executes all of the tasks. 
everything() 
