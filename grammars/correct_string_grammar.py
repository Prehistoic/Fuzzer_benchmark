import gramfuzz
from gramfuzz.fields import *

class NRef(Ref):
    cat = "string_ref"

class NDef(Def):
    cat = "string_def"

Def("correct_string",
	Or(And(NRef("upChar"), NRef("lowChar")), And(NRef("correct_string"), NRef("lowChar"))),
	cat = "correct_string"
)

NDef("upChar",
	Or("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
)

NDef("lowChar",
	Or("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
)