import math

def srednia_arytmetyczna(zbior):
    return sum(zbior) / len(zbior)

def odchylenie_standardowe(zbior):
    srednia = srednia_arytmetyczna(zbior)
    wariancja = 0
    for x in zbior:
        wariancja += (x - srednia) ** 2
    wariancja /= len(zbior) - 1
    return math.sqrt(wariancja)

def mediana(zbior):
    zbior = sorted(zbior)
    polowa = len(zbior) // 2

    if len(zbior) % 2 == 0:
        return (zbior[polowa] + zbior[polowa - 1]) / 2
    else:
        return zbior[polowa]

def kwartyle(zbior):
    zbior = sorted(zbior)
    polowa = len(zbior) // 2

    q1 = mediana(zbior[:polowa])

    if len(zbior) % 2 == 0:
        q3 = mediana(zbior[polowa:])
    else:
        q3 = mediana(zbior[polowa + 1:])
    return q1, q3

def normalizacja(zbior):
    wynik = []
    maksimum = max(zbior)
    minimum = min(zbior)
    mianownik = maksimum - minimum
    for x in zbior:
        wynik.append((2 * ((x - minimum) / mianownik)) - 1)
    return wynik

def kowariancja(zbiora, zbiorb):
    sredniaZbiorA = srednia_arytmetyczna(zbiora)
    sredniaZbiorB = srednia_arytmetyczna(zbiorb)
    odchylenia = []

    for x, y in zip(zbiora, zbiorb):
        x -= sredniaZbiorA
        y -= sredniaZbiorB
        odchylenia.append(x * y)

    return sum(odchylenia) / (len(odchylenia) -1)

def pearson(zbiora, zbiorb):
    kowariancjaWynik = kowariancja(zbiora, zbiorb)
    return kowariancjaWynik / (odchylenie_standardowe(zbiora) * odchylenie_standardowe(zbiorb))

def regresjaLiniowa(zbiora, zbiorb):
    aLicznik = kowariancja(zbiora, zbiorb)
    aMianownik = 0
    xSrednia = srednia_arytmetyczna(zbiora)
    for x in zbiora:
        aMianownik += (x - xSrednia) ** 2

    aMianownik /= len(zbiora)
    a = aLicznik / aMianownik
    ySrednia = srednia_arytmetyczna(zbiorb)
    b = ySrednia - a * xSrednia
    return a, b