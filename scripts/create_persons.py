import argparse, os, random
from random import randint

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',  help="Input file", default="person_data.in", type=str)
parser.add_argument('-n', '--number', help="Number of people to generate", default=10, type=int)
parser.add_argument('-p', '--proportion', help="Proportion of clients vs directors", default=0.2, type=float)
args = parser.parse_args()

names = []
iden  = []
typei = []

nacionality = ["España", "Estados unidos", "Francia", "Ucrania", "Polonia"]
life        = ["bebe", "niño", "adulto"]

def main():
   create_people()
   create_dirs() 
   create_clis() 

def create_people():
    with open(os.getcwd() + f"/{args.input}", "r") as file:
        person_names = file.read().splitlines()
    
    random.shuffle(person_names)
    
    print("INSERT INTO PERSONA VALUES")
    for i in range(args.number):
        selection = randint(0, 1)
        iden.append(create_dni() if selection == 1 else create_pass())
        typei.append(("dni" if selection == 1 else "pasaporte"))
        names.append(person_names.pop(0))
        print(values_to_string([iden[len(iden)-1], typei[len(typei)-1], names[len(names)-1]]), end="")

        if i != (args.number - 1):
            print(",")
        else:
            print(";")

    print("")

def values_to_string(values):
    return_v = "("
    for i in range(len(values)):
        return_v += f"'{values[i]}'"
        if i != len(values) - 1:
            return_v += ", "

    return return_v + ")" 

def create_dirs():
    n_dir = int(len(iden) * args.proportion)

    print("INSERT INTO DIRECTOR VALUES")
    for i in range(n_dir):
        print(values_to_string([iden[0], ''.join(["{}".format(randint(0, 9)) for num in range(0, 9)]),create_mail(names[i])]), end="") 
        iden.pop(0)
        if i != (n_dir - 1):
            print(",")
        else:
            print(";")

    print("")


def create_clis():
    print("INSERT INTO CLIENTE VALUES")
    ID_CLI = []
    for i in range(len(iden)):
        print(values_to_string([iden[i], random.choice(nacionality), random.choice(life)]), end="")
        ID_CLI.append(iden[i])
        if i != (len(iden)-1):
            print(",")
        else:
            print(";")
    with open(os.getcwd() + "/DATA_ID_CLI.out", "w") as file:
        for i in range(len(ID_CLI)):
            file.write(ID_CLI[i] + "\n")

    print("")

def create_mail(name):
    return name.split(" ")[0].lower() + "." + name.split(" ")[1].lower() + "@gmail.com"

def create_dni():
    return str(''.join(["{}".format(randint(0, 9)) for num in range(0, 8)]) + chr(random.randint(ord('A'), ord('Z')))) 

def create_pass():
    return str(chr(random.randint(ord('A'), ord('Z'))) + ''.join(["{}".format(randint(0, 9)) for num in range(0, 5)]) + chr(random.randint(ord('A'), ord('Z'))))

if __name__ == "__main__":
    main()