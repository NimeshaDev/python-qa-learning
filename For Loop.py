for letter in "testcases":
    print(letter) #the letter variable write down all the letters from the loop


friends= ["tim", "brayn" ,"shiya"]
for friend in friends: # this is how it works with the array
    print(friend)

for index in range(10): #this is print everything in the range 10 but not 10
    print(index)

for index in range(3,10): #this is print everything in the range between the 3 - 10 but not 10
    print(index)

friends= ["tim", "brayn" ,"shiya"]
for index in range(len(friends)): # this is how it works with the array and index
    print(friends[index])