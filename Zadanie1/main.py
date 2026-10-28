import csv
import math

with open("data1.csv", "r") as file:
    reader = csv.reader(file, delimiter=",", quotechar='"')
    data = [[float(x) for x in row] for row in reader]

dlugoscDzialkiKielicha = []
szerokoscDzialkiKielicha = []
dlugoscPlatka = []
szerokoscPlatka = []

Setosa = 0
Versicolor = 0
Virginica = 0

for row in data:
    dlugoscDzialkiKielicha.append(row[0])
    szerokoscDzialkiKielicha.append(row[1])
    dlugoscPlatka.append(row[2])
    szerokoscPlatka.append(row[3])
    if row[4] == 0.0:
        Setosa += 1
    elif row[4] == 1.0:
        Versicolor += 1
    elif row[4] == 2.0:
        Virginica += 1

maxDlugoscDzialkiKielicha = max(dlugoscDzialkiKielicha)
maxSzerokoscDzialkiKielicha = max(szerokoscDzialkiKielicha)
maxDlugoscPlatka = max(dlugoscPlatka)
maxSzerokoscPlatka = max(szerokoscPlatka)

minDlugoscDzialkiKielicha = min(dlugoscDzialkiKielicha)
minSzerokoscDzialkiKielicha = min(szerokoscDzialkiKielicha)
minDlugoscPlatka = min(dlugoscPlatka)
minSzerokoscPlatka = min(szerokoscPlatka)

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

def pearson(zbiora, zbiorb):
    sredniaZbiorA = sredniaArytmetyczna(zbiora)
    sredniaZbiorB = sredniaArytmetyczna(zbiorb)
    odchylenia = []

    for x, y in zip(zbiora, zbiorb):
        x -= sredniaZbiorA
        y -= sredniaZbiorB
        odchylenia.append(x * y)

    kowariancja = sum(odchylenia) / len(odchylenia)
    return kowariancja / (odchylenieStandardowe(zbiora) * odchylenieStandardowe(zbiorb))