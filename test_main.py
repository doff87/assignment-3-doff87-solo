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
    """Total of [1, 2, 3] should be 6"""
    #arrange
    itemsEmpty

    #act
    result = calculate_total(itemsEmpty)

    #assert
    assert result == 6