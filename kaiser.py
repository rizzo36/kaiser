# Diese Version von Kaiser dreht sich darum alles aufzudröseln und wenn möglich ohne global und nur mit
# einem return zu arbeiten


from random import uniform, randint, choice


titel = "Baron"
vorname = "Tobi"
spieljahr = 1700
runde = 1
bevoelkerung_gesamt = 1000
geld = 20000
muehlen_anzahl = 2
maerkte_anzahl = 1
land_anzahl = 100
korn_vorhanden = 10000


def anzeige():
    global kornpreis_kaufen, kornpreis_verkaufen, landpreis_kaufen, landpreis_verkaufen
    kornpreis_kaufen = randint(30, 60)
    kornpreis_verkaufen = randint(20, 50)
    landpreis_kaufen = randint(70, 100)
    landpreis_verkaufen = randint(50, 80)
    print("------------------")
    print("Runde:", runde)
    print(titel, vorname + " im Jahre", spieljahr)
    print()
    print("Bevölkerung:", int(bevoelkerung_gesamt), "Geld:", int(geld), "Landbesitz:", land_anzahl, "Kornmühlen:", muehlen_anzahl, "Märkte:", maerkte_anzahl)
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


def eingabe_kauf_verkauf():
    eingabe = input("Möchten sie Korn/Land kaufen (k), verkaufen (v) oder Nichts (jede andere Taste) tun?")
    return eingabe


def kaufwahl_kauf_verkauf():
    kaufwahl = input("Soll Korn (k) oder Land (l) gehandelt werden?")
    return kaufwahl


def menge_kauf_verkauf():
    menge = input("Wie viel soll gehandelt werden?")
    if menge == "":
        return menge
    else:
        return int(menge)


def geld_kauf_verkauf(geld):
    if eingabe == "k":
        if kaufwahl == "k":
            if geld >= menge * kornpreis_kaufen:
                geld -= menge * kornpreis_kaufen
                return geld
            else:
                print("Das können sie sich leider nicht leiten!")
                return geld
        else:
            if geld >= menge * landpreis_kaufen:
                geld -= menge * landpreis_kaufen
                return geld
            else:
                print("Das können sie sich leider nicht leisten!")
                return geld

    elif eingabe == "v":
        if kaufwahl == "k":
            if korn_vorhanden >= menge:
                geld += menge * kornpreis_verkaufen
                return geld
            else:
                print("Soviel Korn besitzen sie leider nicht!")
                return geld
        else:
            if land_anzahl >= menge:
                geld += menge * landpreis_verkaufen
                return geld
            else:
                print("Soviel Land besitzen sie leider nicht!")
                return geld

    else:
        print("Es wurde nicht gehandelt.")
        return geld


def korn_kauf_verkauf(korn_vorhanden):
    if eingabe == "k":
        if kaufwahl == "k":
            korn_vorhanden += menge
            return korn_vorhanden
        else:
            return korn_vorhanden

    elif eingabe == "v":
        if kaufwahl == "k":
            korn_vorhanden -= menge
            return korn_vorhanden
        else:
            return korn_vorhanden

    else:
        return korn_vorhanden


def land_kauf_verkauf(land_anzahl):
    if eingabe == "k":
        if kaufwahl == "k":
            return land_anzahl
        else:
            land_anzahl += menge
            return land_anzahl

    elif eingabe == "v":
        if kaufwahl == "k":
            return land_anzahl
        else:
            land_anzahl -= menge
            return land_anzahl

    else:
        return land_anzahl


def auswahl_korn_markt():
    auswahl = input("Möchten sie Kornmühlen (k) oder Märkte (m) kaufen oder Nichts (jede andere Taste)?")
    return auswahl


def geld_auswahl_erweiterung(geld):
    if auswahl == "k":
        geld -= 1000
        print("Eine Mühle gekauft.")
        print()
        return geld

    elif auswahl == "m":
        geld -= 2000
        print("Einen Marktplatz gekauft.")
        print()
        return geld

    else:
        print("Kein Kauf getätigt.")
        print()
        return geld


