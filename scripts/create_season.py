import random
from datetime import date

def main():

    firstYear = 2019
    lastYear = 2022

    print("INSERT INTO TEMPORADA (tipo_tem, fecha_ini_tem, fecha_fin_tem) VALUES")
    for i in range(firstYear, lastYear+1):

        rTemporadaBaja = random.randint(1,31)
        rTemporadaAlta = random.randint(1, 30)

        iniTempBaja = getDate(i, 1, 1)
        finTempBaja = getDate(i, 5, rTemporadaBaja)

        print(values_to_string(['baja', iniTempBaja, finTempBaja]), end="")
        print(",")

        iniTempAlta = ""

        if rTemporadaBaja == 31:
            iniTempAlta = getDate(i, 6, 1)
        else:
            iniTempAlta = getDate(i, 5, rTemporadaBaja+1)

        finTempAlta = getDate(i, 9, rTemporadaAlta)

        print(values_to_string(['alta', iniTempAlta, finTempAlta]), end="")
        print(",")

        iniTempMedia = ""

        if rTemporadaAlta == 30:
            iniTempMedia = getDate(i, 10, 1)
        else:
            iniTempMedia = getDate(i, 9, rTemporadaAlta+1)

        finTempMedia = getDate(i, 12, 31)

        print(values_to_string(['media', iniTempMedia, finTempMedia]), end="")

        if i != lastYear:
            print(",")
        else:
            print(";\n")

        with open("DATA_SEASONS.out", "w") as file:
            file.write(str(1 + lastYear - firstYear))

        
    

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