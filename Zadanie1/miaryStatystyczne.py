import math

def sredniaArytmetyczna(zbior):
    return sum(zbior) / len(zbior)

def odchylenieStandardowe(zbior):
    srednia = sredniaArytmetyczna(zbior)
    wariancja = 0
    for x in zbior:
        wariancja += (x - srednia) ** 2
    wariancja /= len(zbior)
    return math.sqrt(wariancja)

def mediana(zbior):
    zbior = sorted(zbior)
    polowa = len(zbior) // 2
    if len(zbior) % 2 == 0:
        return (zbior[polowa] + zbior[polowa - 1]) / 2
    else:
        return zbior[polowa]

def normalizacja(zbior):
    wynik = []
    maksimum = max(zbior)
    minimum = min(zbior)
    mianownik = maksimum - minimum
    for x in zbior:
        # Normalizacja do przedziału [-1, 1]
        wynik.append((2 * ((x - minimum) / mianownik)) - 1)
    return wynik

def kowariancja(zbiora, zbiorb):
    sredniaZbiorA = sredniaArytmetyczna(zbiora)
    sredniaZbiorB = sredniaArytmetyczna(zbiorb)
    odchylenia = []

    for x, y in zip(zbiora, zbiorb):
        x -= sredniaZbiorA
        y -= sredniaZbiorB
        odchylenia.append(x * y)

    return sum(odchylenia) / len(odchylenia)

def pearson(zbiora, zbiorb):

    kowariancjaWynik = kowariancja(zbiora, zbiorb)
    return kowariancjaWynik / (odchylenieStandardowe(zbiora) * odchylenieStandardowe(zbiorb))

def regresjaLiniowa(zbiora, zbiorb):
    aLicznik = kowariancja(zbiora, zbiorb)

    aMianownik = 0
    xSrednia = sredniaArytmetyczna(zbiora)
    for x in zbiora:
        aMianownik += (x - xSrednia) ** 2

    aMianownik /= len(zbiora)

    a = aLicznik / aMianownik

    ySrednia = sredniaArytmetyczna(zbiorb)

    b = ySrednia - a * xSrednia

    return a, b