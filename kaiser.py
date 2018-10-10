# Version mit Klasse

from random import uniform, randint, choice


timer = 1


class Game(object):
    def __init__(self, vorname, runde, spieljahr, titel, bevoelkerung_gesamt,
                 geld, muehlen_anzahl, maerkte_anzahl, land_anzahl, korn_vorhanden):
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


    def anzeige(self):
        global kornpreis_kaufen, kornpreis_verkaufen, landpreis_kaufen, landpreis_verkaufen
        kornpreis_kaufen = randint(30, 60)
        kornpreis_verkaufen = randint(20, 50)
        landpreis_kaufen = randint(70, 100)
        landpreis_verkaufen = randint(50, 80)
        print("------------------")
        print("Runde:", self.runde)
        print(self.titel, self.vorname + " im Jahre", self.spieljahr)
        print()
        print("Bevölkerung:", int(self.bevoelkerung_gesamt), "Geld:", int(self.geld), "Landbesitz:", self.land_anzahl,
              "Kornmühlen:",
              self.muehlen_anzahl, "Märkte:", self.maerkte_anzahl)
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
            if kaufwahl == "k":
                menge = int(input("Wie viel Korn möchten sie kaufen?"))
                if self.geld >= menge * kornpreis_kaufen:
                    self.korn_vorhanden += menge
                    self.geld -= menge * kornpreis_kaufen
                else:
                    print("Das können sie sich leider nicht leisten!")
            else:
                menge = int(input("Wie viel Land möchten sie kaufen?"))
                if self.geld >= menge * landpreis_kaufen:
                    self.land_anzahl += menge
                    self.geld -= menge * landpreis_kaufen
                else:
                    print("Das können sie sich leider nicht leisten!")

        elif eingabe == "v":
            verkaufwahl = input("Soll Korn (k) oder Land (l) vergekauft werden?")
            if verkaufwahl == "k":
                menge = int(input("Wie viel Korn möchten sie verkaufen?"))
                if self.korn_vorhanden >= menge:
                    self.korn_vorhanden -= menge
                    self.geld += menge * kornpreis_verkaufen
                else:
                    print("Soviel Korn besitzen sie leider nicht!")
            else:
                menge = int(input("Wie viel Land möchten sie verkaufen?"))
                if self.land_anzahl >= menge:
                    self.land_anzahl -= menge
                    self.geld += menge * landpreis_verkaufen
                else:
                        print("Soviel Land besitzen sie leider nicht!")

        else:
            print("Es wurde nicht gehandelt.")


    def auswahl_erweiterung(self):
        eingabe = input("Möchten sie Kornmühlen (k) oder Märkte (m) errichten oder Nichts (jede andere Taste) ?")
        if eingabe == "k":
            self.geld -= 1000
            self.muehlen_anzahl += 1
            print("Eine Mühle gekauft.")
            print()

        elif eingabe == "m":
            self.geld -= 2000
            self.maerkte_anzahl += 1
            print("Einen Marktplatz gekauft.")
            print()

        else:
            print("Kein Kauf getätigt.")
            print()


    def auswahl_konsum(self):
        print("Wie viel Korn dürfen die Bürger konsumieren?")
        korn_auswahl = input("Minimum = 1 / Durchschnitt = 3 / Maximum = 5  ")
        while korn_auswahl != "1" and korn_auswahl != "3" and korn_auswahl != "5":
            korn_auswahl = input("Bitte erneut eingeben: Minimum = 1 / Durchschnitt = 3 / Maximum = 5 ")

        return korn_auswahl


    def berechnungen(self, korn_auswahl):
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


player_1 = Game("Tobi", 1, 1700, "Baron", 1000, 20000, 2, 1, 100, 10000)

while timer <= 10:
    player_1.anzeige()
    player_1.auswahl_kauf_verkauf()
    player_1.auswahl_erweiterung()
    korn_auswahl = player_1.auswahl_konsum()
    player_1.berechnungen(korn_auswahl)
    player_1.erzeuge_korn()
    player_1.counter()
    timer += 1

