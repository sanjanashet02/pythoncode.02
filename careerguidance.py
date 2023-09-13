"""
career guidance project
app developer
web developer
data science
cyber security
"""
n=input("enter the career you wish").lower()
if n=="app_developer":
    n2=input("select native or hybrid")
    if n2=="native":
        print("you can learn java,swift")
    elif n2=="hybrid":
        print("you can learn flutter ,react native")
    else:
        print("invalid")
elif n=="web_developer":
     n3=input("select frontend or backend")
     if n3=="frontend":
         print("you can learn html")
     elif n3=="backend":
         print("you can learn javascript , ruby ,java ")
     else:
         print("invalid")
elif n=="data_science":
    print("you can learn python")
elif n=="cyber_security":
    print("you can learn networking")
else:
    print("invalid")