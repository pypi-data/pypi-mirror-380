from acronym_expander import AcronymExpander

def test_expansion():
    ae = AcronymExpander()
    s = "WHO met UN in NYC."
    out = ae.expand(s)
    assert "World Health Organization" in out
    assert "United Nations" in out
    assert "New York City" in out
