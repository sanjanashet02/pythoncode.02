# # 1. output of the expression  
# print(-18 // 4)


# # 2. output of print(2 * 3 ** 3 * 4) 
# print(2 * 3 ** 3 * 4)


# 3. output of print(10 - 4 * 2) 
# print(10 - 4 * 2)

# # 4. python program to find minimum of two numbers
# a=int(input("enter the first number:\n"))
# b=int(input("enter the second number:\n"))
# print("the minimum of two numbwers is:")
# if a<b:
#     min=a
#     print(a)
# else:
#     min=b
#     print(b)


# """ 5.python program to convert temperature from Celsius to Fahrenheit. 

# Ask Celsius from User
# """
# temp=float(input("enter the temperature in celsius:\n"))
# print("the temperature in fahrenheit is:")
# f=float((9/5*temp)+32)
# print(f)


# # 6. Calculate the Average.
# a=float(input("enter the first number:"))
# b=float(input("enter the second number:"))
# c=float(input("enter the third number:"))
# sum=float(a+b+c)
# print("the average of three numbers is :")
# avg=sum/3
# print(avg)


""".7 Ask number of games played in a tournament. Ask the user number of

games won and number of games loss. Calculate number of tie and total

Points. (1 win= 4 points, 1 tie =2 points)
"""
n=int(input("enter the number of games played"))
a=int(input(" enter the number of games won"))
b=int(input("enter the number of games lost"))


games_tied=n-a-b
points=(a*4) +(games_tied*2)
print(f"number of ties is: {games_tied} and total points is {points}")


    




    
