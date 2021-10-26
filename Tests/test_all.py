from Tests.test_Crud import test_adaugare_vanzare, test_sterge_vanzare, test_modifica_vanzare
from Tests.test_domain import test_vanzare


def run_all_tests():
    test_vanzare()
    test_adaugare_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
