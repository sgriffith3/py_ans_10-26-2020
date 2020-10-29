# Example test case

import pytest

def multi_add(x, y, z):
    return (x * y) + z


# print(multi_add(10, 5, 4))

def test_multi_add():
    assert multi_add(10, 3, 3) == 33

    with pytest.raises(TypeError):
        multi_add(10, 4, 3)




