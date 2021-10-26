from Tests.test_Crud import test_adaugare_vanzare, test_sterge_vanzare, test_modifica_vanzare
from Tests.test_domain import test_vanzare
from Tests.test_functionalitati import test_reducere_pret


def run_all_tests():
    test_vanzare()
    test_adaugare_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_reducere_pret()
