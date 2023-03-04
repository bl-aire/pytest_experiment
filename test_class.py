# You can group multiple tests in a class

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