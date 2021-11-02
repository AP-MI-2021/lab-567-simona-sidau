from Domain.librarie import get_pret, get_gen, get_id
from Logic.CRUD import adaugare_vanzare, get_by_id
from Logic.functionalitati import reducere_pret, modificare_gen_pt_titlu_dat, pret_minim_per_gen, ordonare_dupa_pret, \
    numar_titluri_distincte_per_gen


def test_reducere_pret():
    lista = []
    lista = adaugare_vanzare("1", "Grecia antica", "Istorie", 20, "gold", lista)
    lista = adaugare_vanzare("2", "Heavier than heaven", "Biografie", 100, "silver", lista)
    lista = adaugare_vanzare("3", "The trouble with being born", "Filosofie", 17, "none", lista)

    lista = reducere_pret(lista)

    assert get_pret(get_by_id("1", lista)) == 18
    assert get_pret(get_by_id("2", lista)) == 95
    assert get_pret(get_by_id("3", lista)) == 17


def test_modificare_gen_pt_titlu_dat():
    lista = []
    lista = adaugare_vanzare("1", "Rauri si munti", "Istorie", 20, "gold", lista)
    lista = adaugare_vanzare("2", "Heavier than heaven", "Biografie", 100, "silver", lista)
    lista = adaugare_vanzare("3", "The trouble with being born", "Filosofie", 17, "none", lista)

    lista = modificare_gen_pt_titlu_dat(lista, "The trouble with being born", "Psihologie")
    lista = modificare_gen_pt_titlu_dat(lista, "Rauri si munti", "Geografie")

    assert get_gen(get_by_id("1", lista)) == "Geografie"
    assert get_gen(get_by_id("3", lista)) == "Psihologie"
    assert get_gen(get_by_id("2", lista)) == "Biografie"


def test_pret_minim_per_gen():
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezii", 17, "gold", lista)
    lista = adaugare_vanzare("2", "Luceafarul", "Poezii", 27, "silver", lista)
    lista = adaugare_vanzare("3", "Heavier than heaven", "Biografie", 45, "silver", lista)
    lista = adaugare_vanzare("4", "You", "Dezvoltare personala", 87, "none", lista)
    lista = adaugare_vanzare("5", "Coco Chanel", "Biografie", 117, "gold", lista)

    rezultat = pret_minim_per_gen(lista)

    assert len(rezultat) == 3
    assert rezultat["Poezii"] == 17
    assert rezultat["Biografie"] == 45
    assert rezultat["Dezvoltare personala"] == 87


def test_ordonare_dupa_pret():
    lista = []
    lista = adaugare_vanzare("1", "Grecia antica", "Istorie", 20, "gold", lista)
    lista = adaugare_vanzare("2", "Heavier than heaven", "Biografie", 1117, "silver", lista)
    lista = adaugare_vanzare("3", "Coco Chanel", "Biografie", 100, "gold", lista)

    rezultat = ordonare_dupa_pret(lista)

    assert get_id(rezultat[0]) == "1"
    assert get_id(rezultat[1]) == "3"
    assert get_id(rezultat[2]) == "2"


def test_numar_titluri_distincte_per_gen():
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezii", 17, "gold", lista)
    lista = adaugare_vanzare("2", "Luceafarul", "Poezii", 27, "silver", lista)
    lista = adaugare_vanzare("3", "Heavier than heaven", "Biografie", 45, "silver", lista)
    lista = adaugare_vanzare("4", "You", "Dezvoltare personala", 87, "none", lista)
    lista = adaugare_vanzare("5", "Coco Chanel", "Biografie", 117, "gold", lista)

    rezultat = numar_titluri_distincte_per_gen(lista)

    assert len(rezultat) == 3
    assert rezultat["Poezii"] == 2
    assert rezultat["Biografie"] == 2
    assert rezultat["Dezvoltare personala"] == 1
