friends= ["TOM","MIKE","RYAN","BRYAN"]
lucky_Numbers=[12, 18, 24, 27, 32]
lucky_Numbers.extend(friends) # we can two list in the last together by using extend function
print(lucky_Numbers)
friends.append("NIsha") #this is helps to add new elements to the list at the end
friends.insert(1, "UMI") #insert for the index
print(friends)
friends.remove("UMI") #remove element form the list
print(friends)
friends.pop()# remove the last element from the list
print(friends)
print(friends.index("MIKE")) # find the index of the relevant element
print(friends.count("MIKE")) #count the number of elements of the list
friends.sort() #sort the list
print(friends)
friends.reverse() #reverse the list
print(friends)
friends1= friends.copy() # we can create a copy of the list
print(friends1)
friends.clear() # clear all list
print(friends)

