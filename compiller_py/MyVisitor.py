from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser
import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
import io
#(IADD,
#ISUB,
#IMUL,
#IDIV,
#LES,
#IEQ,
#BR,
#BRT,
#BRF,
#ICONST,
#LOAD,
#GLOAD,
#STORE,
#GSTORE,
#PRINT,
#POP,
#HALT,
#DUMP,
#DUMP_SP,
#PRINTST,
#DUMP_IP,
#CALL,
#RET,
#INC,
#DEC,
#MOD,
#ABI,
#NEQ,
#LEQ,
#EQU,
#GEQ,
#ODD,
#AND,
#OR,
#XOR,
#NOT,
#RETURN)=range(37)
(
noop,
iconst,
bipush,
iadd,
isub,
imul,
idiv,
print_,
call,
ret,
stop, 
ilt,
ieq,
br,
brt,
brf,
gload,
load,
gstore,
store,
pop 
)=range(21)

TRUE=1
FALSE=0

def conv_to_byte(int_,num_bytes=1):
    return int_.to_bytes(num_bytes,byteorder='little')

class MyVisitor(LabeledExprVisitor):
    def __init__(self):
        self.code=[]
        self.karta_lables={}
        self.startip=0
        self.b=[]
        

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        self.b.append(conv_to_byte(bipush,1))
        i=int(ctx.INT().getText())
        self.b.append(conv_to_byte(i,num_bytes=2))
       

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        if ctx.op.type==LabeledExprParser.MUL:
            self.b.append(conv_to_byte(imul))
        elif ctx.op.type==LabeledExprParser.DIV:
            self.b.append(conv_to_byte(idiv))       

    def visitAddSub(self, ctx):
        self.visit(ctx.expr(0))
        self.visit(ctx.expr(1))
        if ctx.op.type==LabeledExprParser.ADD:
            self.b.append(conv_to_byte(iadd))
        elif ctx.op.type==LabeledExprParser.SUB:
            self.b.append(conv_to_byte(isub))
    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitToTochka(self,ctx):
        self.b.append(conv_to_byte(stop))
        
    def visitToPrint(self,ctx):
        self.visit(ctx.expr())
        self.b.append(conv_to_byte(print_))
        
    def visitToDef(self,ctx):
        label=ctx.NAME().getText()
        ind=len(self.code)
        if label=='main':
            self.startip=ind
            
        print('label',label)
        self.karta_lables[label]=ind 
        self.visitToEndFunc(ctx)
        
    def visitToEndFunc(self,ctx):
       self.code.append(ret)
       
    def __str__(self):
        return 'karta_lables:'+str(self.karta_lables)+\
    ' b_code:'+str(self.code)+\
    ' startip:'+str(self.startip)
               
        
if __name__=='__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1],'r') as f:
          str_=f.read()
        
    
    input_stream = InputStream(str_)

    lexer = LabeledExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(token_stream)
    tree = parser.init()

    visitor = MyVisitor()
    visitor.visit(tree)
    
    print(visitor)
    f=open('code.txt','wb')
    #f.write(visitor.b)
    for i in visitor.b:
        f.write(i)
    f.close()