

def everything():
    fullName = ["Tom Brady", "Aaron Rodgers", "Joe Montana", "Dan Marino", "Peyton Manning"]
    firstYear = ["2000", "2005", "1979", "1983", "1998"] 
    lastYear = ["still playing", "still playing", "1994", "1999", "2015"]
    MVPs = ["2007, 2010 & 2017", "2011, 2014, 2020 & 2021", "1989 & 1990", "1984", "2003, 2004, 2008, 2009 & 2013"]
    championYears = ["2001, 2003, 2004, 2014, 2016 & 2018", "2010", "TBA", "TBA"]
    passingYards = ["86,462", "56,957", "40,551", "61,361", "71,940"]
    touchdowns = ["632", "460", "273", "420", "539"]
    interceptions = ["204", "96", "139", "252", "251"]
    def nameList(fullName): 
        inputNames = input("Please enter the first and last name of the quarterback. Type stop to end the process: ")
        while inputNames != "end":
            fullName.append(inputNames)
            inputNames = input("Please enter the first and last name of the quarterback. Type stop to end the process: ")
        return fullName
    def firstYearList(firstYear): 
        inputFirstYear = input("Please enter the year this quarterback was drafted: ")
        while inputFirstYear != "end":
            firstYear.append(inputFirstYear)
            inputFirstYear = input("Please enter the year this quarterback was drafted: ")
        return firstYear
    def lastYearList(lastYear): 
        inputLastYear = input("Please input this quarterbacks final year. If they are still playing, type 'still playing'. Type stop end the process: ")
        while inputLastYear != "end": 
            lastYear.append(inputLastYear)
            inputLastYear = input("Please input this quarterbacks final year. If they are still playing, type 'still playing'. Type stop end the process: ")
        return lastYear
    def mvpsList(MVPs): 
        inputMVPs = input("Please input the years this quarterback won the MVP award. Enter them all as one entry. Type 'end' to stop: " )
        while inputMVPs != "end": 
            MVPs.append(inputMVPs)
            inputMVPs = input("Please input this quarterbacks final year. If they are still playing, type the current year. If they never won the award, please type 'none' Type stop end the process: ")
        return MVPs
    def calculation(fullName, firstYear, lastYear, MVPs): 
        fullName = nameList(fullName)
        firstYear = firstYearList(firstYear)
        lastYear = lastYearList(lastYear)
        MVPs = mvpsList(MVPs)

        #This asks the user which quarterback they would like to print the information of.
        chosenName = input("Who do you want to find the data of? ")
        #This finds which index the entry name has, and sets it the variable position. This way, we can use position to
        #print that quarterbacks corresponding information from different lists.
        position = fullName.index(chosenName)
        chosenFirstYear = firstYear[position]
        chosenLastYear = lastYear[position]
        chosenMVPs = MVPs[position]
        
        #Because not everyone is still playing, this if statement exists to make the grammar of the print statement correct. 
        if chosenLastYear == "still playing": 
            lastYearPhrase = "and is still currently playing."
        else: 
            lastYearPhrase = "and played until"
        if chosenMVPs == "none":
            mvpPhrase = "He did not win the MVP award throughout his career."
        else:
            mvpPhrase = "He won the MVP in"

        #So some grammatical stuff happens. Because chosenLastYear is equal to 'still playing' for active quarterbacks, 
        #when the print statement is called normally, it would normally say "and played through the X season." However, because
        #it's set to 'still playing', it would say "and is currently still playing. still playing". This if statement exists to fix that
        #grammatical error by removing the chosenLastYear variable depending on whether it is set to 'still playing' or not.
        if chosenLastYear == "still playing":
            print(chosenName, "was drafted in", chosenFirstYear, lastYearPhrase, mvpPhrase, chosenMVPs)
        else:
            print(chosenName, "was drafted in", chosenFirstYear, lastYearPhrase, chosenLastYear, mvpPhrase, chosenMVPs)
    calculation(fullName, firstYear, lastYear, MVPs)







everything()








