import random

ellenfel = input("Gép vagy játékos ellen játszol? (g, j): ")

# lapok kiosztása, mindenki kap 2-2 lapot (1-11 közötti értékek, mint a blackjack-ben)
sajatlap1 = random.randint(1, 11)
sajatlap2 = random.randint(1, 11)
sajatoosszeg = sajatlap1 + sajatlap2

print(f"A te lapjaid: {sajatlap1} és {sajatlap2} (összesen: {sajatoosszeg})")

if ellenfel == "g":
    # gép ellen
    geplap1 = random.randint(1, 11)
    geplap2 = random.randint(1, 11)
    gepoosszeg = geplap1 + geplap2

    print(f"A gép lapjai: {geplap1} és {geplap2} (összesen: {gepoosszeg})")

    if sajatoosszeg > 21:
        print("Túlcsordultál! A gép nyert.")
    elif gepoosszeg > 21:
        print("A gép túlcsordult! Te nyertél.")
    elif sajatoosszeg > gepoosszeg:
        print("Te nyertél!")
    elif gepoosszeg > sajatoosszeg:
        print("A gép nyert!")
    else:
        print("Döntetlen!")

else:
    jatekoslap1 = random.randint(1, 11)
    jatekoslap2 = random.randint(1, 11)
    jatekososszeg = jatekoslap1 + jatekoslap2

    print(f"A másik játékos lapjai: {jatekoslap1} és {jatekoslap2} (összesen: {jatekososszeg})")

    if sajatoosszeg > 21:
        print("Túlcsordultál! Az ellenfél nyert.")
    elif jatekososszeg > 21:
        print("Az ellenfél túlcsordult! Te nyertél.")
    elif sajatoosszeg > jatekososszeg:
        print("Te nyertél!")
    elif jatekososszeg > sajatoosszeg:
        print("Az ellenfél nyert!")
    else:
        print("Döntetlen!")