def muehlen_auswahl_erweiterung(muehlen_anzahl):
    if auswahl == "k":
        muehlen_anzahl += 1
        return muehlen_anzahl

    else:
        return muehlen_anzahl


def maerkte_auswahl_erweiterung(maerkte_anzahl):
    if auswahl == "m":
        maerkte_anzahl += 1
        return maerkte_anzahl

    else:
        return maerkte_anzahl


def korn_auswahl_konsum():
    print("Wie viel Korn dürfen die Bürger konsumieren?")
    korn_auswahl = input("Minimum = 1 / Durchschnitt = 3 / Maximum = 5  ")
    if korn_auswahl != "1" and korn_auswahl != "3" and korn_auswahl != "5":
        korn_auswahl = input("Bitte erneut eingeben: Minimum = 1 / Durchschnitt = 3 / Maximum = 5")
        return korn_auswahl
    else:
        return korn_auswahl


def errechne_korn_vorhanden(korn_vorhanden):
    if korn_auswahl == "1":
        korn_vorhanden -= bevoelkerung_gesamt * 0.5
        return korn_vorhanden

    elif korn_auswahl == "3":
        korn_vorhanden -= bevoelkerung_gesamt * 0.8
        return korn_vorhanden

    else:
        korn_vorhanden -= bevoelkerung_gesamt * 1.1
        return korn_vorhanden


def errechne_bevoelkerung_gesamt(bevoelkerung_gesamt):
    if korn_auswahl == "1":
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.1, 0.2)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.02, 0.075)
        bevoelkerung_gesamt = bevoelkerung_gesamt - bevoelkerung_gestorben + bevoelkerung_geboren
        return bevoelkerung_gesamt

    elif korn_auswahl == "3":
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.075, 0.125)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.075, 0.125)
        bevoelkerung_gesamt = bevoelkerung_gesamt - bevoelkerung_gestorben + bevoelkerung_geboren
        return bevoelkerung_gesamt

    else:
        bevoelkerung_gestorben = bevoelkerung_gesamt * uniform(0.02, 0.075)
        bevoelkerung_geboren = bevoelkerung_gesamt * uniform(0.1, 0.2)
        bevoelkerung_gesamt = bevoelkerung_gesamt - bevoelkerung_gestorben + bevoelkerung_geboren
        return bevoelkerung_gesamt


def errechne_geld(geld):
    geld += bevoelkerung_gesamt * muehlen_anzahl * 0.05 + bevoelkerung_gesamt * maerkte_anzahl * 0.1
    return geld


def erzeuge_korn(korn_vorhanden):
    korn_vorhanden += muehlen_anzahl * 300 * choice([1.5, 1.2, 0.8, 0.5])
    return korn_vorhanden


while runde <= 10:
    anzeige()
    eingabe = eingabe_kauf_verkauf()
    if eingabe == "k" or eingabe == "v":
        kaufwahl = kaufwahl_kauf_verkauf()
        menge = menge_kauf_verkauf()
    else:
        pass

    geld = int(geld_kauf_verkauf(geld))
    korn_vorhanden = korn_kauf_verkauf(korn_vorhanden)
    land_anzahl = land_kauf_verkauf(land_anzahl)
    auswahl = auswahl_korn_markt()
    geld = int(geld_auswahl_erweiterung(geld))
    muehlen_anzahl = muehlen_auswahl_erweiterung(muehlen_anzahl)
    maerkte_anzahl = maerkte_auswahl_erweiterung(maerkte_anzahl)
    korn_auswahl = korn_auswahl_konsum()
    korn_vorhanden = errechne_korn_vorhanden(korn_vorhanden)
    bevoelkerung_gesamt = int(errechne_bevoelkerung_gesamt(bevoelkerung_gesamt))
    geld = errechne_geld(geld)
    korn_vorhanden = erzeuge_korn(korn_vorhanden)

    runde += 1
    spieljahr += 1
