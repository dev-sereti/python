#Sort List Alphanumerically

fruits = ["apple","Kiwi", "mango","banana", "cherry"]

fruits.sort()
print(fruits)
#Sort Descending
fruits.sort(reverse=True)
print(fruits)

#Case Insensitive Sort
fruits.sort(key=str.lower)
print(fruits)