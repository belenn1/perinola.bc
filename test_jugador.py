from jugador import jugador

def test_constructor_sin_fichas():
    j = jugador("b")
    assert(j.nombre == "b" )
    assert(j.fichas == 5)

def test_dar_ficha():
    j = jugador("b", 10)
    j.darFicha(5)
    assert(j.fichas == 15)




    