import csv
import miaryStatystyczne
import pandas as pd

from Zadanie1 import miaryStatystyczne

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

print(f"Setosa: {Setosa}\n"
      f"Versicolor: {Versicolor}\n"
      f"Virginica: {Virginica}\n")


# Pomocnicze formatowanie (2 miejsca po przecinku i zamiana kropki na przecinek)
def fmt(val):
    return f"{val:.2f}".replace(".", ",")

cechy = [
    ("Długość działki kielicha (cm)", dlugoscDzialkiKielicha),
    ("Szerokość działki kielicha (cm)", szerokoscDzialkiKielicha),
    ("Długość płatka (cm)", dlugoscPlatka),
    ("Szerokość płatka (cm)", szerokoscPlatka)
]

wiersze_tabeli = []

for nazwa, zbior in cechy:
    minimum = min(zbior)
    maksimum = max(zbior)
    srednia = miaryStatystyczne.sredniaArytmetyczna(zbior)
    odchylenie = miaryStatystyczne.odchylenieStandardowe(zbior)
    med = miaryStatystyczne.mediana(zbior)
    q1, q3 = miaryStatystyczne.kwartyle(zbior)

    wiersze_tabeli.append({
        "Cecha": nazwa,
        "Minimum": fmt(minimum),
        "Śr. arytm. (± odch. stand.)": f"{fmt(srednia)} (±{fmt(odchylenie)})",
        "Mediana (Q1 - Q3)": f"{fmt(med)} ({fmt(q1)} - {fmt(q3)})",
        "Maksimum": fmt(maksimum)
    })

df = pd.DataFrame(wiersze_tabeli)
print(df.to_string(index=False))