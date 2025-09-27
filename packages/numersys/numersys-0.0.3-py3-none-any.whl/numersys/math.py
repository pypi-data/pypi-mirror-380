# numersys - Powerful numbers conversion library
# Copyright (c) 2025 Treizd
#
# This file is part of numersys.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


from .exceptions import ConversionError, BaseError
from functools import lru_cache

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZαβγδεζηθικλμνξοπρστυφχψω"

@lru_cache
def convert(number: str, from_base: int, to_base: int) -> str:
    """
    Converts number to other base
    
    :param number: Number
    :type number: :obj:`str`
    
    :param from_base: Base to decode from
    :type from_base: :obj:`int`
    
    :param to_base: Base to encode to
    :type to_base: :obj:`int`
    
    :return: Converted number
    :type rtype: :obj:`str`
    
    """
    
    def _end(number: int, base: int) -> str:
        """
        Converts decimal number to other base
        
        :param number: Decimal number
        :type number: :obj:`int`
        
        :param base: Base to encode to
        :type base: :obj:`int`
        
        :return: Converted number
        :type rtype: :obj:`str`
        
        """
        
        converted_number = ""
        if number != 0:
            while number > 0:
                remainder = number % base
                if remainder < len(chars):
                    converted_number = chars[remainder] + converted_number
                else:
                    raise ConversionError(f"Could not convert number to '{base}' base due to lack of symbols.")
                number //= base
        
            return converted_number
        return '0'

    def _start(number: str, from_base: int) -> int:
        """
        Converts number from base to decimal
        
        :param number: Any number
        :type number: :obj:`str`
        
        :param from_base: Base to decode from
        :type from_base: :obj:`int`
        
        :return: Converted decimal number
        :type rtype: :obj:`int`
        
        """
        
        num = 0
        number = number[::-1]
        for power, char in zip(range(len(number)), number):
            idx = chars.find(char)
            if idx == -1 or idx >= from_base:
                raise ConversionError(f"Invalid character '{char}' for base {from_base}.")
            num += idx * from_base ** power
        
        return num

    if not isinstance(number, str):
        raise ConversionError(f"Number must be 'str' type, not '{type(number)}'.")
    
    nnumber = number.upper().strip("-")
    
    if to_base > len(chars) or to_base < 0:
        raise BaseError(f"Could not convert number '{number}' to '{to_base}' due to base limitation of {len(chars)}.")
    if any(char not in chars[:from_base] for char in nnumber):
        raise ConversionError(f"Could not convert number '{number}': the base is invalid or the number contains inappropriate symbols.")
    
    return _end(_start(number, from_base), to_base) if not number.startswith("-") else "-" + _end(_start(nnumber, from_base), to_base)