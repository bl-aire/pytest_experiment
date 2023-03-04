# Making use of context-sensitive comparisons

def test_set_comparison():
    set1 = set("1234")
    set2 = set("4567")
    assert set1 == set2 # pytest has rich support for providing context-sensitive information when it encounters comparisons