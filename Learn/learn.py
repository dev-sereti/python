#Change Tuple Values
fruits = ("apple","banana","mango","orange","cherry")
newFruits = list(fruits)
newFruits.append("grapes")
newFruits.remove(newFruits[3])
fruits = tuple(newFruits)

print(fruits)