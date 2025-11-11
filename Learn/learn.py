thisList = ["Mangos","Banana","Orange","Cherry"]
if "Apple" in thisList:
  print("Apple is in the list")
else:
  print("Not on the list")
thisList[2]="Apple"
print(thisList[2])

#Change range of items

thisList[1:3] = ["kiwi","watermelon"]
print(thisList)


#Insert Items
thisList.insert(2,"blackcurrant")
print(thisList)

#Extend List
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

#
thisTurple = ("Mango", "pineapple", "papaya")
thisList.extend(thisTurple)
print(thisList)

#Remove Specified Item
thisList.remove("mango")
print(thisList)

#Remove Specified Index
thisList.pop(4)
print(thisList)

#Use del to delete item
del thisList[2]
print(thisList)

