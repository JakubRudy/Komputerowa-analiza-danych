import csv

import pandas as pd
import matplotlib.pyplot as plt

import miaryStatystyczne

def fmt(val):
    return f"{val:.2f}".replace(".", ",")

def rysowanie_histogramu(dane, k, xPodpis, yPodpis, tytul):
    minimum = min(dane)
    maksimum = max(dane)

    szerokosc = (maksimum - minimum) / k

    podzialka = [
        minimum + i * szerokosc
        for i in range(k + 1)
    ]

    plt.xticks(podzialka)

    licznosci = [0] * k

    for x in dane:
        indeks = int((x - minimum) / szerokosc)

        if indeks == k:
            indeks = k - 1

        licznosci[indeks] += 1

    granice = [
        minimum + i * szerokosc
        for i in range(k)
    ]
    plt.bar(
        granice,
        licznosci,
        width=szerokosc,
        align="edge",
        edgecolor="black"
    )

    plt.xlabel(xPodpis)
    plt.ylabel(yPodpis)
    plt.title(tytul)

    plt.show()
    return 0

def rysowanie_wykresu(x, y, xPodpis, yPodpis):
    plt.scatter(x, y)
    r = miaryStatystyczne.pearson(x, y)
    a, b = miaryStatystyczne.regresjaLiniowa(x, y)

    noweY = [
        a * x[i] + b
        for i in range(len(x))
    ]

    plt.plot(x, noweY, "r-")
    plt.xlabel(xPodpis)
    plt.ylabel(yPodpis)
    plt.title(f"r = {r:.2f}; y = {a:.2f}x {b:+.2f}")
    plt.show()
    return 0

def main():
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['legend.fontsize'] = 12

    with open("data1.csv", "r") as file:
        reader = csv.reader(file, delimiter=",", quotechar='"')
        data = [[float(x) for x in row] for row in reader]

    dlugosc_dzialki = []
    szerokosc_dzialki = []
    dlugosc_platka = []
    szerokosc_platka = []
    setosa = 0
    versicolor = 0
    virginica = 0

    for row in data:
        dlugosc_dzialki.append(row[0])
        szerokosc_dzialki.append(row[1])
        dlugosc_platka.append(row[2])
        szerokosc_platka.append(row[3])
        if row[4] == 0.0:
            setosa += 1
        elif row[4] == 1.0:
            versicolor += 1
        elif row[4] == 2.0:
            virginica += 1

    print(f"Setosa: {setosa}\n"
          f"Versicolor: {versicolor}\n"
          f"Virginica: {virginica}\n")

    cechy = [
        ("Długość działki kielicha (cm)", dlugosc_dzialki),
        ("Szerokość działki kielicha (cm)", szerokosc_dzialki),
        ("Długość płatka (cm)", dlugosc_platka),
        ("Szerokość płatka (cm)", szerokosc_platka)
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

    rysowanie_histogramu(dlugosc_dzialki, 8, "Długość (cm)", "Liczebność", "Długość działki kielicha")
    rysowanie_wykresu(dlugosc_dzialki, szerokosc_dzialki, "Długość działki kielicha", "Szerokość działki kielicha")

    rysowanie_histogramu(szerokosc_dzialki, 8, "Długość (cm)", "Liczebność", "Szerokość działki kielicha")
    rysowanie_histogramu(dlugosc_platka, 8, "Długość (cm)", "Liczebność", "Długość płatka kielicha")
    rysowanie_histogramu(szerokosc_platka, 8, "Długość (cm)", "Liczebność", "Szerokość płatka kielicha")


if __name__ == "__main__":
    main()