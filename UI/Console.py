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
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare lista vanzari")
    print("x. Exit")


def ui_adaugare_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii ")
        titlu = input("Dati titlul cartii ")
        gen = input("Dati genul cartii ")
        pret = float(input("Dati pretul cartii "))
        reducere = input("Dati tipul de reducere ")
        if get_by_id(id, lista) is not None:
            raise ValueError("Id-ul exista deja!")
        rezultat = adaugare_vanzare(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def ui_sterge_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii ce urmeaza sa fie stearsa ")
        rezultat = sterge_vanzare(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_mofificare_vanzare(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul vanzarii de modificat ")
        titlu = input("Dati noul titlul al cartii ")
        gen = input("Dati noul gen al cartii ")
        pret = float(input("Dati noul pret al cartii "))
        reducere = input("Dati noul tip de reducere ")
        rezultat = modifica_vanzare(id, titlu, gen, pret, reducere, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def afisare(lista):
    for vanzare in lista:
        print(to_string(vanzare))


def ui_reducere_pret(lista, undo_list, redo_list):
    rezultat = reducere_pret(lista)
    undo_list.append(lista)
    redo_list.clear()
    return rezultat


def ui_modificare_gen_pt_titlu_dat(lista, undo_list, redo_list):
    try:
        titlu = input("Introduceti titlul cartii: ")
        gen_nou = input("Introduceti noul gen al cartii: ")
        rezultat = modificare_gen_pt_titlu_dat(lista, titlu, gen_nou)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_pret_minim_per_gen(lista):
    rezultat = pret_minim_per_gen(lista)
    for gen in rezultat:
        print("Genul {} are ca pret minim {} lei".format(gen, rezultat[gen]))


def ui_ordonare_dupa_pret(lista, undo_list, redo_list):
    undo_list.append(lista)
    redo_list.clear()
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
    print("add. Adaugare vanzare (id, titlu, gen, pret, tip reducere)")
    print("delete. Sterge vanzare")
    print("show all. Show all")
    print("x. Exit")


def ui_add(lista, option):
    try:
        id = option[1]
        titlu = option[2]
        gen = option[3]
        pret = int(option[4])
        reducere = option[5]
        if get_by_id(id, lista) is not None:
            raise ValueError("Id-ul exista deja!")
        return adaugare_vanzare(id, titlu, gen, pret, reducere, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def ui_delete(lista, option):
    id = option[1]
    return sterge_vanzare(id, lista)


def run_menu(lista):
    undo_list = []
    redo_list = []
    while True:
        print_console_menu()
        optiune = input("Alegeti consola pe care o doriti: ")
        if optiune == "i":
            while True:
                print_menu()
                optiune = input("Dati optiunea: ")

                if optiune == "1":
                    lista = ui_adaugare_vanzare(lista, undo_list, redo_list)
                elif optiune == "2":
                    lista = ui_sterge_vanzare(lista, undo_list, redo_list)
                elif optiune == "3":
                    lista = ui_mofificare_vanzare(lista, undo_list, redo_list)
                elif optiune == "4":
                    lista = ui_reducere_pret(lista, undo_list, redo_list)
                elif optiune == "5":
                    lista = ui_modificare_gen_pt_titlu_dat(lista, undo_list, redo_list)
                elif optiune == "6":
                    ui_pret_minim_per_gen(lista)
                elif optiune == "7":
                    ui_ordonare_dupa_pret(lista, undo_list, redo_list)
                elif optiune == "8":
                    ui_numar_titluri_distincte_per_gen(lista)
                elif optiune == "u":
                    if len(undo_list) > 0:
                        redo_list.append(lista)
                        lista = undo_list.pop()
                    else:
                        print("Nu se poate face undo!")
                elif optiune == "r":
                    if len(redo_list) > 0:
                        undo_list.append(lista)
                        lista = redo_list.pop()
                    else:
                        print("Nu se poate face redo!")
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
                command_line = input("Introduceti comenzile separete prin punct si virgula,"
                                     " iar specificatiile prin virgula: ")
                option_line = command_line.split(";")
                for ajutor in option_line:
                    option = ajutor.split(",")
                    if option[0] == "add":
                        lista = ui_add(lista, option)
                        print("Optiunea add realizata!")
                    elif option[0] == "show all":
                        afisare(lista)
                        print("Optiunea show all realizata")
                    elif option[0] == "delete":
                        lista = ui_delete(lista, option)
                        print("Optiunea delete realizata")
                    elif option[0] == "x":
                        should_run = False
                        break
                    else:
                        print("Optiunea {} nu exista. Reincercati".format(option[0]))

        elif optiune == "x":
            break
        else:
            print("Optiune inexistenta. Reincercati!")
