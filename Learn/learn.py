#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruits = []

for i in fruits:
  if "a" in i:
    newFruits.append(i)
print(newFruits)
