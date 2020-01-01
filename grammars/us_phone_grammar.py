import gramfuzz
from gramfuzz.fields import *

class NRef(Ref):
    cat = "phone_def"

class NDef(Def):
    cat = "phone_def"

Def("phone_number",
    And("(", NRef("area"), ")", NRef("exchange"), "-", NRef("line")),
    cat = "phone_number"
)

NDef("area",
    And(NRef("lead_digit"), NRef("digit"), NRef("digit"))
)

NDef("exchange",
    And(NRef("lead_digit"), NRef("digit"), NRef("digit"))
)

NDef("line",
    And(NRef("digit"), NRef("digit"), NRef("digit"), NRef("digit"))
)

NDef("lead_digit",
    Or("2", "3", "4", "5", "6", "7", "8", "9")
)

NDef("digit",
    Or("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
)
