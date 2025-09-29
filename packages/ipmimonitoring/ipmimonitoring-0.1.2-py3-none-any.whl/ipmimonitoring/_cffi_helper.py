#! /usr/bin/python3
"""CFFI helper classes for IPMI monitoring.

This module provides helper classes and utilities for working with CFFI
bindings in the IPMI monitoring library.
"""

import cffi
from enum import Enum
from typing import Any, Dict, Optional, Union

class CffiStructWrapper:
    """Base class for wrapping CFFI structures.

    This class provides a convenient interface for working with CFFI
    structures by handling the conversion between Python and C data types.
    """

    def __init__(self, ffi: cffi.FFI, obj: Any) -> None:
        """Initialize the CFFI structure wrapper.

        Args:
            ffi: CFFI instance
            obj: CFFI object to wrap
        """
        super().__setattr__('_ffi',  ffi)
        super().__setattr__('_obj',  obj)

        # This dictionary keeps references to the CCFI objects making
        # sure that they are not garbage collected
        super().__setattr__('_refs',  {})

    def __setattr__(self, k: str, v: Any) -> None:
        """Set attribute value, handling CFFI type conversions.

        This method handles the conversion of Python values to appropriate
        CFFI-compatible types when setting attributes on wrapped structures.

        Args:
            k: Attribute name
            v: Value to set
        """

        kind = self._ffi.typeof(self._obj)
        if isinstance(v, Enum):
            v = v.value
        try:
            self._ffi.typeof(v)
            # if we get this far, v is already a cffi data structure

        except (TypeError, cffi.CDefError):
            try:
                t = self._ffi.typeof(getattr(self._obj, k))
                if t.kind == 'pointer':
                    if v is None:
                        v = self._ffi.NULL
                    else:
                        if isinstance(v, str):
                            v = v.encode('utf-8')
                        cname = t.cname
                        if cname == 'char *':
                            cname = 'char []'
                        v = self._ffi.new(cname, v)

                    self._refs[k] = v

            except TypeError:
                pass

        setattr(self._obj, k, v)

    def __getattr__(self, k: str) -> Any:
        """Get attribute value, handling CFFI type conversions.

        This method handles the conversion of CFFI values to appropriate
        Python types when getting attributes from wrapped structures.

        Args:
            k: Attribute name

        Returns:
            The attribute value converted to Python type
        """

        v = getattr(self._obj, k)
        try:
            t = self._ffi.typeof(v)
            if t.cname == 'char *' or t.cname.startswith('char['):
                v = self._ffi.string(v)

        except TypeError:
            pass

        return v

def cffi_encode_string(ffi: cffi.FFI, string: Any) -> Any:
    """Encode a string for CFFI usage.

    This function encodes a Python string into a format suitable for
    passing to CFFI functions that expect char* or char[] parameters.

    Args:
        string: The string to encode, or None

    Returns:
        A CFFI-compatible byte array or ffi.NULL if string is None
    """
    if string is None:
        return ffi.NULL

    if isinstance(string, str):
        string = string.encode('utf-8')

    return ffi.new("char[]", string)

if __name__ == '__main__':
    def test():
        import cffi
        ffi = cffi.FFI()
        ffi.cdef("""
            struct st {
               int i;
               char *char_p;
               char char_a[8];
            };
        """)

        st = ffi.new("struct st *")

        csw = CffiStructWrapper(ffi, st)
        csw.i = 3
        csw.char_p = "foo"
        csw.char_a = b"bar"
        # csw.char_a = b"xyzzyplugh"

        print(f"i {csw.i!r}")
        print(f"char_p {csw.char_p!r}")
        print(f"char_a {csw.char_a!r}")

    test()
