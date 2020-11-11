# Konstanten in GROSSBUCHSTABEN rename titel_tupel in TITEL_BEZEICHNUNG
# game_continue erst dann definieren wenn es gebraucht wird
# while game_continue: ist das gleiche wie while game_continue is TRUE:
# Init-Werte wurden als Default gesetzt da sie für alle gleich sind anstatt bei
# der Initialisierung der einzelnen Spieler
# changed auswahl_konsum() :
# while korn_auswahl != "1" and korn_auswahl != "3" .. --->
# while korn_auswahl not in ("1", "3", "5"):
# spieljahr läßt sich aus 1699 + Anzahl der Runden herleiten
# fixed: Spieler Counter zeigte immer einen zu wenig an
# def erzeuge_korn() wurde in def berechnungen() integriert
# befoerderungsmethode verbessert
# check_ob_digit ersetzt durch check ob decimal
# spielererschaffung umgeschrieben
# def befördert wurde mit auf multiline umgeschrieben
# docstrings eingefügt
# schleife umgeschrieben bei der abfrage ob korn/land ge-verkauft werden soll
# korn kann nicht länger negativ werden
# falls kein korn vorhanden ist, wird die verbrauchsauswahl nicht berücksichtigt

from random import uniform, randint, choice

# standard-input ist für nur für AREPL
# standard_input = ["Tobi", "j", "", "", "", "3"]

TITEL_BEZEICHNUNG = ("Baron", "Graf", "Fürst", "Herzog",
                     "Kurfürst", "Großherzog", "König", "Kaiser")
KORN_MULTIPLIKATOR_MIN = 0.5
KORN_MULTIPLIKATOR_AVG = 0.8
KORN_MULTIPLIKATOR_MAX = 1.1

# // TODO: Spielererschaffung sollte eine eigene Funktion sein.
spieler_liste = []
add_new_player = True
while add_new_player is True:
    count = len(spieler_liste) + 1
    prompt = "Ja (j) / Nein (n) "
    print("Bitte Spielername eingeben. Leere Eingabe um fortzufahren.")
    print()
    print("Spieler ", count)
    spieler_name = input("Name: ").strip()
    print()
    if not spieler_name:
        break
    print("Ist dieser Name korrekt?", spieler_name)
    print()
    eingabe = input(prompt)
    print()

    while eingabe != "j":
        print()
        spieler_name = input("Bitte Name erneut eingeben: ")
        print()
        print("Ist dieser Name korrekt?", spieler_name)
        print()
        eingabe = input(prompt)
        print()

    spieler_liste.append(spieler_name)

ANZAHL_SPIELER = len(spieler_liste)


def generiere_preise():
    """Erzeugt Preise für Korn und Land

    Returns:
        int: zufällig erzeugte Preise innerhalb einer definierten Range
    """
    kornpreis_kaufen = randint(3, 6)
    kornpreis_verkaufen = randint(2, 5)
    landpreis_kaufen = randint(70, 100)
    landpreis_verkaufen = randint(50, 80)
    return kornpreis_kaufen, kornpreis_verkaufen, landpreis_kaufen, landpreis_verkaufen


# // TODO: Wenn ich kein Korn habe, ist eine Abfrage unnötig
def auswahl_konsum():
    """Nimmt eine Eingabe entgegen wie viel Korn die Bürger konsumieren dürfen

    Returns:
        str: korn_auswahl Input darf nur 1, 3, 5 sein ansonsten erneute Abfrage
    """
    print("Wie viel Korn dürfen die Bürger konsumieren?")
    prompt = """Minimum = 1 / Durchschnitt = 3 / Maximum = 5
    Ihre Auswahl: """
    korn_auswahl = input(prompt)
    while korn_auswahl not in ("1", "3", "5"):
        korn_auswahl = input(
            "Bitte erneut eingeben: " + prompt)
    return korn_auswahl


def check_ob_decimal(menge_str):
    """Prüft ob die Eingabe einfach numerisch ist

    Args:
        menge_str (str): Eingabe wie viel man handeln möchte

    Returns:
        int: menge_str : Ausgabe des gewählten Wertes als int und geprüft
    """
    while menge_str.isdecimal() is False:
        menge_str = input(
            "Bitte erneut eingeben: Wie viel möchten sie handeln?")
        print()
    return int(menge_str)


