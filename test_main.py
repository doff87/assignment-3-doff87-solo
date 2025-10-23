from main import calculate_total, calculate_average, find_max, find_min
import pytest

itemsInts = [1, 2, 3]
itemsFloats = [1.0, 2.0, 3.0]
itemsEmpty = []
itemsNone = None
itemsStrings = ["Hello", "Hi", "Howdy"]


# ============================================================================
# Tests for calculate_total(items)
# ============================================================================


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
    result = calculate_total(itemsFloats)

    #assert
    assert result == 6.0

def test_calculate_total_empty(capsys):
    """Empty list should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsEmpty

    #act
    calculate_total(itemsEmpty)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_calculate_total_none(capsys):
    """None object should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsNone

    #act
    calculate_total(itemsNone)
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

# ============================================================================
# Tests for calculate_average(items)
# ============================================================================

def test_calculate_average_ints():
    """average of [1, 2, 3] should be 2.0"""
    #arrange
    itemsInts

    #act
    result = calculate_average(itemsInts)

    #assert
    assert result == 2.0

def test_calculate_average_floats():
    """average of [1.0, 2.0, 3.0] should be 2.0"""
    #arrange
    itemsFloats

    #act
    result = calculate_average(itemsFloats)

    #assert
    assert result == 2.0

def test_calculate_average_empty(capsys):
    """Empty list should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsEmpty

    #act
    calculate_average(itemsEmpty)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_calculate_average_none(capsys):
    """None object should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsNone

    #act
    calculate_average(itemsNone)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_calculate_average_strings():
    """String object in list will raise Value error"""
    #arrange
    itemsStrings

    #act
    with pytest.raises(ValueError) as errorMsg:
        calculate_average(itemsStrings)

    #assert
    assert "Error: All provided values must be numeric." in str(errorMsg.value)

# ============================================================================
# Tests for find_max(items)
# ============================================================================

def test_find_max_ints():
    """average of [1, 2, 3] should be 3"""
    #arrange
    itemsInts

    #act
    result = find_max(itemsInts)

    #assert
    assert result == 3

def test_find_max_floats():
    """average of [1.0, 2.0, 3.0] should be 3.0"""
    #arrange
    itemsFloats

    #act
    result = find_max(itemsFloats)

    #assert
    assert result == 3.0

def test_find_max_empty(capsys):
    """Empty list should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsEmpty

    #act
    find_max(itemsEmpty)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_find_max_none(capsys):
    """None object should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsNone

    #act
    find_max(itemsNone)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_find_max_strings():
    """String object in list will raise Value error"""
    #arrange
    itemsStrings

    #act
    with pytest.raises(ValueError) as errorMsg:
        find_max(itemsStrings)

    #assert
    assert "Error: All provided values must be numeric." in str(errorMsg.value)


# ============================================================================
# Tests for find_min(items)
# ============================================================================

def test_find_min_ints():
    """average of [1, 2, 3] should be 1"""
    #arrange
    itemsInts

    #act
    result = find_min(itemsInts)

    #assert
    assert result == 1

def test_find_min_floats():
    """average of [1.0, 2.0, 3.0] should be 1.0"""
    #arrange
    itemsFloats

    #act
    result = find_min(itemsFloats)

    #assert
    assert result == 1.0

def test_find_min_empty(capsys):
    """Empty list should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsEmpty

    #act
    find_min(itemsEmpty)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_find_min_none(capsys):
    """None object should return error message of 'No values provided to evaluate.'"""
    #arrange
    itemsNone

    #act
    find_min(itemsNone)
    errorMsg = capsys.readouterr()

    #assert
    assert "No values provided to evaluate." in errorMsg.out

def test_find_min_strings():
    """String object in list will raise Value error"""
    #arrange
    itemsStrings

    #act
    with pytest.raises(ValueError) as errorMsg:
        find_min(itemsStrings)

    #assert
    assert "Error: All provided values must be numeric." in str(errorMsg.value)