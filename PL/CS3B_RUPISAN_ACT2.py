'''Python activity that prints info'''

#Student Full name, Address, Age, and Favorite Number
firstName = "Christian"
middleName = "Daleja"
lastName = "Rupisan"
address = "Darapidap, Candon City, Ilocos Sur"
age = 20
favoriteNumOne = 12
favoriteNumTwo = 2

#Print Student Full name, Address, Age, and Favorite Number
print(firstName, middleName, lastName)
print(address)
print(age)
print(favoriteNumOne)
print(favoriteNumTwo)
print(favoriteNumOne + favoriteNumTwo)
print(firstName, middleName, lastName, address, age, favoriteNumOne, favoriteNumTwo)

#Concatenation
print(firstName + middleName + lastName)

#Collection of three animals
animals = ["Parrot", "Shark", "Cow"]

#print the middle animal
print(animals[1])

#Actors
actorOne = "Ang ghwapo ko diba? said friend 'Macayan'"
actorTwo = 'Thank you! said "Macayan Puyot"'
#erros if double quotation or double single quotation
print (actorOne, actorTwo)

#String are also considered as collection
print(actorOne[3])

#Calculate Length
#A code that gets the length of Actor 1 and Actor 2

#Adding the lengths of two actor then minus the length addrtess

actorLetter = len(actorOne) + len (actorTwo)

#Print the result
print(actorLetter - len(address))