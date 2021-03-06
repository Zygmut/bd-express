import numpy as np
import random
from random import randrange

instalations = ["piscina", "discoteca", "campo de golf", "bar", "pista de tenis", "jacuzzi", "comedor", "gym"]
hotelNames = ['Canyes Blanques', 'Condesa', 'Citric Soller', 'Saratoga', 'Nordeste Playa', 'PortBlue Club Pollentia Resort & Spa', 'Tent Capi Playa', 'Amic Horizonte', 'Estrella', 'Cappuccino', 'Vell Mari Hotel & Resort', 'Hostal Bonany']

random_alq =[]

def main():
    print("INSERT INTO INSTALACION (nombre_ins, nombre_hot) VALUES ")
    num = 0
    for i in range(len(hotelNames)):
        ins_subset = np.random.choice(instalations, randrange(int(len(instalations) * 0.7)), replace=False)
        for ins in range(len(ins_subset)):
            num += 1
            print(values_to_string([ins_subset[ins], hotelNames[i]]), end="")

            if 1 == randrange(1, 3):
                random_alq.append(num)

            if i == (len(hotelNames) - 1):
                if (ins == (len(ins_subset) - 1)):
                    print(";")
                else:
                    print(",")
            else:
                print(",")

    print("\nINSERT INTO ALQUILABLE VALUES")
    for i in range(len(random_alq)):
        print(values_to_string([random_alq[i]]), end="")
        
        if i != (len(random_alq) - 1):
            print(",")
        else:
            print(";")

def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")" 

if __name__ == "__main__":
    main()