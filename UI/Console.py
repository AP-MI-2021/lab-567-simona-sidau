from Domain.librarie import to_string
from Logic.CRUD import adaugare_vanzare, sterge_vanzare, modifica_vanzare, get_by_id
from Logic.functionalitati import reducere_pret, modificare_gen_pt_titlu_dat, pret_minim_per_gen, ordonare_dupa_pret, \
    numar_titluri_distincte_per_gen


def print_menu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Reducere pret")
    print("5. Modificare genului pentru un titlu dat")
    print("6. Afisare pret minim pentru fiecare gen")
    print("7. Afisarea vanzarilor crescator in functie de pret")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("a. Afisare lista vanzari")
    print("x. Exit")


def ui_adaugare_vanzare(lista):
    try:
        id = input("Dati id-ul vanzarii ")
        titlu = input("Dati titlul cartii ")
        gen = input("Dati genul cartii ")
        pret = float(input("Dati pretul cartii "))
        reducere = input("Dati tipul de reducere ")
        if get_by_id(id, lista) is not None:
            raise ValueError("Id-ul exista deja!")
        return adaugare_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def ui_sterge_vanzare(lista):
    id = input("Dati id-ul vanzarii ce urmeaza sa fie stearsa ")
    return sterge_vanzare(id, lista)


def ui_mofificare_vanzare(lista):
    try:
        id = input("Dati id-ul vanzarii de modificat ")
        titlu = input("Dati noul titlul al cartii ")
        gen = input("Dati noul gen al cartii ")
        pret = float(input("Dati noul pret al cartii "))
        reducere = input("Dati noul tip de reducere ")
        return modifica_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def afisare(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_reducere_pret(lista):
    return reducere_pret(lista)


def ui_modificare_gen_pt_titlu_dat(lista):
    titlu = input("Introduceti titlul cartii: ")
    gen_nou = input("Introduceti noul gen al cartii: ")
    return modificare_gen_pt_titlu_dat(lista, titlu, gen_nou)


def ui_pret_minim_per_gen(lista):
    rezultat = pret_minim_per_gen(lista)
    for gen in rezultat:
        print("Genul {} are ca pret minim {} lei".format(gen, rezultat[gen]))


def ui_ordonare_dupa_pret(lista):
    afisare(ordonare_dupa_pret(lista))


def ui_numar_titluri_distincte_per_gen(lista):
    rezultat = numar_titluri_distincte_per_gen(lista)
    for gen in rezultat:
        print("Genul {} are {} titluri distincte".format(gen, rezultat[gen]))


def print_console_menu():
    print("i. Consola veche")
    print("ii. Command line console ")
    print("x.Exit")


def print_comand_line_console_menu():
    print("1. Adaugare vanzare")
    print("2. Sterge vanzare")
    print("3. Show all")
    print("x. Exit")


def run_menu(lista):
    while True:
        print_console_menu()
        optiune = input("Alegeti consola pe care o doriti: ")
        if optiune == "i":
            while True:
                print_menu()
                optiune = input("Dati optiunea: ")

                if optiune == "1":
                    lista = ui_adaugare_vanzare(lista)
                elif optiune == "2":
                    lista = ui_sterge_vanzare(lista)
                elif optiune == "3":
                    lista = ui_mofificare_vanzare(lista)
                elif optiune == "4":
                    lista = ui_reducere_pret(lista)
                elif optiune == "5":
                    lista = ui_modificare_gen_pt_titlu_dat(lista)
                elif optiune == "6":
                    ui_pret_minim_per_gen(lista)
                elif optiune == "7":
                    ui_ordonare_dupa_pret(lista)
                elif optiune == "8":
                    ui_numar_titluri_distincte_per_gen(lista)
                elif optiune == "a":
                    afisare(lista)
                elif optiune == "x":
                    break
                else:
                    print("Optiune inexistenta! Reincercati!")
        elif optiune == "ii":
            should_run = True
            while should_run:
                print_comand_line_console_menu()
                linie_optiune = input("Introduceti comenzile separete prin virgula: ")
                ajutor_optiune = linie_optiune.split(",")
                for optiune in ajutor_optiune:
                    if optiune == "1":
                        lista = ui_adaugare_vanzare(lista)
                        print("Optiunea 1 realizata cu succes!")
                    elif optiune == "2":
                        lista = ui_sterge_vanzare(lista)
                        print("Optiunea 2 realizata cu succes!")
                    elif optiune == "3":
                        afisare(lista)
                        print("Optiunea 3 realizata cu succes!")
                    elif optiune == "x":
                        should_run = False
                        break
                    else:
                        print("Optiunea {} este inexistenta! Reincercati".format(optiune))
        elif optiune == "x":
            break
        else:
            print("Optiune inexistenta. Reincercati!")
