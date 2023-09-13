"""
BILL CALCULATOR
ENTER YOUR BILLING AMOUNT
50000 ABOVE 40% DISCOUNT
40000 - 49999 30% DISCOUNT
20000-39999 20% DISCOUNT
0-19999 0% DISCOUNT

"""

amt=int(input("enter the amount:"))

if amt >= 50000:
    disc1=amt*(40/100)
    amt1=amt-disc1
    print("YOU GOT 40% DISCOUNT")
    print(f"YOUR AMOUNT IS {amt1}")
elif amt>=40000 and amt <49999:
    disc2=amt*(30/100)
    amt2=amt-disc2
    print("YOU GOT 30% DISCOUNT")
    print(f"YOUR AMOUNT IS {amt2}")
elif amt>=20000 and amt <39999:
    disc3=amt*(20/100)
    amt3=amt-disc3
    print("YOU GOT 20% DISCOUNT")
    print(f"YOUR AMOUNT IS {amt3}")
elif amt>=0000 and amt <19999:
    disc4=0
    amt4=amt-disc4
    print("YOU GOT 0% DISCOUNT")
    print(f"YOUR AMOUNT IS {amt4}")
else:
    print("invalid choice")




