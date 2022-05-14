import random, os, datetime

NUM_TAR = []

def main():
    tipoRegimen = ['SH', 'HD', 'MP', 'PC']
    firstYear = 2019
    lastYear = 2022

    with open (os.getcwd() + "/DATA_NUM_TAR.out", "r") as file:
        NUM_TAR = file.read().splitlines()

    f = open("bookingData.out", "a")

    f.write("INSERT INTO RESERVA (fecha_ini_res, fecha_fin_res, tipo_reg, num_tar) VALUES\n")

    for i in range (firstYear, lastYear):
        start_date = datetime.date(i, 1, 1)
        end_date = datetime.date(i, 12, 31)
        for j in range (1, 51):
            rInitDate = randomDate(start_date, end_date)
            r = random.randint(1, 30)
            rFinDate = rInitDate + datetime.timedelta(days=r)

            regimenRandom = random.randint(0,3)

            f.write(values_to_string([rInitDate, rFinDate, tipoRegimen[regimenRandom], random.choice(NUM_TAR)]))

            if i == lastYear and j == 50:
                f.write(";\n")
            else:
                f.write(",\n")
    
def randomDate(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)

def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")"


if __name__ == '__main__':
    main()