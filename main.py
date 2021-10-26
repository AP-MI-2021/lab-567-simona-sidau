from Logic.CRUD import adaugare_vanzare
from Tests.test_all import run_all_tests
from UI.Console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adaugare_vanzare("1", "Plumb", "Poezii", 17, "none", lista)
    lista = adaugare_vanzare("2", "You", "Dezvoltare Personala", 58, "silver", lista)
    lista = adaugare_vanzare("3", "Luceafarul", "Poezii", 12, "gold", lista)

    run_menu(lista)


main()
