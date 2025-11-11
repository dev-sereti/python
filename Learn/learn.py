#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newFruits = []

for x in fruits:
  if "a" in x:
    newFruits.append(x)

print(newFruits)