import argparse, os, random
from random import randrange

parser = argparse.ArgumentParser()
parser.add_argument('-Mp', '--maxPrice',  help="Max price value", default=1000, type=int)
parser.add_argument('-mp', '--minPrice',  help="Min price value", default=100, type=int)
args = parser.parse_args()

REG = ["SH", "HD", "MP", "PC"]
with open("DATA_SEASONS.out", "r") as file:
    N_TEM = int(file.read())

def main():
    create_prices()
    link_hot()
    link_alq()

def create_prices():
    print("INSERT INTO PRECIO (precio, id_tem, tipo_reg) VALUES")
    for i in range(N_TEM ):
        for j in range(len(REG)):
            print(values_to_string([randrange(args.minPrice,args.maxPrice), i+1, REG[j]] ), end=",\n")
            print(values_to_string([randrange(args.minPrice,args.maxPrice), i+1, REG[j]] ), end=",\n")

            print(values_to_string([randrange(50, 100), i+1, REG[j]] ), end=",\n")
            print(values_to_string([randrange(50, 100), i+1, REG[j]] ), end="")
            
            if i == N_TEM-1:
                if j == len(REG)-1:
                    print(";")
                else:
                    print(",")
            else:
                print(",")

def link_hot():
    pass

def link_alq():
    pass

def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")" 

if __name__ == "__main__":
    main()
