# You can specify additional plugins to pytest.main:

# Run "python myinvoke.py"........in my case, i used python3. It ran all my tests and printed the string when all tests were T
import sys

import pytest


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))


# pytest.main() will result in importing your tests and any modules that they import. 
# Due to the caching mechanism of python’s import system, 
# making subsequent calls to pytest.main() from the same process will not reflect changes to those files between the calls. 
# For this reason, making multiple calls to pytest.main() from the same process (in order to re-run tests, for example) is not recommended.