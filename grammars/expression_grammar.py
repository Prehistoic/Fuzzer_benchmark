#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gramfuzz
from gramfuzz.fields import *

class NRef(Ref):
    cat = "expression_def"

class NDef(Def):
    cat = "expression_def"

Def("expression",
    NRef("full_expr"),
cat = "expression")

NDef("full_expr", Or(
	And(NRef("expr"),"=",NRef("expr"),";"),
    And(NRef("expr"),";")
))

NDef("expr", Or(
    And(NRef("expr"),"*",NRef("expr")),
    And(NRef("expr"),"+",NRef("expr")),
    And(NRef("expr"),"(",NRef("expr"),")"),
    NRef("id")
))

NDef("id",
	Or("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
)
