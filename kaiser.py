# Diese Version von Kaiser dreht sich darum alles in einem Aufruf zu schreiben

from random import uniform, randint, choice


runde = 1
spieljahr = 1700
titel = "Baron"
bevoelkerung_gesamt = 1000
geld = 20000
muehlen_anzahl = 2
maerkte_anzahl = 1
land_anzahl = 100
korn_vorhanden = 10000


def spiel():
    vorname = "Tobi"
    global titel, bevoelkerung_gesamt, geld, muehlen_anzahl, maerkte_anzahl, land_anzahl, korn_vorhanden
    kornpreis_kaufen = randint(30, 60)
    kornpreis_verkaufen = randint(20, 50)
    landpreis_kaufen = randint(70, 100)
    landpreis_verkaufen = randint(50, 80)

    print("------------------")
    print("Runde:", runde)
    print(titel, vorname + " im Jahre", spieljahr)
    print()
    print("Bevölkerung:", int(bevoelkerung_gesamt), "Geld:", int(geld), "Landbesitz:", land_anzahl, "Kornmühlen:",
          muehlen_anzahl, "Märkte:", maerkte_anzahl)
    print()
    print("Vorhandenes Korn:", int(korn_vorhanden))
    print(" Benötigtes Korn")
    print("             Min:", int(bevoelkerung_gesamt * 0.5))
    print("    Durchschnitt:", int(bevoelkerung_gesamt * 0.8))
    print("             Max:", int(bevoelkerung_gesamt * 1.1))
    print()
    print("Kornpreise:       Landpreise:")
    print("   Einkauf:", kornpreis_kaufen, "      Einkauf:", landpreis_kaufen)
    print("   Verkauf:", kornpreis_verkaufen, "      Verkauf:", landpreis_verkaufen)
    print()

    eingabe = input("Möchten sie Korn/Land kaufen (k) oder verkaufen (v) oder Nichts (jede andere Taste) tun?")
    if eingabe == "k":
        kaufwahl = input("Soll Korn (k) oder Land (l) gekauft werden?")
        if kaufwahl == "k":
            menge = int(input("Wie viel Korn möchten sie kaufen?"))
            if geld >= menge * kornpreis_kaufen:
                korn_vorhanden += menge
                geld -= menge * kornpreis_kaufen
            else:
                print("Das können sie sich leider nicht leisten!")
        else:
            menge = int(input("Wie viel Land möchten sie kaufen?"))
            if geld >= menge * landpreis_kaufen:
                land_anzahl += menge
                geld -= menge * landpreis_kaufen
            else:
                print("Das können sie sich leider nicht leisten!")

    elif eingabe == "v":
        verkaufwahl = input("Soll Korn (k) oder Land (l) vergekauft werden?")
        if verkaufwahl == "k":
            menge = int(input("Wie viel Korn möchten sie verkaufen?"))
            if korn_vorhanden >= menge:
                korn_vorhanden -= menge
                geld += menge * kornpreis_verkaufen
            else:
                print("Soviel Korn besitzen sie leider nicht!")
        else:
            menge = int(input("Wie viel Land möchten sie verkaufen?"))
            if land_anzahl >= menge:
                land_anzahl -= menge
                geld += menge * landpreis_verkaufen
            else:
                print("Soviel Land besitzen sie leider nicht!")

    else:
        print("Es wurde nicht gehandelt.")

    eingabe = input("Möchten sie Kornmühlen (k) oder Märkte (m) errichten oder Nichts (jede andere Taste) ?")

    if eingabe == "k":
        geld -= 1000
        muehlen_anzahl += 1
        print("Eine Mühle gekauft.")
        print()

    elif eingabe == "m":
        geld -= 2000
        maerkte_anzahl += 1
        print("Einen Marktplatz gekauft.")
        print()

    else:
        print("Kein Kauf getätigt.")
        print()

    print("Wie viel Korn dürfen die Bürger konsumieren?")
    korn_auswahl = input("Minimum = 1 / Durchschnitt = 3 / Maximum = 5  ")

    while korn_auswahl != "1" and korn_auswahl != "3" and korn_auswahl != "5":
        korn_auswahl = input("Bitte erneut eingeben: Minimum = 1 / Durchschnitt = 3 / Maximum = 5 ")

    if korn_auswahl == "1":
        korn_vorhanden -= bevoelkerung_gesamt * 0.5
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.1, 0.2)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.02, 0.075)
    elif korn_auswahl == "3":
        korn_vorhanden -= bevoelkerung_gesamt * 0.8
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.075, 0.125)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.075, 0.125)
    else:
        korn_vorhanden -= bevoelkerung_gesamt * 1.1
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.02, 0.075)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.1, 0.2)

    bevoelkerung_gesamt = bevoelkerung_gesamt - bevoelkerung_gestorben + bevoelkerung_geboren
    geld += bevoelkerung_gesamt * muehlen_anzahl * 0.05 + bevoelkerung_gesamt * maerkte_anzahl * 0.1

    korn_vorhanden += muehlen_anzahl * 300 * choice([1.5, 1.2, 1, 0.8, 0.5])


while runde <= 10:
    spiel()
    runde += 1
    spieljahr += 1
