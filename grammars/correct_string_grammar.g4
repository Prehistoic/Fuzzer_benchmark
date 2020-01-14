
grammar correct_string_grammar;

correct_string : UPCHAR lower_case_string;

lower_case_string : lower_case_string LOWCHAR | LOWCHAR;

UPCHAR : [A-Z];

LOWCHAR : [a-z];
