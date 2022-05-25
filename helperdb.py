import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--mode', help="Show tables, data or all", default="all", type=str)
args = parser.parse_args()

tables = ["TEMPORADA", "REGIMEN", "HOTEL", "TIPO", "HABITACION", "INSTALACION", "ALQUILABLE", "PERSONA", "CLIENTE", "DIRECTOR", "TARJETA", "RESERVA", "USO", "PRECIO", "OCUPACION", "R_ALQUILABLE_PRECIO", "R_HABITACION_PRECIO", "R_HABITACION_RESERVA", "R_RESERVA_CLIENTE" ]

def main():
    print("drop database ch; create database ch; use ch;")
    for table in tables:
        if args.mode == 'tables':
            with open(f"{table}/create", "r", encoding='utf-8') as file: print(file.read() + "\n")

        elif args.mode == "data":
            with open(f"{table}/data", "r", encoding='utf-8') as file: print(file.read() + "\n")
        else:
            with open(f"{table}/create", "r", encoding='utf-8') as file: print(file.read() + "\n")
            with open(f"{table}/data", "r", encoding='utf-8') as file: print(file.read() + "\n")

if __name__ == "__main__":
    main()