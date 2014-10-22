from fizz_buzz import fizz_buzz


def test_fizz_buzz():
    assert fizz_buzz()


def test_first_element():
    first = fizz_buzz()[0]
    assert first == 1


# def test_returns_1_to_100():
#     assert fizz_buzz() == range(1, 101)


def test_3_return_fizz(capsys):
    fizz_buzz()
    output, _ = capsys.readouterr()
    third = output.splitlines()[2]
    assert third == 'fizz'


def test_5_return_buzz():
    fifth = fizz_buzz()[4]
    assert fifth == 'buzz'

def test_15_return_fizzbuzz():
    fifteen = fizz_buzz()[14]
    assert fifteen == 'fizzbuzz'


def test_prints(capsys):
    fizz_buzz()
    output, _= capsys.readouterr()
    assert not output
