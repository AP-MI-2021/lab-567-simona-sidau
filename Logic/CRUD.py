from Domain.librarie import creaza_vanzare, get_id


def adaugare_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    Adauga o vanzare in lista
    :param id: id-ul vanzarii - string
    :param titlu: titlul cartii -string
    :param gen: genul cartii - string
    :param pret: pretul cartii - float
    :param reducere: tipul de reducere al vanzarii (none, silver, gold) - string
    :param lista: lista de vanzari
    :return: lista veche + noua vanzare
    """
    vanzare = creaza_vanzare(id, titlu, gen, pret, reducere)
    return lista + [vanzare]


def get_by_id(id, lista):
    """
    Gaseste vanzarea cu id-ul dat dintr-o lista
    :param id: string
    :param lista: lista de vanzari
    :return: returneaza vanzarea cu id-ul dat sau none daca nu exista
    """
    for vanzare in lista:
        if get_id(vanzare) == id:
            return vanzare


def sterge_vanzare(id, lista):
    """
    Sterge o vanzare dintr-o lista dupa id
    :param id: string
    :param lista: lista de vanzari
    :return: lista de vanzari obtinuta in urma stergerii vanzarii cu id-ul dat
    """
    return [vanzare for vanzare in lista if get_id(vanzare) != id]


def modifica_vanzare(id, titlu, gen, pret, reducere, lista):
    """
    Modifica o vanzare dupa id
    :param id: id-ul dupa care se face modidicarea
    :param titlu: noul titlu - string
    :param gen: noul gen - string
    :param pret: noul pret - float
    :param reducere: noul tip de reducere - string
    :param lista: lista de vanzari
    :return: lista de vanzari obtinuta in urma modificarilor
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o vanzare cu id-ul dat")
    lista_noua = []
    for vanzare in lista:
        if get_id(vanzare) == id:
            vanzare_noua = creaza_vanzare(id, titlu, gen, pret, reducere)
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(vanzare)
    return lista_noua


def adauga_vanzare_undo_redo(id, titlu, gen, pret, reducere, lista, undo_list, redo_list):
    """
    Adauga o vanzare in lista
    :param id: string
    :param titlu: string
    :param gen: string
    :param pret: float
    :param reducere: strig
    :param lista: string
    :param undo_list:
    :param redo_list:
    :return: returneaza o lista continand atat vanzarile vechi cat si cele noi
    """
    if get_by_id(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    vanzare = creaza_vanzare(id, titlu, gen, pret, reducere)
    undo_list.append(lista)
    redo_list.clear()
    return lista + [vanzare]
