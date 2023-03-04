# You can group multiple tests in a class. Advantages include:
    # Test organization
    # Sharing fixtures for tests only in that particular class
    # Applying marks at the class level and having them implicitly apply to all tests

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        class Blessing:
            job = "Frontend"
            age = 100

        blessing = Blessing()
        assert hasattr(blessing, "job")


# Something to be aware of when grouping tests inside classes is that each test has a unique instance of the class. 
# Having eachshare the same class instance would be detrimental to test isolation and would promote poor test practices
class TestClassDemoInstance:
    value = 0 # shared between tests as it is a "class attribute"

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1