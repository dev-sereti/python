#Python Scope

#Local Scope

def localScope():
    age = 26
    print (age)
localScope()


#Global scope
x = 300

def myfunc():
  print(x)
myfunc()
print(x)