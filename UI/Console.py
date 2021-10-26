from Domain.librarie import to_string
from Logic.CRUD import adaugare_vanzare, sterge_vanzare, modifica_vanzare


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("a. Afisare lista vanzari")
    print("x. Exit")


def ui_adaugare_vanzare(lista):
    id = input("Dati id-ul vanzarii ")
    titlu = input("Dati titlul cartii ")
    gen = input("Dati genul cartii ")
    pret = float(input("Dati pretul cartii "))
    reducere = input("Dati tipul de reducere ")
    return adaugare_vanzare(id, titlu, gen, pret, reducere, lista)


def ui_sterge_vanzare(lista):
    id = input("Dati id-ul vanzarii ce urmeaza sa fie stearsa ")
    return sterge_vanzare(id, lista)


def ui_mofificare_vanzare(lista):
    id = input("Dati id-ul vanzarii de modificat ")
    titlu = input("Dati noul titlul al cartii ")
    gen = input("Dati noul gen al cartii ")
    pret = float(input("Dati noul pret al cartii "))
    reducere = input("Dati noul tip de reducere ")
    return modifica_vanzare(id, titlu, gen, pret, reducere, lista)


def afisare(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def run_menu(lista):
    while True:
        print_menu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = ui_adaugare_vanzare(lista)
        elif optiune == "2":
            lista = ui_sterge_vanzare(lista)
        elif optiune == "3":
            lista = ui_mofificare_vanzare(lista)
        elif optiune == "a":
            afisare(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune inexistenta! Reincercati!")
