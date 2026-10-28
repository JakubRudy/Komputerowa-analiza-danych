import csv
import miaryStatystyczne

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