#-*-coding: utf-8 -*-
import pdb
#pdb.set_trace()
#import logging as lg
#lg.basicConfig(level=lg.DEBUG,format='%(asctime)s%(levelname)s:%(message)s',filename='vm.log')
from Context import Context
from FuncMetaData import FuncMetaData

(IADD,
ISUB,
IMUL,
IDIV,
LES,
IEQ,
BR,
BRT,
BRF,
ICONST,
LOAD,
GLOAD,
STORE,
GSTORE,
PRINT,
POP,
HALT,
DUMP,
DUMP_SP,
PRINTST,
DUMP_IP,
CALL,
RET,
INC,
DEC,
MOD,
ABI,
NEQ,
LEQ,
EQU,
GEQ,
ODD,
AND,
OR,
XOR,
NOT)=range(36)

TRUE=1
FALSE=0

opcodes=('IADD','ISUB','IMUL','IDIV','LES','IEQ','BR','BRT','BRF',
'ICONST','LOAD','GLOAD','STORE','GSTORE','PRINT','POP','HALT','DUMP',
'DUMP_SP','PRINTST','DUMP_IP','CALL','RET','INC','DEC','MOD','ABI','NEQ',
'LEQ','EQU','GEQ','ODD','AND','OR','XOR','NOT')
not_tabl={1:0,0:1}
class Vm:
 code=[]#сам байт код,как бы слова,но просто числа(байт-обычно до 256 инструкций)
 steck=[]#стек-стек данных-стек операций
 ip=0#указатель инструкций
 sp=-1#указатель стека
 fp=0
 trace=False
 globals_=[]
 metadata=None
 ctx=None
 
 def __init__(self,code,nglobals,metadata,trace=False):
   self.code=code
   self.globals_=[0]*nglobals
   self.steck=[0]*100
   self.metadata=metadata
   self.trace=trace
 def exec_(self,startip):
   self.ip=startip
   if self.metadata!=None:
#уподобляем определению main()
    self.ctx=Context(None,0,self.metadata[0])
   self.cpu() 
#Отображает выборка-декодирование выполнение петлю
 def cpu(self):
   opcode=-1
#sp+=1 steck[sp]=val
#Выделяем некоторое место на стеке,а затем записываем туда значение.
#Аналог push()
#---
#C++:steck[sp++](постинкремент)
#---
#val=steck[sp]=val sp-=1->val=TOP() sp-=1
#копируем верхушку стека в val и передвигаем указатель на 1
#к меньшему адресу,чтобы TOP() могли ползоваться 
#другие команды.
#Аналог pop()
#---
#C++:steck[--sp](преинкремент)
#---
   while (self.ip<len(self.code) and opcode!=HALT):
     opcode=self.code[self.ip] #fetch 
#некоторая трассировка-вывод только опкодов, без 
#аргументов
     if self.trace:
       print('%d:%s\n'%(self.ip,opcodes[opcode])) 
     if (opcode==ICONST):#switch
      self.ip+=1#exec
      self.sp+=1
      self.steck[self.sp]=self.code[self.ip] 
     elif (opcode==PRINT):
       v=self.steck[self.sp]
       self.sp-=1  
       print(v)
     elif opcode==GSTORE:#сохраняем значение с 
#верхушки стека,в глобальную память по индексу(адресу) взятого 
#как параметр инструкции
       v=self.steck[self.sp]
       #print('v',v)
       self.sp-=1
       self.ip+=1
       addr=self.code[self.ip]
       self.globals_[addr]=v 
#загружаем на верхушку стека значение из глобальной памяти
#взятого по индексу(адресу) как параметр инструкции      
     elif opcode==GLOAD:
      self.ip+=1
      addr=self.code[self.ip]
      v=self.globals_[addr]
      self.sp+=1
      self.steck[self.sp]=v 
     #выход из функции cpu() 
     elif opcode==HALT:
        return
     elif opcode==DUMP:
        print('steck:',self.steck)  
     elif opcode==DUMP_SP:
      print('steck sp:',self.sp)     
     elif opcode==BR:
        self.ip+=1
        self.ip=self.code[self.ip]
        continue
     elif opcode==BRT:
       self.ip+=1
       addr=self.code[self.ip]
       if self.steck[self.sp]==TRUE:
          self.ip=addr
          self.sp-=1 
          continue  
     elif opcode==BRF:
        self.ip+=1
        addr=self.code[self.ip]
        if self.steck[self.sp]==FALSE:
          self.ip=addr
          self.sp-=1 
          continue
     elif opcode==IADD:
       b=self.steck[self.sp]
       self.sp-=1
       a=self.steck[self.sp]
       self.sp-=1
       self.sp+=1
       self.steck[self.sp]=a+b
     elif opcode==ISUB:
       b=self.steck[self.sp]
       self.sp-=1
       a=self.steck[self.sp]
       self.sp-=1
       self.sp+=1
       self.steck[self.sp]=a-b 
     elif opcode==IMUL:
       b=self.steck[self.sp]
       self.sp-=1
       a=self.steck[self.sp]
       self.sp-=1
       self.sp+=1
       self.steck[self.sp]=a*b 
     elif opcode==IDIV:
       b=self.steck[self.sp]
       self.sp-=1
       a=self.steck[self.sp]
       self.sp-=1
       self.sp+=1
       self.steck[self.sp]=a/b  
     elif opcode==LES:
        b=self.steck[self.sp]
        self.sp-=1
        a=self.steck[self.sp]
        self.sp-=1
        if a<b:
          self.sp+=1 
          self.steck[self.sp]=TRUE#True 
        else:
          self.sp+=1
          self.steck[self.sp]=FALSE#False 
     elif opcode==PRINTST:   
        self.ip+=1
        v=self.code[self.ip]
        print(v)
     elif opcode==DUMP_IP:   
        print('ip:',self.ip)
     elif opcode==POP:
      self.sp-=1
