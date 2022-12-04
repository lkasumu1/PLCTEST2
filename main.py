import re


file = open("test2.py")

keywords = {
  'circle' : 'loop', 'ss' : 'switch statement', 'el' : 'else', 'Begin' : 'start', 'ed' : 'end', 'mem1' : 'byte1', 'mem2' : 'byte2', 'mem4' : 'byte4','mem8' : 'byte8', 'tru' : 'true','fal' : 'false','&&' : 'and','||' : 'or',
}
keywords_key = keywords.keys()
symbols = {'=' : 'Ass','+' : 'Add','-' : 'Sub','/' : 'Div','*' : 'Mul','<' : 'lst','>' : 'grt','(' : 'leftp' ,')' : 'rightp' ,';' : 'eos', '%' : 'mod','!=' : 'nte','==' : 'eq','<=' : 'lste','>=' : 'grte'}
symbols_key = symbols.keys()

data_type = {'int' : 'int_lit', 'float': 'float_lit' , 'bool' : 'bool_lit' }
data_type_key = data_type.keys()

punctuation_symbol = { ':' : 'colon', ';' : 'semi-colon', '.' : 'dot' , ',' : 'comma' }
punctuation_symbol_key = punctuation_symbol.keys()

identifier = { 'a' : 'idf', 'b' : 'idf', 'c' : 'idf' , 'd' : 'idf' , 'e' : 'idf', 'f' : 'idf',  'g' : 'idf', 
              'h' : 'idf', 'i' : 'idf', 'j' : 'idf' , 'k' : 'idf' , 'l' : 'idf' , 'm' : 'idf' , 'n' : 'idf', 'o' : 'idf', 'p' : 'idf' , 'q' : 'idf' , 'r' : 'idf' , 's' : 'idf', 't' : 'idf', 'u' : 'idf', 'v' : 'idf', 'w' : 'idf', 'x' : 'idf', 'y' : 'idf' , 'z' : 'idf', 'A' : 'idf', 'B' : 'idf', 'C' : 'idf', 'D' : 'idf', 'E' : 'idf' , 'F' : 'idf', 'G' : 'idf', 'H' : 'idf', 'I' : 'idf', 'J' : 'idf' , 'K' : 'idf' , 'L' : 'idf' , 'M' : 'idf', 'N' : 'idf', 'O' : 'idf', 'P' : 'idf', 'Q' : 'idf', 'S' : 'idf', 'T' : 'idf', 'U' : 'idf', 'V' : 'idf', 'W' : 'idf', 'X' : 'idf', 'Y' : 'idf', 'Z' : 'idf'    }
identifier_key = identifier.keys()

literals = {
  '0': 'lit','1': 'lit','2': 'lit','3': 'lit','4': 'lit','5': 'lit','6': 'lit','7': 'lit','8': 'lit','9': 'lit'
}
literals_key = literals.keys()

dataFlag = False

a=file.read()

count=0
program = a.split("\n")
for line in program:
    count = count + 1
    print("line#" , count, "\n" , line)

    tokens=line.split(' ')
    print("Tokens are " , tokens)
    print("Line#", count, "properties \n")
    for token in tokens:
        if token in symbols_key:
            print("operator is ", symbols[token])
        if token in data_type_key:
            print("datatype is", data_type[token])
        if token in punctuation_symbol_key:
            print (token, "Punctuation symbol is" , punctuation_symbol[token])
        if token in identifier_key:
            print (token, "Identifier is" , identifier[token])
        if token in literals_key:
            print (token, "Literal is" , literals[token])
        if token in keywords_key:
            print (token, "Keyword is" , keywords[token])

           
    dataFlag=False
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _") 