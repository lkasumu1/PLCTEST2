# from _typeshed import self

class main:

  file = open("test1.py")
  
  def __init__(self, tokens:list(str)) -> None:
      self.tokens = token
      self.current = 0
      self.currentToken = tokens[self.current]
  def getNextToken():
        if self.current < len(self.tokens):
          self.current += 1
          self.currentToken = slef.tokens[self.current]
  def stmt(self):
#<stmt> -> <loop> | <switch> | <var_op> | <block> 
    if self.currentToken == 'circle' :
      self.loop()
    elif self.currentToken == 'ss':
      self.switch()
    elif self.currentToken == 'idf':
      self.var_op()
    elif self.currentToken == '{':
      self.block()
    else:
      self.error()

    def block(self):    
#<block> —> ‘{‘ <stmt> ‘;’ ‘}’
      if self.currentToken == '{':
        self.getNextToken()
        while self.currentToken == 'loop' or self.currentToken == 'switch' or self.currentToken == 'var_op' or     self.currentToken == 'block' or self.currentToken == '{':
          self.stmt()
        if self.currentToken == ';':
          self.getNextToken()
      else:
        self.error()
      if self.currentToken == '}':
        self.getNextToken()
      else:
        self.error()
        
  def loop():
#<loop> —> ‘[circle]’ <boolexpr><block>
      if self.currentToken == 'circle':
          self.getNextToken()
      if self.currentToken == '(':
          self.getNextToken()
          self.expr()
      if self.currentToken == ')':
          self.getNextToken()
          self.block()
      else:
          self.error()
      
  def ass(self):
  #<ass> —> ‘=‘ <expr> 
      if self.currentToken == 'id':
        self.getNextToken()
        if self.currentToken == '=':
          self.getNextToken()
        self.expr()
      else:
        self.error()

  def expr(self):
#<expr> —> <term> {(‘*’ | ‘/’ | ‘%’)<term>}
      self.term()
  while self.currentToken == '*' or self.currentToken == '/' or self.currentToken == '%':
      self.getNetToken()
      self.term()
      
  def term(self):
     #<term> —> <factor> {(‘+’ | ‘-’)<factor>}
    self.factor()
    while self.currentToken == '+' or self.currentToken == '-':
      self.getNextToken()
self.factor()
      
def factor(self):
# <factor> —> ‘idf’| ‘lit’ | ’(‘ <expr> ‘)’
      if self.currentToken == 'idf' or self.currentToken == 'lit':
        self.getNextToken()
      elif self.currentToken == '(':
        self.getNextToken()
        self.expr()
      if self.currentToken == ')':
        self.getNextToken
      else:
        self.error()
def error(self):
        pass
        
        
      
  