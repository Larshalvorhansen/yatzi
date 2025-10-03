import random as r


def trill(beholdte):
    terninger = [] + beholdte
    for i in range(6 - len(beholdte)):
        terninger.append(r.randint(1, 6))
    return terninger


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

    def set_score(self, category, score):
        if category in self.scores:
            self.scores[category] = score
        else:
            print("Error in setting score")


def main():
    print("Running")
    Lars = Scorecard("Lars")
    print(Lars.scores)
    Lars.set_score("enere", 3)
    print(Lars.scores)


if __name__ == "__main__":
    main()
