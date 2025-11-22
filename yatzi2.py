import random as r

players = []


def trill(beholdte):
    terninger = list(beholdte)
    for _ in range(6 - len(beholdte)):  # Yatzy uses 5 dice
        terninger.append(r.randint(1, 6))
    return terninger


def beregn(terninger, kategori):
    poeng = 0
    n = 0
    match kategori:
        case "enere":
            n = 1
        case "toere":
            n = 2
        case "treere":
            n = 3
        case "firere":
            n = 4
        case "femmere":
            n = 5
        case "seksere":
            n = 6
        case _:
            pass
        case "hus":

    for i in terninger:
        if i == n:
            poeng += n
    return poeng


class Scorecard:
    def __init__(self, name):
        self.name = name
        self.scores = {
            "enere": None,
            "toere": None,
            "treere": None,
            "firere": None,
            "femmere": None,
            "seksere": None,
            "ettPar": None,
            "toPar": None,
            "yatzi": None,
        }
        self.prikker = 0

    def set_score(self, category, score):
        if category in self.scores:
            self.scores[category] = score
        else:
            print("Error in setting score")

    def print_score(self):
        print(f"\nPoengoversikt for {self.name}:")
        total = 0
        for category, score in self.scores.items():
            if score is None:
                print(f"{category}: -")
            else:
                print(f"{category}: {score}")
                total += score
        print(f"Totalt: {total}")
        print(f"Prikker: {self.prikker}\n")


def generatePlayers():
    numberOfPlayers = int(input("Hvor mange spiller? "))
    for i in range(numberOfPlayers):
        navn = input(f"Skriv spiller nr.{i+1}: ")
        players.append(Scorecard(navn))

    while True:
        if input("Flere? (Ja/Nei) ").strip().lower() == "ja":
            navn = input("Skriv spiller ")
            players.append(Scorecard(navn))
        else:
            break


def printScores():
    for p in players:
        p.print_score()


def tur(player: Scorecard):
    beholde = []
    terninger = []
    for kast in range(1, 4):
        terninger = trill(beholde)
        print("Trill:", terninger)
        if kast < 3:
            valg = input(f"Vil du avslutte nå og få {3-kast} prikker? ('ja'/'nei') ")
        else:
            valg = "ja"
        if valg.strip().lower() == "ja":
            kategori = input("Hva vil du sette terningene dine på? ")
            player.set_score(kategori, beregn(terninger, kategori))
            return kast
        sbeholde = input("Hvilke terninger vil du beholde? feks('5,5,6') ")
        beholde = [int(x.strip()) for x in sbeholde.split(",") if x.strip()]
    kategori = input("Hva vil du sette terningene dine på? ")
    player.set_score(kategori, beregn(terninger, kategori))
    return kategori


def main():
    generatePlayers()
    printScores()
    for j in range(1, 3):
        print(f"Runde {j}!")
        for p in players:
            print(f"{p.name} sin tur")  # use .name
            tur(p)
            printScores()


if __name__ == "__main__":
    main()
