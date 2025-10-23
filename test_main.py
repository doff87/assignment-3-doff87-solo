from main import calculate_total, calculate_average, find_max, find_min
import pytest

itemsInts = [1, 2, 3]
itemsFloats = [1.0, 2.0, 3.0]
itemsEmpty = []
itemsNone = None
itemsStrings = ["Hello", "Hi", "Howdy"]



def test_calculate_total_ints():
    """Total of [1, 2, 3] should be 6"""
    #arrange
    itemsInts

    #act
    result = calculate_total(itemsInts)

    #assert
    assert result == 6

def test_calculate_total_floats():
    """Total of [1.0, 2.0, 3.0] should be 6.0"""
    #arrange
    itemsFloats

    #act
    result = calculate_total(itemsInts)

    #assert
    assert result == 6.0

def test_calculate_total_empty():
    """Empty list should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsEmpty

    #act
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_calculate_total_none():
    """None object should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsNone

    #act
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_calculate_total_strings():
    """String object in list will raise Value error"""
    #arrange
    itemsStrings

    #act
    with pytest.raises(ValueError) as errorMsg:
        calculate_total(itemsStrings)

    #assert
    assert "Error: All provided values must be numeric." in str(errorMsg.value)