#Загружает на верхушку стека,значение из 'локальной' карты,
#взятое по индексу-аргументу LOAD
     elif opcode==LOAD:
        self.ip+=1
        regnum=self.code[self.ip]
        self.sp+=1
        self.steck[self.sp]=self.ctx.locals_[regnum]
#'консервируем' в 'локальную' карту верхушку
#стека на индекс(адрес) как аргумент STORE        
     elif opcode==STORE:
        self.ip+=1
        regnum=self.code[self.ip]
        self.ctx.locals_[regnum]=self.steck[self.sp]
        self.sp-=1 
     elif opcode==CALL:
#ожидается все аргументы на стеке
        self.ip+=1
#индекс целевой функции
        findex=self.code[self.ip]
#сколько аргументов она положила на стек
        nargs=self.metadata[findex].nargs
#ip+1 как аргумент-это returnip,адрес возврата для данной функции,
#используется в RET
        self.ctx=Context(self.ctx,self.ip+1,self.metadata[findex])
#первый аргумент
        firstarg=self.sp-nargs+1
#копируем аргументы со стека
#в новый контекст
        for i in range(0,nargs):
           self.ctx.locals_[i]=self.steck[firstarg+i]
        self.sp-=nargs
        self.ip=self.metadata[findex].address
        continue
     elif opcode==RET:
        self.ip=self.ctx.returnip
        self.ctx=self.ctx.invokingContext
        continue
     elif opcode==INC:
       v=self.steck[self.sp]
       v+=1
       self.steck[self.sp]=v
     elif opcode==DEC: 
      v=self.steck[self.sp]
      v-=1
      self.steck[self.sp]=v
     elif opcode==MOD:
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      self.sp+=1
      self.steck[self.sp]=a%b 
     elif opcode==ABI:
      v=self.steck[self.sp]
      self.steck[self.sp]=abs(v)
     elif opcode==NEQ:#a != b ?
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      if a!=b:
       self.sp+=1 
       self.steck[self.sp]=TRUE#True 
      else:
       self.sp+=1
       self.steck[self.sp]=FALSE#False   
     elif opcode==LEQ:#a <= b ?
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      if a<=b:
       self.sp+=1 
       self.steck[self.sp]=TRUE#True 
      else:
       self.sp+=1
       self.steck[self.sp]=FALSE#False    
     elif opcode==EQU:#a == b ?
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      if a==b:
       self.sp+=1 
       self.steck[self.sp]=TRUE#True 
      else:
       self.sp+=1
       self.steck[self.sp]=FALSE#False  
     elif opcode==GEQ:#a == b ?
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      if a>=b:
       self.sp+=1 
       self.steck[self.sp]=TRUE#True 
      else:
       self.sp+=1
       self.steck[self.sp]=FALSE#False 
     elif opcode==ODD:  
      v=self.steck[self.sp]
      if v%2!=0:
        self.steck[self.sp]=TRUE
      else:
        self.steck[self.sp]=FALSE
     elif opcode==AND:
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      self.sp+=1
      self.steck[self.sp]=a and b
     elif opcode==OR:
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      self.sp+=1
      self.steck[self.sp]=a or b
     elif opcode==XOR:
      b=self.steck[self.sp]
      self.sp-=1
      a=self.steck[self.sp]
      self.sp-=1
      self.sp+=1
      self.steck[self.sp]=a ^ b
     elif opcode==NOT:
      a=self.steck[self.sp]
      self.sp-=1
      self.sp+=1
      self.steck[self.sp]=not_tabl[a]       
     else:
       raise Exception("invalid opcode:",opcodes[opcode]," at ip=",(self.ip))
      
     self.ip+=1
     
#if __name__=='__main__':
 #co=[ICONST,1,ICONST,0,XOR,DUMP,HALT]
 #vm=Vm(co,4,None,trace=True);vm.exec_(0)

