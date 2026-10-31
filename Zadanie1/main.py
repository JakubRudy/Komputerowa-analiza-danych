import csv
import matplotlib.pyplot as plt
import pandas as pd

import miary_statystyczne


def fmt(val):
    return f"{val:.2f}".replace(".", ",")


def rysowanie_histogramu(ax, dane, k, xPodpis, yPodpis, tytul, zakres=None):
    if zakres is not None:
        minimum, maksimum = zakres
    else:
        minimum = min(dane)
        maksimum = max(dane)

    szerokosc = (maksimum - minimum) / k
    podzialka = [minimum + i * szerokosc for i in range(k + 1)]

    licznosci = [0] * k
    for x in dane:
        indeks = int((x - minimum) / szerokosc)
        if indeks >= k:
            indeks = k - 1
        elif indeks < 0:
            indeks = 0
        licznosci[indeks] += 1

    granice = [minimum + i * szerokosc for i in range(k)]

    ax.bar(granice, licznosci, width=szerokosc, align="edge", edgecolor="black")

    # Formatowanie podziałki, żeby uniknąć długich ułamków typu 0.3125
    ax.set_xticks(podzialka)
    ax.set_xticklabels([f"{val:.2f}".rstrip('0').rstrip('.') if val % 0.5 != 0 else f"{val:.1f}" for val in podzialka])

    ax.set_xlabel(xPodpis)
    ax.set_ylabel(yPodpis)
    ax.set_title(tytul)

    # Automatyczne dopasowanie wysokości osi Y z lekkim zapasem nad najwyższym słupkiem
    ax.set_ylim(0, max(licznosci) + 4)

def rysowanie_pudelkowego(ax, x, y, z, yPodpis):
    ax.boxplot([x, y, z], tick_labels=["setosa", "versicolor", "virginica"])  #[cite: 1]
    ax.set_ylabel(yPodpis)  #[cite: 1]
    ax.set_xlabel("Gatunek")  #[cite: 1]


def main():
    df = pd.read_csv(
        "data1.csv",
        header=None,
        names=[
            "Długość działki kielicha",
            "Szerokość działki kielicha",
            "Długość płatka",
            "Szerokość płatka",
            "Gatunek",
        ],
    )

    print(
        f"Setosa: {(df['Gatunek'] == 0).sum()}\n"
        f"Versicolor: {(df['Gatunek'] == 1).sum()}\n"
        f"Virginica: {(df['Gatunek'] == 2).sum()}\n"
    )

    # Konfiguracja podpisów osi i zakresów dla poszczególnych cech
    konfiguracja = [
        ("Długość działki kielicha", "Długość (cm)", (4.0, 8.0)),
        ("Szerokość działki kielicha", "Szerokość (cm)", (2.0, 4.4)),
        ("Długość płatka", "Długość (cm)", (1.0, 7.0)),
        ("Szerokość płatka", "Szerokość (cm)", (0.0, 2.5)),
    ]

    # Tworzenie siatki 4 wiersze x 2 kolumny
    fig, axes = plt.subplots(4, 2, figsize=(8, 10))

    for i, (kolumna, podpis_osi, zakres) in enumerate(konfiguracja):
        dane = df[kolumna]

        print(
            f"{kolumna}:\t\t"
            f"{min(dane):.2f}\t"
            f"{miary_statystyczne.srednia_arytmetyczna(dane):.2f} ± ({miary_statystyczne.odchylenie_standardowe(dane):.2f})\t"
            f"{miary_statystyczne.mediana(dane):.2f} {miary_statystyczne.kwartyle(dane)}\t"
            f"{max(dane):.2f}"
        )

        # Podział danych na 3 gatunki do wykresu pudełkowego
        setosa = df[df["Gatunek"] == 0][kolumna]
        versicolor = df[df["Gatunek"] == 1][kolumna]
        virginica = df[df["Gatunek"] == 2][kolumna]

        # Lewa kolumna (indeks 0): Histogram
        rysowanie_histogramu(
            axes[i, 0], dane, 8, podpis_osi, "Liczebność", kolumna, zakres=zakres
        )

        # Prawa kolumna (indeks 1): Wykres pudełkowy
        rysowanie_pudelkowego(
            axes[i, 1], setosa, versicolor, virginica, podpis_osi
        )

    # Automatyczne dopasowanie odstępów między wykresami, aby napisy na siebie nie nachodziły
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()