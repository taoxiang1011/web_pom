import os
import time

import pytest


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system("allure generate ./temp -o ./report --clean")