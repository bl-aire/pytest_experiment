# Request a unique temporary directory for functional tests

def test_needsfiles(tmp_path):
    print(tmp_path)
    assert 0



# pytest --fixtures   
# shows builtin and custom fixtures
# omits fixtures with leading _ unless the -v option is added