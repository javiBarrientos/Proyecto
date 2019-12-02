from importarXml import parsearXml


def test_CasoTestXml():
    assert len(parsearXml()) == 50
