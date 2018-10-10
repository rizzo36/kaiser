# added function "check_ob_digit" to check if input is int or string and convert it--> deleted 16 lines of code
# fixed titel progression.
# descending is not possible anymore. only 1 ascend per turn

from random import uniform, randint, choice


game_continue = True
titel_tupel = ("Baron", "Graf", "Fürst", "Herzog", "Kurfürst", "Großherzog", "König", "Kaiser")


anzahl_spieler_str = input("Wie viele Spieler?")
while anzahl_spieler_str.isdigit() is False:
    anzahl_spieler_str = input("Bitte erneut eingeben: Wie viele Spieler?")
anzahl_spieler = int(anzahl_spieler_str)

spieler_liste = []
for spieler in range(anzahl_spieler):
    print("Spieler ", spieler)
    spieler_name = input("Name: ")
    print()
    spieler_liste.append(spieler_name)


def generiere_preise():
    kornpreis_kaufen = randint(3, 6)
    kornpreis_verkaufen = randint(2, 5)
    landpreis_kaufen = randint(70, 100)
    landpreis_verkaufen = randint(50, 80)
    return kornpreis_kaufen, kornpreis_verkaufen, landpreis_kaufen, landpreis_verkaufen


def auswahl_konsum():
    print("Wie viel Korn dürfen die Bürger konsumieren?")
    korn_auswahl = input("Minimum = 1 / Durchschnitt = 3 / Maximum = 5  ")
    while korn_auswahl != "1" and korn_auswahl != "3" and korn_auswahl != "5":
        korn_auswahl = input("Bitte erneut eingeben: Minimum = 1 / Durchschnitt = 3 / Maximum = 5 ")
    return korn_auswahl


def check_ob_digit(menge_str):      # Abfrage wurde stets wiederholt also in Funktion ausgelagert
    while menge_str.isdigit() is False:
        menge_str = input("Bitte erneut eingeben: Wie viel möchten sie handeln?")
        print()
    menge = int(menge_str)
    return menge


