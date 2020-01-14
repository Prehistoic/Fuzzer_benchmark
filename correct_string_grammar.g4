  
grammar correct_string_grammar;

correct_string  : upChar lowChar | correct_string lowChar ;

upChar : ('A' .. 'Z');

lowChar : ('a' .. 'z');