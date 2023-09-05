import random
print("\n-------------------------------------------------------------------")
print(".:gissa talet :.\n\n")
print("gissa ett tal mellan 1 och 10 och pröva lyckan, du får 3st försök!\n")
slumptal = random.randint(1,10)
#print (slumptal)
i = 0
hittat = False
#loop
while i < 3:
    gissatal =input ("mata in tal: ")

    if  slumptal == int(gissatal):
        hittat = True
        print("\n rätt svar! \n")
        break

    i += 1

    if hittat:
        print("\nBra jobbat, här får du fem kr")
    else:
        print("\nBättre lycka nästa gång")
print("\n---------------------------------------------------------------------")