class Game(object):
    def __init__(self, vorname, runde, spieljahr, titel, bevoelkerung_gesamt,
                 geld, muehlen_anzahl, maerkte_anzahl, land_anzahl, korn_vorhanden, palast_elemente):
        self.vorname = vorname
        self.runde = runde
        self.spieljahr = spieljahr
        self.titel = titel
        self.bevoelkerung_gesamt = bevoelkerung_gesamt
        self.geld = geld
        self.muehlen_anzahl = muehlen_anzahl
        self.maerkte_anzahl = maerkte_anzahl
        self.land_anzahl = land_anzahl
        self.korn_vorhanden = korn_vorhanden
        self.palast_elemente = palast_elemente


    def anzeige(self):
        print("------------------")
        print()
        print("Runde:", self.runde)
        print(titel_tupel[self.titel], self.vorname + " im Jahre", self.spieljahr)
        print()
        print("Bevölkerung:", int(self.bevoelkerung_gesamt), "Geld:", int(self.geld), "Landbesitz:", self.land_anzahl,
              "Kornmühlen:", self.muehlen_anzahl, "Märkte:", self.maerkte_anzahl, "Palastelemente:", self.palast_elemente)
        print()
        print("Vorhandenes Korn:", int(self.korn_vorhanden))
        print(" Benötigtes Korn")
        print("             Min:", int(self.bevoelkerung_gesamt * 0.5))
        print("    Durchschnitt:", int(self.bevoelkerung_gesamt * 0.8))
        print("             Max:", int(self.bevoelkerung_gesamt * 1.1))
        print()
        print("Kornpreise:       Landpreise:")
        print("   Einkauf:", kornpreis_kaufen, "      Einkauf:", landpreis_kaufen)
        print("   Verkauf:", kornpreis_verkaufen, "      Verkauf:", landpreis_verkaufen)
        print()


    def auswahl_kauf_verkauf(self):
        eingabe = input("Möchten sie Korn/Land kaufen (k) oder verkaufen (v) oder Nichts (jede andere Taste) tun?")
        if eingabe == "k":
            kaufwahl = input("Soll Korn (k) oder Land (l) gekauft werden?")
            while kaufwahl != "k" and kaufwahl != "l":
                kaufwahl = input("Bitte erneut eingeben, Korn (k) oder Land (l):")

            if kaufwahl == "k":
                menge_str = input("Wie viel Korn möchten sie kaufen?")
                print()
                menge = check_ob_digit(menge_str)       # hier wird neue funktion aufgerufen

                while self.geld <= menge * kornpreis_kaufen:
                    menge_str = input("Das können sie sich nicht leisten. Bitte eine niedrigere Anzahl eingeben: ")
                    menge = check_ob_digit(menge_str)

                else:
                    self.korn_vorhanden += menge
                    self.geld -= menge * kornpreis_kaufen

            else:
                menge_str = input("Wie viel Land möchten sie kaufen?")
                print()
                menge = check_ob_digit(menge_str)

                while self.geld <= menge * landpreis_kaufen:
                    menge_str = input("Das können sie sich nicht leisten. Bitte eine niedrigere Anzahl eingeben: ")
                    menge = check_ob_digit(menge_str)

                else:
                    self.land_anzahl += menge
                    self.geld -= menge * landpreis_kaufen

        elif eingabe == "v":
            verkaufwahl = input("Soll Korn (k) oder Land (l) verkauft werden?")
            while verkaufwahl != "k" and verkaufwahl != "l":
                verkaufwahl = input("Bitte erneut eingeben, Korn (k) oder Land (l):")

            if verkaufwahl == "k":
                menge_str = input("Wie viel Korn möchten sie verkaufen?")
                print()
                menge = check_ob_digit(menge_str)

                while self.korn_vorhanden < menge:
                    menge_str = input("Soviel besitzen sie leider nicht. Bitte eine niedrigere Anzahl eingeben: ")
                    menge = check_ob_digit(menge_str)

                else:
                    self.korn_vorhanden -= menge
                    self.geld += menge * kornpreis_verkaufen

            else:
                menge_str = input("Wie viel Land möchten sie verkaufen?")
                print()
                menge = check_ob_digit(menge_str)

                while self.land_anzahl < menge:
                    menge_str = input("Soviel besitzen sie leider nicht. Bitte eine niedrigere Anzahl eingeben: ")
                    menge = check_ob_digit(menge_str)

                else:
                    self.land_anzahl -= menge
                    self.geld += menge * landpreis_verkaufen

        else:
            print("Es wurde nicht gehandelt.")
            print()


    def auswahl_erweiterung(self):
        eingabe = input("Möchten sie Kornmühlen (k), Märkte (m) oder Palastelemente (p) errichten oder Nichts tun (jede andere Taste) ?")
        if eingabe == "k":
            if self.geld >= 1000:
                self.geld -= 1000
                self.muehlen_anzahl += 1
                print("Eine Mühle gekauft.")
                print()
            else:
                print("Leider nicht genügend Geld!")
                print()

        elif eingabe == "m":
            if self.geld >= 2000:
                self.geld -= 2000
                self.maerkte_anzahl += 1
                print("Einen Marktplatz gekauft.")
                print()
            else:
                print("Leider nicht genügend Geld!")
                print()

        elif eingabe == "p":
            if self.geld >= 9000:
                self.geld -= 9000
                self.palast_elemente += 1
                print("Ein Palastelement gekauft.")
                print()
            else:
                print("Leider nicht genügend Geld!")
                print()

        else:
            print("Kein Kauf getätigt.")
            print()


    def berechnungen(self):
        if korn_auswahl == "1":
            self.korn_vorhanden -= self.bevoelkerung_gesamt * 0.5
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * uniform(0.1, 0.2)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * uniform(0.02, 0.075)
        elif korn_auswahl == "3":
            self.korn_vorhanden -= self.bevoelkerung_gesamt * 0.8
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * uniform(0.075, 0.125)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * uniform(0.075, 0.125)
        else:
            self.korn_vorhanden -= self.bevoelkerung_gesamt * 1.1
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * uniform(0.02, 0.075)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * uniform(0.1, 0.2)

        self.bevoelkerung_gesamt = self.bevoelkerung_gesamt - bevoelkerung_gestorben + bevoelkerung_geboren
        self.geld += self.bevoelkerung_gesamt * self.muehlen_anzahl * 0.05 + self.bevoelkerung_gesamt * self.maerkte_anzahl * 0.1


    def erzeuge_korn(self):
        self.korn_vorhanden += self.muehlen_anzahl * 300 * choice([1.5, 1.2, 1, 0.8, 0.5])


    def counter(self):
        self.runde += 1
        self.spieljahr += 1


    def befoerderung(self):  # vorher if anstatt elif benutzt und jetzt wird immer nur auf die nächste stufe geprüft
        if self.titel == 0 and self.geld > 20000 and self.bevoelkerung_gesamt > 2000 and self.land_anzahl > 200 and self.maerkte_anzahl > 2 and self.muehlen_anzahl > 2:
            self.titel = 1
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 1 and self.geld > 30000 and self.bevoelkerung_gesamt > 3000 and self.land_anzahl > 300 and self.maerkte_anzahl > 3 and self.muehlen_anzahl > 3:
            self.titel = 2
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 2 and self.geld > 50000 and self.bevoelkerung_gesamt > 5000 and self.land_anzahl > 500 and self.maerkte_anzahl > 5 and self.muehlen_anzahl > 5:
            self.titel = 3
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 3 and self.geld > 60000 and self.bevoelkerung_gesamt > 6000 and self.land_anzahl > 600 and self.maerkte_anzahl > 6 and self.muehlen_anzahl > 6:
            self.titel = 4
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 4 and self.geld > 80000 and self.bevoelkerung_gesamt > 8000 and self.land_anzahl > 800 and self.maerkte_anzahl > 8 and self.muehlen_anzahl > 8 and self.palast_elemente > 3:
            self.titel = 5
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 5 and self.geld > 90000 and self.bevoelkerung_gesamt > 9000 and self.land_anzahl > 900 and self.maerkte_anzahl > 9 and self.muehlen_anzahl > 9 and self.palast_elemente > 6:
            self.titel = 6
            print("Herzlichen Glückwunsch. Sie wurden zum " + titel_tupel[self.titel] + " befördert! ")
            print()

        elif self.titel == 6 and self.geld > 120000 and self.bevoelkerung_gesamt > 12000 and self.land_anzahl > 1200 and self.maerkte_anzahl > 12 and self.muehlen_anzahl > 12 and self.palast_elemente > 10:
            self.titel = 7


    def spielende(self):
        if self.titel == 7:
            print("Herzlichen Glückwunsch. Du bist Kaiser! Du hast gewonnen!")
            print()
            game_continue = False
            return game_continue
        else:
            game_continue = True
            return game_continue


spieler_data = []
for spieler in spieler_liste:
    spieler = Game(spieler, 1, 1700, 0, 1000, 10000, 0, 0, 100, 10000, 0)
    spieler_data.append(spieler)


while game_continue is True:
    for i in range(anzahl_spieler):
        kornpreis_kaufen, kornpreis_verkaufen, landpreis_kaufen, landpreis_verkaufen = generiere_preise()
        spieler_data[i].anzeige()
        spieler_data[i].auswahl_kauf_verkauf()
        spieler_data[i].auswahl_erweiterung()
        korn_auswahl = auswahl_konsum()
        spieler_data[i].berechnungen()
        spieler_data[i].erzeuge_korn()
        spieler_data[i].counter()
        spieler_data[i].befoerderung()
        game_continue = spieler_data[i].spielende()

