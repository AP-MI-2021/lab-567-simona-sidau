from Domain.librarie import get_id, get_titlu, get_gen, get_pret, get_reducere
from Logic.CRUD import adaugare_vanzare, sterge_vanzare, get_by_id, modifica_vanzare


def test_adaugare_vanzare():
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezie", 12, "none", lista)

    assert len(lista) == 1
    assert get_id(lista[0]) == "1"
    assert get_titlu(lista[0]) == "Plumb"
    assert get_gen(lista[0]) == "Poezie"
    assert get_pret(lista[0]) == 12
    assert get_reducere(lista[0]) == "none"


def test_sterge_vanzare():
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezie", 12, "none", lista)
    lista = adaugare_vanzare("2", "You", "Filosofie", 52, "silver", lista)

    lista = sterge_vanzare("1", lista)

    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_modifica_vanzare():
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezii", 17, "none", lista)
    lista = adaugare_vanzare("2", "You", "Dezvoltare Personala", 58, "silver", lista)

    lista = modifica_vanzare("1", "Ion", "Roman", 25, "gold", lista)

    vanzare_updatata = get_by_id("1", lista)
    assert get_id(vanzare_updatata) == "1"
    assert get_titlu(vanzare_updatata) == "Ion"
    assert get_gen(vanzare_updatata) == "Roman"
    assert get_pret(vanzare_updatata) == 25
    assert get_reducere(vanzare_updatata) == "gold"

    vanzare_neupdatata = get_by_id("2", lista)
    assert get_id(vanzare_neupdatata) == "2"
    assert get_titlu(vanzare_neupdatata) == "You"
    assert get_gen(vanzare_neupdatata) == "Dezvoltare Personala"
    assert get_pret(vanzare_neupdatata) == 58
    assert get_reducere(vanzare_neupdatata) == "silver"



