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

day = "Sunday"
if day == "Saturday" or "Sunday":
    print("It is a weekend")
else:
    print("Weekday")
    
    

    