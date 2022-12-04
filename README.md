# PLCTEST2

Keyword, loop = circle 
Keyword, switch statement = ss
Keyword, else = el
Keyword, start = Begin
Keyword, end = ed
Keyword, byte1 = mem1
Keyword, byte2 = mem2
Keyword, byte4 = mem4
Keyword, byte8 = mem8
Keyword, true = tru
Keyword, false = fal
Keyword, and = &&
Keyword, or = ||

Symbols: 
Symbol, leftp = (
Symbol, rightp = )
Symbol, eos = ;
Symbol, add = +
Symbol, sub = -
Symbol, mult= *
Symbol, div = \
Symbol, mod = %
Symbol, ass = =
Symbol, nte = !=
Symbol, eq = =
Symbol, lst= <
Symbol, lste = <=
Symbol, grt = >
Symbol, grte = >=
Lit: [0-9]+
Idf = ([a-zA-Z]|_)


Ss —> ‘Begin’ <stmt>
<stmt> -> <loop> | <switch> | <var_op> | <block> 
<block> —> ‘{‘ <stmt> ‘;’ ‘}’
<switch> —> ‘[ss]’ <boolexpr> <block> [‘[el]’<block>]
<loop> —> ‘[circle]’ <boolexpr><block>
<var_op> —>’idf’(declare|<ass>)
<declare> —> ‘[mem1]’ | [mem2]’ | [mem4]’ | [mem8]’
<ass> —> ‘=‘ <expr> 
<factor> —> ‘idf’| ‘lit’ | ’(‘ <expr> ‘)’

<boolexpr> --> <bor> { `OR` <bor> }
<bor> --> <beq> { `OR` <beq> }
<beq> --> <brel> { (`!=`|`==`) <brel> }
<brel> --> <expr> { (`<=`|`>=` | `<` | `>`) <expr> }
<expr> —> <term> {(‘*’ | ‘/’ | ‘%’)<term>}
<term> --> <not> { (`+`|`-`|``) <factor> }
<not> -> [!]<bfactor>
<factor> --> `id` | `int_lit` | `float_lit` | `bool_lit` | `(` <bexpr> `)`

3. This is not a pairwise disjoint and there is no left hand recursion since I have <block> so it gets rid of recursion 
4. The same rule can’t be made twice 
