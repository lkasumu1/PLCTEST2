# PLCTEST2

<program> -> Begin <statement_list> 
<statement_list> -> <stmt>;\
<stmt> -> <assign> | <declaration> | <expression> | <loop> |<if>\
<declaration> -> <identifier> <memory_value> \
<assignment> -> <identifier> = <memory_value>: <expression>\
<memory_value> -> 1 | 2 | 4 | 8\
<expression> -> <expression>+<term> | <expression>-<term>| <term>\
<Comparisons> -> < |<= | > | >= | == | != <Comparisons> \
<condition> -> <expression><Comparisons><expression>\
<term> -> <term>*<factor> | <term>/<factor> | <term>%<factor> \
<factor> -> <identifier>|<number> | (<expression>)\
<identifier>-> <letters><identifiers> | <letters>|_\
<letters> -> [a-z][A-Z] <letters>\
<digits> ->0|1|2|3|4|5|6|7|8|9 <digits>\
<number> -> <digit>|<digit> <number>\
<memory_value> -> 1 | 2 | 4 | 8 <memory_value> \

<bool_expr> --> <bor> { `OR` <bor> }
<bor> --> <beq> { `AND` <beq> }
<beq> --> <brel> { (`!=`|`==`) <brel> }
<brel> --> <expr> { (`<=`|`>=` | `<` | `>`) <expr> }
<expr> --> <term> { (`+`|`-`) <term> }
<term> --> <not> { (`*`|`\`|`%`) <bnot> }
<not> -> [!]<bfactor>
<factor> --> `id` | `int_lit` | `float_lit` | `bool_lit` | `(` <bexpr> `)`
}
