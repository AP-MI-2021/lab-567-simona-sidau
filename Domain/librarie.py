def creaza_vanzare(id, titlu, gen, pret, reducere):
    """
    Creaza un dictionar ce retine o vanzare
    :param id: id-ul vanzarii - string
    :param titlu: titlul cartii - string
    :param gen: genul cartii - string
    :param pret: pretul cartii - float
    :param reducere: tipul de reducere aplicata (none, silver, gold) - string
    :return: un dictionar ce retine o vanzare
    """
    return{
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "reducere": reducere
    }


def get_id(vanzare):
    """
    Gaseste id-ul unei vanzari
    :param vanzare: un dictionar de tip vanzare
    :return: id-ul unei vanzari
    """
    return vanzare["id"]


def get_titlu(vanzare):
    """
    Gaseste titlul cartii dintr-o vanzare
    :param vanzare: un dictionar de tip vanzare
    :return: titlul unei vanzari - string
    """
    return vanzare["titlu"]


def get_gen(vanzare):
    """
    Gaseste genul unei carti dintr-o vanzare
    :param vanzare: un dictionar de tip vanzare
    :return: genul unei carti dintr-o vanzare - string
    """
    return vanzare["gen"]


def get_pret(vanzare):
    """
    Gaseste pretul unei carti dintr-o vanzare
    :param vanzare: un dictionar de tip vanzare
    :return: pretul cartii - float
    """
    return vanzare["pret"]


def get_reducere(vanzare):
    """
    Gaseste tipul reducerii dintr-o vanzare
    :param vanzare: un dictionar de tip vanzare
    :return: tipul reducerii - string
    """
    return vanzare["reducere"]


def to_string(vanzare):
    return "id: {}, titlu: {}, gen: {}, pret: {}, reducere:{}".format(
        get_id(vanzare),
        get_titlu(vanzare),
        get_gen(vanzare),
        get_pret(vanzare),
        get_reducere(vanzare)
    )
