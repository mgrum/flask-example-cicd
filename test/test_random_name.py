from flaskr import random_name
import random


def test_type():
    random_name.lis_names = ["Test"]
    assert isinstance(random_name.random_name(), str)
    random_name.lis_names = [1, 2, 3]
    assert isinstance(random_name.random_name(), str)


def test_randomness():
    expected = []
    result = []
    random_name.lis_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Fill expected list
    random.seed("Test")
    for _ in range(10):
        index = random.randint(0, len(random_name.lis_names)-1)
        expected.append(str(random_name.lis_names[index]))
    # Fill result list
    random_name.random.seed("Test")
    for _ in range(10):
        result.append(random_name.random_name())
    assert expected == result
