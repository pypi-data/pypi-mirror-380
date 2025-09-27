# numersys - Powerful numbers conversion library
# Copyright (c) 2025 Treizd
#
# This file is part of numersys.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


from .math import convert, chars
from . import exceptions 

__version__ = "0.0.3"
__all__ = ["convert", "chars", "exceptions"]

def __dir__():
    return ["convert", "chars", "exceptions", "__all__", "__builtins__", "__cached__", "__doc__", "__file__", "__loader__", "__name__", "__package__", "__path__", "__spec__", "__version__"]