# phy=int(input("enter the physics marks"))
# chem=int(input("enter the chemistry marks"))
# if phy >= 33  and chem >= 33:
#     print("PASS")
# else:
#     print("FAIL")


"""
ASK AGE FROM USER 
AGE>80 ADULT
13-17 TEENAGER
13 BELOW CHILD
"""
age=int(input("enter the age"))
if age >= 18:
    print("ADULT")
elif age > 13 and age <=17:
    print("TEENAGER")
elif age>0 and age <=13:
    print("CHILD")
else:
    print("invalid number")