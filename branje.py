from asyncore import read
import csv
from sqlite3 import Row
import numpy as np
import pandas as pd


def readYear(yearDir):
    # print(yearDir)

    data = pd.read_csv("data/"+str(yearDir)+"/uspesnost.csv", delimiter=";")
    print(data)
    # with open('data/'+str(yearDir)+'/napake.csv') as csvfile:
    #    reader = csv.reader(csvfile, delimiter=";")
    #    napake = np.array(
    #        [(row["OZNAKA_KATEGORIJE"], row["OPIS_KATEGORIJE"], row["NADGRADNJA_SIFRA"], row["NADGRADNJA_OPIS"], row["DODATNA_NADGRADNJA"], row["VRSTA_GORIVA_OZNAKA"], row["VRSTA_GORIVA_OPIS"], row["OZNAKA_POSTAVKE"], row["PODROBNI_OPIS_POSTAVKE"], row["OPIS_POSTAVKE_1"], row["OPIS_POSTAVKE_2"], row["OPIS_POSTAVKE_3"], row["OPIS_POSTAVKE_4"], row["OCENA"]) for row in reader])
    #    print(napake)
    # reader = DictReader(
    #    open(, 'rt', encoding='utf-8') delimiter=)
    # print([x for x in reader][0])
    # napake = np.array(
    #    [(row["OZNAKA_KATEGORIJE"], row["OPIS_KATEGORIJE"], row["NADGRADNJA_SIFRA"], row["NADGRADNJA_OPIS"], row["DODATNA_NADGRADNJA"], row["VRSTA_GORIVA_OZNAKA"], row["VRSTA_GORIVA_OPIS"], row["OZNAKA_POSTAVKE"], row["PODROBNI_OPIS_POSTAVKE"], row["OPIS_POSTAVKE_1"], row["OPIS_POSTAVKE_2"], row["OPIS_POSTAVKE_3"], row["OPIS_POSTAVKE_4"], row["OCENA"]) for row in reader])

    # reader = DictReader(
    #    open('data/'+str(yearDir)+'/uspesnost.csv', 'rt', encoding='utf-8'))
    # uspesnost = np.array(
    #    [(row["ZNAMKA"], row["TOVARNISKA_OZNAKA"], row["KOMERCIALNA_OZNAKA"], row["KOMERCIALNI_TIP"], row["VIN"], row["VIN_TRAKTORJA"], row["KATEGORIJA_OZNAKA"], row["KATEGORIJA_OPIS"], row["NADGRADNJA_OZNAKA"], row["NADGRADNJA_OPIS"], row["DODATNA_NADGRADNJA_OPIS"], row["VRSTA_GORIVA_OZNAKA"], row["VRSTA_GORIVA_OPIS"], row["NAMEN_VOZILA"], row["DATUM_PRVE_REGISTRACIJE"], row["DATUM_PRVE_REGISTRACIJE_SLO"], row["PREVOZENI_KILOMETRI"], row["LASTNIK_VOZILA"], row["UPORABNIK_VOZILA"], row["DATUM_PREGLEDA"], row["TEHNICNI_ZAPISNIK_RAZLOG"], row["TEHNICNI_PREGLED_STATUS"], row["VELJA_OD"], row["VELJA_DO"], row["IZVAJALNA_ENOTA_OPIS"]) for row in reader])
    # filmRatings = np.array([[float(row[\"userId\"]),float(row[\"movieId\"]),float(row[\"rating\"]),float(row[\"timestamp\"])] for row in reader])\n


readYear(2017)
