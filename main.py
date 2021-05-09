import math
def henger_felszín(r: float, m: float) -> float:
    felszín: float = 2 * math.pi * r * (r + m)
    return felszín


def henger_térfogat(r: float, m: float) -> float:
    térfogat: float = math.pi * m * r * r
    return térfogat


def main() -> None:
    print("Henger felszín, térfogat számítás")
    print("")
    print("Az adatokat cm-ben adja meg!")

    r = float(input("Adja meg a henger sugarát: "))
    m = float(input("Adja meg a henger magasságát: "))
    if r <= 0 or m <= 0:
        print("Egyik érték sem lehet negatív szám vagy nulla")
    else:
        felszín: float = round(henger_felszín(r, m), 2)
        térfogat: float = round(henger_térfogat(r, m), 2)
        print(f"A henger felszíne: {felszín} cm²")
        print(f"A henger térfogata: {térfogat} cm³")


if __name__ == '__main__':
    main()