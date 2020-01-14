
grammar expression_grammar;

expression : expr '=' expr ';'
  | expr ';'
  ;

expr : expr '*' expr
  | expr '+' expr
  | expr '(' expr ')'
  | ID
  ;

ID : [a-z];
