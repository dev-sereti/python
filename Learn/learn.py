#Conditional Statements
#--- If statement ---

Age = 8
if Age>=18: 
    print("Not Under Age")
else:
    print("Under age")

#if-elif-else Statement

Score = 5.5

if Score>=90:
    print("Grade: A")
elif Score>=80:
    print("Grade: A-")
elif Score>=70:
    print("Grade: B+")
elif Score>=60:
    print("Grade: B")
elif Score>=50:
    print("Grade:B-")
elif Score>=40:
    print("Grade: C+")
elif Score>=30:
    print("Grade: C-")
else:
    print("Fail")


#Comparison Operators

x=20
y=88

#Equal
if x==y:
    print("Equal")

#Not equal
if x!=y:
    print("Not equal")
    
#Greater than
if x>y:
    print("X is greater than Y")
    
#Less than
if x<y:
    print("X is less than Y")

# Greater than or equal to
if x>=10:
    print("X is greater")
    
#Less than equal to 

if x<=10:
    print ("X is less than 10")
    
#Logical Operators
#and - Both conditions must be True

age=25
has_licence=True

if age>25 and has_licence:
    print("You can drive")

#At least one condition must be True

day = "Monday"
if day == "Saturday" or "Sunday":
    print("It is a weekend")
else:
    print("Weekday")
    
#Nested Conditionals
age = 20
has_ticket = True

if age>=18:
    if has_ticket:
        print("Allowed to attend")
    else:
        print("You need a ticket")
else:
    print("Too young")
    
#Membership Operators
#in - Check if value exists in sequence

fruits = ["Apples","Oranges","Bananas","Cherry"]

if "Apples" in fruits:
    print("Apples are in the store")
    
#Check substring
Greetings = "Hello Sereti"

if "llo" in Greetings:
    print("You have greetings")
    
#not in - Check if value doesn't exist
if "mango" not in fruits:
    print("Get some Mangoes")

#Identity Operators
x=None
if x is None:
    print("x is None")

#is not 
y=[1,2.3]

if y is not None:
    print("Y has values")
    
#Ternary Operator (Conditional Expression)

myAge = 3
status = "Adult" if myAge>= 18 else "Minor"
print(status)

#Multiple Conditions
if myAge>10 and myAge<30:
    print("Your age is between 10 and 30")
else:
    print("Your age is below 10 or more than 30")
    
#  Match-Case Statement

def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown Error"
print(http_status)

#Loops

