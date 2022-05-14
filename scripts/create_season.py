import random
from datetime import date

def main():

    firstYear = 2019
    lastYear = 2022

    f = open("seasonsData.txt", "a")

    f.write("INSERT INTO temporada VALUES\n")
    for i in range(firstYear, lastYear+1):

        rTemporadaBaja = random.randint(1,31)
        rTemporadaAlta = random.randint(1, 30)

        iniTempBaja = getDate(i, 1, 1)
        finTempBaja = getDate(i, 5, rTemporadaBaja)

        f.write(values_to_string(['baja', iniTempBaja, finTempBaja]))
        f.write(",\n")

        iniTempAlta = ""

        if rTemporadaBaja == 31:
            iniTempAlta = getDate(i, 6, 1)
        else:
            iniTempAlta = getDate(i, 5, rTemporadaBaja+1)

        finTempAlta = getDate(i, 9, rTemporadaAlta)

        f.write(values_to_string(['alta', iniTempAlta, finTempAlta]))
        f.write(",\n")

        iniTempMedia = ""

        if rTemporadaAlta == 30:
            iniTempMedia = getDate(i, 10, 1)
        else:
            iniTempMedia = getDate(i, 9, rTemporadaAlta+1)

        finTempMedia = getDate(i, 12, 31)

        f.write(values_to_string(['media', iniTempMedia, finTempMedia]))

        if i != lastYear:
            f.write(",\n")
        else:
            f.write(";\n")
    

def getDate(y, m, d):
    return date(year = y, month = m, day = d)

def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")"


if __name__ == '__main__':
    main()