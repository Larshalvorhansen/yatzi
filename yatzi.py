import math
import random

print("test")

players = []
dice = []

# Push test


def getOccurance(dice):
    occurance = [0, 0, 0, 0, 0, 0]
    for i in range(1, 6):
        for j in dice:
            print(f"j: {j}")
            if dice[j] == i:
                occurance[i - 1] += 1
    return occurance


def beregnPoeng(kategori, dice):
    sum = 0
    occurance = getOccurance(dice)
    dice.sort(reverse=True)
    match kategori:
        case "enere":
            for i in dice:
                if i == 1:
                    sum += 1
            return sum
        case "toere":
            for i in dice:
                if i == 2:
                    sum += 2
            return sum
        case "treere":
            for i in dice:
                if i == 3:
                    sum += 3
            return sum
        case "firere":
            for i in dice:
                if i == 4:
                    sum += 4
            return sum
        case "femmere":
            for i in dice:
                if i == 5:
                    sum += 5
            return sum
        case "seksere":
            for i in dice:
                if i == 6:
                    sum += 6
            return sum
        case "ett_par":
            print(occurance)
            for i in occurance:
                print(i)

                if i >= 2:
                    return (5 - i) * 2
            return 0
        case "to_par":
            return 0
        case "tre_like":
            return 0
        case "fire_like":
            return 0
        case "liten_straight":
            return 0
        case "stor_straight":
            return 0
        case "hus":
            return "hus"
        case "sjanse":
            return 0
        case "yatzy":
            if dice[1] == dice[2] == dice[3] == dice[4] == dice[5] == dice[0]:
                return 100
            return 0


print(beregnPoeng("ett_par", [3, 3, 4, 1, 5, 6]))


dice = [1, 2, 3, 2, 5, 6]
print(beregnPoeng(input(""), dice))


def lagTabell(n):
    kategorier = [
        "enere",
        "toere",
        "treere",
        "firere",
        "femmere",
        "seksere",
        "ett_par",
        "to_par",
        "tre_like",
        "fire_like",
        "liten_straight",
        "stor_straight",
        "hus",
        "sjanse",
        "yatzy",
    ]

    # hver kategori får en liste med n_spillere plasser
    tabell = {kategori: [None] * n for kategori in kategorier}
    return tabell


def printTabell(tabell, players):
    kategorier = list(tabell.keys())
    bredder = [max(len("Kategori"), max(len(k) for k in kategorier))]
    bredder += [max(len(p), 7) for p in players]

    def fmt(rad):
        if len(rad) < len(bredder):
            rad = rad + ["-"] * (len(bredder) - len(rad))
        return " | ".join(str(c).ljust(b) for c, b in zip(rad, bredder))

    header = ["Kategori"] + players
    print(fmt(header))
    print("-" * (sum(bredder) + 3 * (len(bredder) - 1)))

    for kategori in kategorier:
        rad = [kategori]
        for felt in tabell[kategori]:
            if isinstance(felt, list):
                rad.append(" ".join(map(str, felt)))
            elif felt is None:
                rad.append("-")
            else:
                rad.append(str(felt))
        print(fmt(rad))


def roll(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


# return kept dice and new dice
def rollRemaining(dice):
    newRoll = []
    nums = [int(ch) for ch in dice]
    for i in nums:
        newRoll.append(i)
    newRoll.append(roll(6 - len(nums)))
    flat = [n for sub in newRoll for n in (sub if isinstance(sub, list) else [sub])]
    print("")
    return flat


def main():
    players.append(input("Skriv spiller 1: "))
    players.append(input("Skriv spiller 2: "))

    while True:
        if (input("Flere? (Ja/Nei) ")) == "Ja":
            players.append(input("Skriv spillere"))
        else:
            break
    printTabell(lagTabell(3), players)

    input("Trykk enter for å trille!")
    print(roll(6))

    for i in range(1, 3):
        svar = input(
            f"Du har {3-i} kast igjen. Fortsette å trille?(Skriv hvilke terninger du vil beholde) eller ta {3-i} prikker(p)?"
        )
        if svar.isdigit():
            print(rollRemaining(svar))
        elif svar == "p":
            print(f"Du får {i} prikker")
            break
        else:
            print("Ugylig input prøv igjen.")
            i -= 1
    plassering = input("Hvor vil du plassere denne scoren?")


if __name__ == "__main__":
    main()
    print("done")