class Game(object):
    """Erzeugt die Spielklasse

    Args:
        object ([type]): [description]
    """
    def __init__(self, vorname, runde=1, titel=0, bevoelkerung_gesamt=1000,
                 geld=10000, muehlen_anzahl=0, maerkte_anzahl=0, land_anzahl=100,
                 korn_vorhanden=0, palast_elemente=0):
        self.vorname = vorname
        self.runde = runde
        self.titel = titel
        self.bevoelkerung_gesamt = bevoelkerung_gesamt
        self.geld = geld
        self.muehlen_anzahl = muehlen_anzahl
        self.maerkte_anzahl = maerkte_anzahl
        self.land_anzahl = land_anzahl
        self.korn_vorhanden = korn_vorhanden
        self.palast_elemente = palast_elemente

    def anzeige(self):
        """Stell bei Rundenstart die nötigen Statusinfos bereit
        """
        # // TODO Mit Formatierung arbeiten anstatt Leerzeichen um es auszurichten
        print("------------------")
        print()
        print("Runde:", self.runde)
        print(TITEL_BEZEICHNUNG[self.titel],
              self.vorname + " im Jahre", 1699 + self.runde)
        print()
        print("Bevölkerung:", int(self.bevoelkerung_gesamt), "Geld:", int(self.geld), "Landbesitz:",
              self.land_anzahl, "Kornmühlen:", self.muehlen_anzahl, "Märkte:",
              self.maerkte_anzahl, "Palastelemente:", self.palast_elemente)
        print()
        print("Vorhandenes Korn:", int(self.korn_vorhanden))
        print(" Benötigtes Korn")
        # // TODO: Sind die Berechnungen doppelt aufgeführt? Wie kann ich die Werte direkt aus der
        # berechnungsfunktion von unten nehmen ohne die 0,5 0,8 1,1 neu auszuschreiben? Konstanten?
        print("             Min:", int(self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_MIN))
        print("    Durchschnitt:", int(self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_AVG))
        print("             Max:", int(self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_MAX))
        print()
        print("Kornpreise:       Landpreise:")
        print("   Einkauf:", kornpreis_kaufen,
              "      Einkauf:", landpreis_kaufen)
        print("   Verkauf:", kornpreis_verkaufen,
              "      Verkauf:", landpreis_verkaufen)
        print()

# // TODO: Zu viel ähnlichen Code?
    def auswahl_kauf_verkauf(self):
        """Fragt ob Korn oder Land ge- oder verkauft werden soll. Fügt hinzu bzw zieht ab und prüft
        ob die nötigen Bedingungen erfüllt werden.
        """
        eingabe = input(
            "Möchten sie Korn/Land kaufen (k) oder verkaufen (v) oder Nichts"
            " (jede andere Taste) tun?")
        if eingabe == "k":
            kaufwahl = input("Soll Korn (k) oder Land (l) gekauft werden?")
            while kaufwahl not in ("k", "l"):
                kaufwahl = input(
                    "Bitte erneut eingeben, Korn (k) oder Land (l):")

            if kaufwahl == "k":
                menge_str = input("Wie viel Korn möchten sie kaufen?")
                print()
                menge = check_ob_decimal(menge_str)

                while True:
                    if self.geld <= menge * kornpreis_kaufen:
                        menge_str = input("Das können sie sich nicht leisten. Bitte eine"
                                          " niedrigere Anzahl eingeben: ")
                        menge = check_ob_decimal(menge_str)

                    else:
                        self.korn_vorhanden += menge
                        self.geld -= menge * kornpreis_kaufen
                        break

            else:
                menge_str = input("Wie viel Land möchten sie kaufen?")
                print()
                menge = check_ob_decimal(menge_str)

                while True:
                    if self.geld <= menge * landpreis_kaufen:
                        menge_str = input("Das können sie sich nicht leisten. Bitte eine"
                                          " niedrigere Anzahl eingeben: ")
                        menge = check_ob_decimal(menge_str)

                    else:
                        self.land_anzahl += menge
                        self.geld -= menge * landpreis_kaufen
                        break

        elif eingabe == "v":
            verkaufwahl = input("Soll Korn (k) oder Land (l) verkauft werden?")
            while verkaufwahl not in ("k", "l"):
                verkaufwahl = input(
                    "Bitte erneut eingeben, Korn (k) oder Land (l):")

            if verkaufwahl == "k":
                menge_str = input("Wie viel Korn möchten sie verkaufen?")
                print()
                menge = check_ob_decimal(menge_str)

                while True:
                    if self.korn_vorhanden < menge:
                        menge_str = input("Soviel besitzen sie leider nicht. Bitte eine niedrigere"
                                          " Anzahl eingeben: ")
                        menge = check_ob_decimal(menge_str)

                    else:
                        self.korn_vorhanden -= menge
                        self.geld += menge * kornpreis_verkaufen
                        break

            else:
                menge_str = input("Wie viel Land möchten sie verkaufen?")
                print()
                menge = check_ob_decimal(menge_str)

                while True:
                    if self.land_anzahl < menge:
                        menge_str = input("Soviel besitzen sie leider nicht. Bitte eine niedrigere"
                                          " Anzahl eingeben: ")
                        menge = check_ob_decimal(menge_str)

                    else:
                        self.land_anzahl -= menge
                        self.geld += menge * landpreis_verkaufen
                        break

        else:
            print("Es wurde nicht gehandelt.")
            print()

