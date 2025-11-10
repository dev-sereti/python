my_string = "   Hello World   "

# Case conversion
print(my_string.upper())      # Output: "   HELLO WORLD   "
print(my_string.lower())      # Output: "   hello world   "
print(my_string.strip().capitalize()) # Output: "Hello world"

# Removing whitespace
cleaned_string = my_string.strip()
print(cleaned_string)         # Output: "Hello World"

# Splitting and joining
words = cleaned_string.split()
print(words)                  # Output: ['Hello', 'World']
joined_string = "-".join(words)
print(joined_string)          # Output: "Hello-World"

# Searching and replacing
print(cleaned_string.find("World"))  # Output: 6
print(cleaned_string.replace("World", "Python")) # Output: "Hello Python"