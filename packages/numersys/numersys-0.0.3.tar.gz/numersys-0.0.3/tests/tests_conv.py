import os
import pytest
import sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if path not in sys.path:
    sys.path.insert(0, path)
    
from numsystems.math import *


def test_convert_decimal_to_binary():
    assert convert("10", 10, 2) == "1010"

def test_convert_decimal_to_hex():
    assert convert("255", 10, 16) == "FF"

def test_convert_binary_to_decimal():
    assert convert("1010", 2, 10) == "10"

def test_convert_hex_to_decimal():
    assert convert("FF", 16, 10) == "255"

def test_convert_custom_base_to_decimal():
    assert convert("ABC", 36, 10) == "13368"

def test_convert_decimal_to_custom_base():
    assert convert("13368", 10, 36) == "ABC"
    
def test_convert_negative_small():
    assert convert("-101", 2, 10) == "-5"

def test_convert_negative_big():
    assert convert("-ZZZZZ", 36, 10) == "-60466175"
    
def test_conversion_invalid_base():
    with pytest.raises(BaseError):
        convert("1010", 2, 70)

def test_conversion_invalid_symbol_in_number():
    with pytest.raises(ConversionError):
        convert("10Z", 10, 2)

def test_conversion_invalid_character_for_base():
    with pytest.raises(ConversionError):
        convert("ABC", 10, 16)

def test_conversion_from_base_to_decimal_with_invalid_character():
    with pytest.raises(ConversionError):
        convert("2", 2, 10)

def test_convert_large_decimal_to_binary():
    large_number = 10 ** 100
    result = convert(str(large_number), 10, 2)
    assert len(result) > 300

def test_convert_large_number_to_other_base():
    large_number = 10 ** 100
    result = convert(str(large_number), 10, 36)
    assert len(result) > 60

def test_convert_zero():
    assert convert("0", 10, 2) == "0"

def test_convert_one():
    assert convert("1", 10, 2) == "1"

def test_convert_large_number_from_high_base():
    assert convert("ZZZZZ", 36, 10) == "60466175"