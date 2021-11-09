from Domain.librarie import creaza_vanzare, get_reducere, get_id, get_titlu, get_gen, get_pret


def reducere_pret(lista):
    """
    Reduce pretul unei carti dupa tipul de reducere
    :param lista: lista de vanzari
    :return: o lista continand atat vanzarile reduse cat si cele nemodificate
    """
    lista_noua = []
    for vanzare in lista:
        if get_reducere(vanzare) == "silver":
            vanzare_noua = creaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) - 5/100*get_pret(vanzare),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        elif get_reducere(vanzare) == "gold":
            vanzare_noua = creaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                get_gen(vanzare),
                get_pret(vanzare) - 1/10*get_pret(vanzare),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)

    return lista_noua


def modificare_gen_pt_titlu_dat(lista, titlu, gen_nou):
    """
    Modifica genul unei carti dintr-o vanzare dupa un titlu dat
    :param lista: lista de vanzari
    :param titlu: titlul cartii ce trebuie modificata - string
    :param gen_nou: noul gen al cartii
    :return: lista in urma modificarii genului cartii cerute
    """
    lista_noua = []
    for vanzare in lista:
        if get_titlu(vanzare) == titlu:
            vanzare_noua = creaza_vanzare(
                get_id(vanzare),
                get_titlu(vanzare),
                gen_nou,
                get_pret(vanzare),
                get_reducere(vanzare)
            )
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua


def pret_minim_per_gen(lista):
    """
    Deetrmina pretul minim pentru fiecare gen din lista de vanzari
    :param lista: lista de vanzari
    :return: dictionar cantinand genul si pretul minim
    """
    rezultat = {}
    for vanzare in lista:
        gen = get_gen(vanzare)
        pret = get_pret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret

    return rezultat


def ordonare_dupa_pret(lista):
    """
    Ordoneaza o lista de vanzari crescator in functie de pret
    :param lista: lista de vanzari
    :return: lista ordonata crescator in functie de pret
    """

    return sorted(lista, key=lambda vanzare: get_pret(vanzare))


def numar_titluri_distincte_per_gen(lista):
    """
    Determina numarul de titluri distincte pentru fiecare gen
    :param lista: lista de vanzari
    :return: dictionar continand genul si numarul de titluri distincte
    """
    rezultat = {}
    for vanzare in lista:
        gen = get_gen(vanzare)
        if gen in rezultat:
            rezultat[gen] = rezultat[gen] + 1
        else:
            rezultat[gen] = 1

    return rezultat


def undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop()
    return lista


def redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    return lista
