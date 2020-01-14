grammar us_phone_grammar;

phone_number  : '(' area ')' exchange '-' line ;

area : LEAD_DIGIT DIGIT DIGIT ;
exchange : LEAD_DIGIT DIGIT DIGIT ;
line : DIGIT DIGIT DIGIT DIGIT ;
LEAD_DIGIT : [2-9] ;
DIGIT : [0-9] ;
