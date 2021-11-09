from Logic.CRUD import adauga_vanzare_undo_redo, get_by_id
from Logic.functionalitati import undo, redo


def test_undo_redo():
    lista = []
    undo_lst = []
    redo_lst = []

    lista = adauga_vanzare_undo_redo("1", "Rauri si munti", "Istorie", 20, "gold", lista, undo_lst, redo_lst)
    lista = adauga_vanzare_undo_redo("2", "Heavier than heaven", "Biografie", 100, "silver", lista, undo_lst, redo_lst)
    lista = adauga_vanzare_undo_redo("3", "Amurg", "Filosofie", 17, "none", lista, undo_lst, redo_lst)

    assert len(lista) == 3

    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 2

    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 1

    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 0

    lista = undo(lista, undo_lst, redo_lst)

    assert lista == []

    lista = []
    undo_lst = []
    redo_lst = []

    lista = adauga_vanzare_undo_redo("1", "Rauri si munti", "Istorie", 20, "gold", lista, undo_lst, redo_lst)
    lista = adauga_vanzare_undo_redo("2", "Heavier than heaven", "Biografie", 100, "silver", lista, undo_lst, redo_lst)
    lista = adauga_vanzare_undo_redo("3", "Amurg", "Filosofie", 17, "none", lista, undo_lst, redo_lst)

    assert len(lista) == 3

    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 3

    lista = undo(lista, undo_lst, redo_lst)
    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 1

    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 2
    assert get_by_id("2", lista) is not None

    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 3
    assert get_by_id("3", lista) is not None

    lista = undo(lista, undo_lst, redo_lst)
    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 1
    assert get_by_id("2", lista) is None
    assert get_by_id("3", lista) is None

    lista = adauga_vanzare_undo_redo("4", "Coco Chanel", "Biografie", 117, "gold", lista, undo_lst, redo_lst)

    assert len(lista) == 2

    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 2

    lista = undo(lista, undo_lst, redo_lst)

    assert len(lista) == 1

    lista = redo(lista, undo_lst, redo_lst)
    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 2

    lista = redo(lista, undo_lst, redo_lst)

    assert len(lista) == 2