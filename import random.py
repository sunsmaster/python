import random

dator_poäng = 0
spelare_poäng = 0
val = ["sten", "sax", "påse"]

print("Välkommen till sten sax påse!")

while dator_poäng < 3 and spelare_poäng < 3:

    dator_val = random.choice(val)

    spelare_val = input("sten, sax eller påse? ")

    print("dator valde" + dator_val)

    if dator_val == spelare_val:
        print("Ni valde samma! Kör igen.")
    elif (spelare_val == "sten" and  dator_val == "sax") or (spelare_val == "sax" and dator_val == "påse") or (spelare_val == "påse" and dator_val == "sten"):
        spelare_poäng += 1
        print("Du fick poäng!")
    else:
        dator_poäng += 1
        print("Datorn fick poäng!")


if dator_poäng > spelare_poäng:
    print("Dator vann spelet! Försök igen.")
else:
    print("Du vann spelet! Bra jobbat!")