# // TODO: Zu viel ähnlichen Code?
    def auswahl_erweiterung(self):
        """Fragt ob eine Erweiterung gekauft werden soll und falls ja, prüft ob das Geld
        ausreicht. Bei falschen Eingaben, wird wiederholt
        """
        eingabe = input(
            "Möchten sie Kornmühlen (k), Märkte (m) oder Palastelemente (p) errichten oder Nichts"
            " tun (jede andere Taste) ?")
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
        """Berechnet wie viel Korn noch vorhanden ist, wie viel Bevölkerung
        starb und neu geboren wurde
        """
        if self.korn_vorhanden <= 0:
            self.korn_vorhanden = 0
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * uniform(0.2, 0.3)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * uniform(0.01, 0.02)

        elif korn_auswahl == "1":
            self.korn_vorhanden -= self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_MIN
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * \
                uniform(0.1, 0.2)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * \
                uniform(0.02, 0.075)
        elif korn_auswahl == "3":
            self.korn_vorhanden -= self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_AVG
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * \
                uniform(0.075, 0.125)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * \
                uniform(0.075, 0.125)
        else:
            self.korn_vorhanden -= self.bevoelkerung_gesamt * KORN_MULTIPLIKATOR_MAX
            bevoelkerung_gestorben = self.bevoelkerung_gesamt * \
                uniform(0.02, 0.075)
            bevoelkerung_geboren = self.bevoelkerung_gesamt * uniform(0.1, 0.2)

        self.bevoelkerung_gesamt = self.bevoelkerung_gesamt - \
            bevoelkerung_gestorben + bevoelkerung_geboren
        self.geld += self.bevoelkerung_gesamt * self.muehlen_anzahl * \
            0.05 + self.bevoelkerung_gesamt * self.maerkte_anzahl * 0.1
        self.korn_vorhanden += self.muehlen_anzahl * \
            300 * choice([1.5, 1.2, 1, 0.8, 0.5])

# // TODO: Funktion nur für den Counter?
    def counter(self):
        """Zählt die Runde höher
        """
        self.runde += 1

# // TODO: Hier lassen sich wohl mit "ENUM" Objekten  Grenzwerte herausziehen und  viel Code sparen
    def befoerderung(self):
        """Prüft ob diese Runde befördert wurde. falls nicht prüft ob Bedingungen erfüllt werden
        und befördert
        """
        befoerdert_diese_runde = False
        if (
            self.titel == 0
            and self.geld > 10000
            and self.bevoelkerung_gesamt > 1200
            and self.land_anzahl > 130
            and self.maerkte_anzahl > 2
            and self.muehlen_anzahl > 2
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 1
            and self.geld > 30000
            and self.bevoelkerung_gesamt > 1800
            and self.land_anzahl > 180
            and self.maerkte_anzahl > 3
            and self.muehlen_anzahl > 3
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 2
            and self.geld > 50000
            and self.bevoelkerung_gesamt > 2800
            and self.land_anzahl > 250
            and self.maerkte_anzahl > 5
            and self.muehlen_anzahl > 5
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 3
            and self.geld > 60000
            and self.bevoelkerung_gesamt > 4000
            and self.land_anzahl > 350
            and self.maerkte_anzahl > 6
            and self.muehlen_anzahl > 6
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 4
            and self.geld > 80000
            and self.bevoelkerung_gesamt > 6000
            and self.land_anzahl > 500
            and self.maerkte_anzahl > 8
            and self.muehlen_anzahl > 8
            and self.palast_elemente > 3
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 5
            and self.geld > 90000
            and self.bevoelkerung_gesamt > 9000
            and self.land_anzahl > 800
            and self.maerkte_anzahl > 9
            and self.muehlen_anzahl > 9
            and self.palast_elemente > 6
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        elif (
            self.titel == 6
            and self.geld > 120000
            and self.bevoelkerung_gesamt > 12000
            and self.land_anzahl > 1200
            and self.maerkte_anzahl > 12
            and self.muehlen_anzahl > 12
            and self.palast_elemente > 10
        ):
            self.titel += 1
            befoerdert_diese_runde = True

        if befoerdert_diese_runde is True:
            print()
            print("Herzlichen Glückwunsch. Sie wurden zum",
                  TITEL_BEZEICHNUNG[self.titel], "befördert! ")
            print()

    def spielende(self):
        """Prüft ob die Siegbedingung erfüllt wurde. Falls ja, beendet das Spiel

        Returns:
            bool: game_continue : Wird auf False gesetzt, wenn das Spiel beendet wurde
        """
        if self.titel == 7:
            print()
            print("Sie haben gewonnen!")
            print()
            game_continue = False

        else:
            game_continue = True

        return game_continue


spieler_data = []
for spieler in spieler_liste:
    spieler = Game(spieler)
    spieler_data.append(spieler)
    # spieler_data.append(Game(spieler)) --> ist das gleiche wie die 2 Zeilen darüber

game_continue = True

while game_continue:
    for i in range(ANZAHL_SPIELER):
        (kornpreis_kaufen, kornpreis_verkaufen,
         landpreis_kaufen, landpreis_verkaufen) = generiere_preise()
        spieler_data[i].anzeige()
        spieler_data[i].auswahl_kauf_verkauf()
        spieler_data[i].auswahl_erweiterung()
        korn_auswahl = auswahl_konsum()
        spieler_data[i].berechnungen()
        spieler_data[i].counter()
        spieler_data[i].befoerderung()
        game_continue = spieler_data[i].spielende()
