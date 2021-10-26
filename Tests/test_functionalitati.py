from Domain.librarie import get_pret
from Logic.CRUD import adaugare_vanzare, get_by_id
from Logic.functionalitati import reducere_pret


def test_reducere_pret():
    lista=[]
    lista = adaugare_vanzare("1", "Grecia antica", "Istorie", 20, "gold", lista)
    lista = adaugare_vanzare("2", "Heavier than heaven", "Biografie", 100, "silver", lista)
    lista = adaugare_vanzare("3", "The trouble with being born", "Filosofie", 17, "none", lista)

    lista = reducere_pret(lista)

    assert get_pret(get_by_id("1", lista)) == 18
    assert get_pret(get_by_id("2", lista)) == 95
    assert get_pret(get_by_id("3", lista)) == 17