import random

def main():
    roomType = ['individual', 'doble']
    hotelNames = ['Canyes Blanques', 'Condesa', 'Citric Soller', 'Saratoga', 
    'Nordeste Playa', 'PortBlue Club Pollentia Resort & Spa', 'Tent Capi Playa', 
    'Amic Horizonte', 'Estrella', 'Cappuccino', 'Vell Mari Hotel & Resort', 'Hostal Bonany']

    firstRoomNumber = 300 
    lastRoomNumber = 351

    f = open("roomsData.out", "a")
    f.write("INSERT INTO habitacion (num_hab, nombre_hot, tipo_hab) VALUES\n")

    for i in range(len(hotelNames)):
        for j in range(firstRoomNumber, lastRoomNumber):
            r = random.randint(0,1)
            f.write(f"('{j}', '{hotelNames[i]}', '{roomType[r]}')")
            if i == len(hotelNames)-1:
                if j == lastRoomNumber-1:
                    f.write(";\n")
                else:
                    f.write(",\n")
            else:
                f.write(",\n")



if __name__ == '__main__':
    main()