import os, random
from random import randint

NUM_TAR  = []

type_tar = ["visa", "mastercard", "american express"]

def main():

    payer_cli_prop = 0.3

    with open(os.getcwd() + "/DATA_ID_CLI.out", "r") as file:
        ID_CLI = file.read().splitlines()
    
    print("INSERT INTO TARJETA VALUES")

    for i in range(int(len(ID_CLI) * payer_cli_prop)):
        NUM_TAR.append(''.join(["{}".format(randint(0, 9)) for num in range(0, 16)]))        
        print(values_to_string([NUM_TAR[len(NUM_TAR)-1], random.choice(type_tar), random.choice(ID_CLI) ]), end="")
        if i != (int(len(ID_CLI) * payer_cli_prop) - 1):
            print(",")
        else:
            print(";")

    with open(os.getcwd() + "/DATA_NUM_TAR.out", "w") as file:
        for i in range(len(NUM_TAR)):
            file.write(NUM_TAR[i] + "\n")
   
def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")" 

if __name__ == '__main__':
    main()