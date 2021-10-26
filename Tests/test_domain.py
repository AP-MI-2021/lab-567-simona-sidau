from Domain.librarie import creaza_vanzare, get_id, get_titlu, get_gen, get_pret, get_reducere


def test_vanzare():
    vanzare = creaza_vanzare("1", "Plumb", "Poezie", 12, "none")

    assert get_id(vanzare) == "1"
    assert get_titlu(vanzare) == "Plumb"
    assert get_gen(vanzare) == "Poezie"
    assert get_pret(vanzare) == 12
    assert get_reducere(vanzare) == "none"
