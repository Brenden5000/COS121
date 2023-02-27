#This asks the user to input the amount of cookies, and stores it as an integer. 
cookies = int(input("How many cookies are each baker going to bake? "))
print(cookies)

#This asks the user to input the amount of bakers, and stores it as an integer. 
bakers = int(input("How many bakers are in the tent this week? "))
print(bakers)

#This multiplies the amount of cookies each baker will baking by the amount of bakers to find the total amount of cookies being baked.
totalCookies = (int(cookies) * int(bakers))


#This calculates the total amount of butter needed for all the cookies, using the provided recipe and batch count with a buffer.
totalButter = ((int(totalCookies) // 24) + int(bakers))
#This calculates the total amount of eggs needed for all the cookies, using the provided recipe and batch count with a buffer.
totalEggs = ((int(totalCookies) // 12) + int(bakers)) 
#This calculates the total amount of flour needed for all the cookies, using the provided recipe and batch count with a buffer.
totalFlour = ((int(totalCookies) // 8) + (int(bakers) * 2)) 
#This calculates the total amount of sugar needed for all the cookies, using the provided recipe and batch count with a buffer.
totalWhiteSugar = ((int(totalCookies) // 24) + (int(bakers))) 
#This calculates the total amount of brown sugar needed for all the cookies, using the provided recipe and batch count with a buffer.
totalBrownSugar = ((int(totalCookies) // 24) + (int(bakers))) 
#This calculates the total amount of chocolate chips needed for all the cookies, using the provided recipe and batch count with a buffer.
totalChocolateChips = ((int(totalCookies) // 12) + int(bakers)) 


#This is the print function that gives the user the answer.
print ("There are", bakers, "in the booth baking", cookies, "each, and", totalCookies, "in all. You will need", totalButter, "cups of butter,", totalEggs, "eggs,", totalFlour, "cups of flour,", totalWhiteSugar, "cups of white sugar,", totalBrownSugar, "cups of brown sugar, and", totalChocolateChips, "cups of chocolate chips.")








