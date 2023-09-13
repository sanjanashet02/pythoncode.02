"""
Q.1 Write a program that asks the user for their favorite color and prints out a message 

depending on the color they choose. For example: "Red is a bold color!" or "Blue is a

calm color!". Use at least 3 different colors in your program.
"""
col=input("ENTER YOUR FAVOURITE COLOUR:")
if col == "red" or " RED":
    print("RED IS BOLD COLOUR")
elif col=="blue" or "BLUE":
    print("BLUE IS CALM COLOUR")
elif col=="white" or "WHITE":
    print("WHITE IS PEACFUL COLOUR")
else:
    print("INVALID COLOUR")



"""
Q.2 Write a program that asks the user for a number and prints out whether the

number is positive, negative, or zero.
"""
n=int(input("ENTER THE NUMBER"))
if n>0:
    print(f" {n} is positive")
elif n <0:
    print(f" {n} is negative")
else:
    print(f" NUMBER IS 0")


"""
Q.3 Write a program that asks the user for a letter grade (A, B, C, D, or F) and prints 

out the corresponding GPA. For example, an A should print out as 4.0, a B as

3.0, and so on."""
grade=input("enter your grade")
if grade=='A':
    print("YOUR GPA IS 4.0")
elif grade=='B':
     print("YOUR GPA IS 3.0")
elif grade=='C':
     print("YOUR GPA IS 2.0")
elif grade=='D':
     print("YOUR GPA IS 1.0")
elif grade=='F':
     print("YOUR GPA IS 0")
else:
     print("INVALID CHOICE")


"""
Q.4 Ask 4 ages from user (age1, age2, age3, age4). Print out which age is

the youngest.
"""
a1=int(input("ENTER THE AGE 1:"))
a2=int(input("ENTER THE AGE 2:"))
a3=int(input("ENTER THE AGE 3:"))
a4=int(input("ENTER THE AGE 4:"))
if a1<a2 and a1<a3 and a1<a4:
     print(f"a1({a1}) is youngest")
elif a2<a1 and a2<a3 and a2<a4:
     print(f"a2({a2}) is youngest")
elif a3<a1 and a3<a2 and a3<a4:
     print(f"a3({a3}) is youngest")
else:
     print(f"a4({a4}) is youngest")
     
     
#Q.5 Python Program to Generate a Random Number (take help of google)   
import random
rnum=random.randint(1,50)
print("THE RANDOM NUMBER IS:")
print(rnum)

     










