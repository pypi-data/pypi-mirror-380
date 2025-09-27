# numersys - Powerful numbers conversion library
# Copyright (c) 2025 Treizd
#
# This file is part of numersys.
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


class NumerSysError(Exception):
    """Base exception class for library."""
    pass

class ConversionError(NumerSysError):
    """Raised when some errors occured or might occur when convert."""
    pass

class BaseError(NumerSysError):
    """Raised when base is invalid."""
    pass