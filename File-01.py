# # Topics : Basics
# # Output function
# # variables
# # Data types
# # input and output
# # Type casting and type of function
# # Arithmetic operations
# # Control-flow : conditional sentence
# # Control-flow : Loops-While
# # Control-flow : Loops-For
# # Breaks and continue

# Output function


print("Hello world!")

# variables

x = 50
var_one = "Who's gonna carry the boats?"

# Data types

xc = 50 #Integer or int
cx = 50.435 #Float or flt
xcv = "Hello!" #String or str
vcx = False #Boolean or bool

# input and output

x = input("Enter your name : ")
print("Hello",x)

# Type casting and type of function
x = int(input("Enter a number : "))
print("Square of the given number is : ",x*x)

x = 54
print(type(x))

# Arithmetic operations

x = 50
y = 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)


# Control-flow : conditional sentence

print("Are u eligible to vote?")
xc = int(input("Enter your age : "))
if xc <=18 :
    print("Not eligible")
elif xc == 18 :
    print("Yep! It's time for you to vote!")
elif xc >= 18 : 
    print("YOU'RE ELIGILBE TO VOTE")
else:
    print("Invalid code!")
    

# Control-flow : Loops-While

x = 0
while x <=12 : 
    print(x)
    x += 1
    
# Control-flow : Loops-For

for i in range(1,11) :
    print(i)
    i += 1
    
# # Breaks and continue

x = 0
while x == 0 : 
    print("Hello")
    break

for i in range(1,11) :
    print(i)
    i += 1
    continue