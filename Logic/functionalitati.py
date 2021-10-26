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