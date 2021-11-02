from Tests.test_Crud import test_adaugare_vanzare, test_sterge_vanzare, test_modifica_vanzare, test_get_by_id
from Tests.test_domain import test_vanzare
from Tests.test_functionalitati import test_reducere_pret, test_modificare_gen_pt_titlu_dat, test_pret_minim_per_gen, \
    test_ordonare_dupa_pret, test_numar_titluri_distincte_per_gen


def run_all_tests():
    test_vanzare()
    test_adaugare_vanzare()
    test_sterge_vanzare()
    test_modifica_vanzare()
    test_reducere_pret()
    test_get_by_id()
    test_modificare_gen_pt_titlu_dat()
    test_pret_minim_per_gen()
    test_ordonare_dupa_pret()
    test_numar_titluri_distincte_per_gen()
