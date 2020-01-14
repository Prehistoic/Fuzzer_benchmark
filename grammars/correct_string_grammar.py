#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gramfuzz
from gramfuzz.fields import *

class NRef(Ref):
    cat = "string_def"

class NDef(Def):
    cat = "string_def"

Def("correct_string",
	NRef("up_char"),
    NRef("low_char_string"),
cat = "correct_string")

NDef("low_char_string",
    Opt(NRef("low_char_string")), NRef("low_char")
)

NDef("up_char",
	Or("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
)

NDef("low_char",
	Or("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
)
