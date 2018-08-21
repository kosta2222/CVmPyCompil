# Generated from LabeledExpr.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("I\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4+\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\64\n")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5?\13\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\2\3\b\t\2\4\6\b\n\f\16")
        buf.write("\2\4\3\2\16\17\3\2\20\21\2I\2\20\3\2\2\2\4\24\3\2\2\2")
        buf.write("\6*\3\2\2\2\b\63\3\2\2\2\n@\3\2\2\2\fD\3\2\2\2\16F\3\2")
        buf.write("\2\2\20\21\5\4\3\2\21\22\5\16\b\2\22\3\3\2\2\2\23\25\5")
        buf.write("\6\4\2\24\23\3\2\2\2\25\26\3\2\2\2\26\24\3\2\2\2\26\27")
        buf.write("\3\2\2\2\27\5\3\2\2\2\30\31\5\b\5\2\31\32\7\3\2\2\32+")
        buf.write("\3\2\2\2\33\34\7\22\2\2\34\35\7\4\2\2\35\36\5\b\5\2\36")
        buf.write("\37\7\3\2\2\37+\3\2\2\2 !\7\5\2\2!\"\7\6\2\2\"#\5\b\5")
        buf.write("\2#$\7\7\2\2$%\7\3\2\2%+\3\2\2\2&\'\7\b\2\2\'(\7\r\2\2")
        buf.write("()\7\t\2\2)+\5\n\6\2*\30\3\2\2\2*\33\3\2\2\2* \3\2\2\2")
        buf.write("*&\3\2\2\2+\7\3\2\2\2,-\b\5\1\2-\64\7\23\2\2.\64\7\22")
        buf.write("\2\2/\60\7\6\2\2\60\61\5\b\5\2\61\62\7\7\2\2\62\64\3\2")
        buf.write("\2\2\63,\3\2\2\2\63.\3\2\2\2\63/\3\2\2\2\64=\3\2\2\2\65")
        buf.write("\66\f\7\2\2\66\67\t\2\2\2\67<\5\b\5\b89\f\6\2\29:\t\3")
        buf.write("\2\2:<\5\b\5\7;\65\3\2\2\2;8\3\2\2\2<?\3\2\2\2=;\3\2\2")
        buf.write("\2=>\3\2\2\2>\t\3\2\2\2?=\3\2\2\2@A\7\n\2\2AB\5\4\3\2")
        buf.write("BC\5\f\7\2C\13\3\2\2\2DE\7\13\2\2E\r\3\2\2\2FG\7\f\2\2")
        buf.write("G\17\3\2\2\2\7\26*\63;=")
        return buf.getvalue()


class LabeledExprParser ( Parser ):

    grammarFileName = "LabeledExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'print'", "'('", "')'", 
                     "'def'", "':'", "'['", "']'", "'.'", "<INVALID>", "'*'", 
                     "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NAME", "MUL", 
                      "DIV", "ADD", "SUB", "ID", "INT", "WS" ]

    RULE_init = 0
    RULE_prog = 1
    RULE_stat = 2
    RULE_expr = 3
    RULE_suite = 4
    RULE_end_func = 5
    RULE_tochka = 6

    ruleNames =  [ "init", "prog", "stat", "expr", "suite", "end_func", 
                   "tochka" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    NAME=11
    MUL=12
    DIV=13
    ADD=14
    SUB=15
    ID=16
    INT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(LabeledExprParser.ProgContext,0)


        def tochka(self):
            return self.getTypedRuleContext(LabeledExprParser.TochkaContext,0)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit" ):
                return visitor.visitInit(self)
            else:
                return visitor.visitChildren(self)




    def init(self):

        localctx = LabeledExprParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.prog()
            self.state = 15
            self.tochka()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.StatContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.StatContext,i)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LabeledExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.stat()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LabeledExprParser.T__2) | (1 << LabeledExprParser.T__3) | (1 << LabeledExprParser.T__5) | (1 << LabeledExprParser.ID) | (1 << LabeledExprParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ToPrintContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToPrint" ):
                return visitor.visitToPrint(self)
            else:
                return visitor.visitChildren(self)


    class ToDefContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NAME(self):
            return self.getToken(LabeledExprParser.NAME, 0)
        def suite(self):
            return self.getTypedRuleContext(LabeledExprParser.SuiteContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToDef" ):
                return visitor.visitToDef(self)
            else:
                return visitor.visitChildren(self)


    class ToExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToExpr" ):
                return visitor.visitToExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = LabeledExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = LabeledExprParser.ToExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.expr(0)
                self.state = 23
                self.match(LabeledExprParser.T__0)
                pass

            elif la_ == 2:
                localctx = LabeledExprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(LabeledExprParser.ID)
                self.state = 26
                self.match(LabeledExprParser.T__1)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.match(LabeledExprParser.T__0)
                pass

            elif la_ == 3:
                localctx = LabeledExprParser.ToPrintContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(LabeledExprParser.T__2)
                self.state = 31
                self.match(LabeledExprParser.T__3)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(LabeledExprParser.T__4)
                self.state = 34
                self.match(LabeledExprParser.T__0)
                pass

            elif la_ == 4:
                localctx = LabeledExprParser.ToDefContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(LabeledExprParser.T__5)
                self.state = 37
                self.match(LabeledExprParser.NAME)
                self.state = 38
                self.match(LabeledExprParser.T__6)
                self.state = 39
                self.suite()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LabeledExprParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LabeledExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LabeledExprParser.INT]:
                localctx = LabeledExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(LabeledExprParser.INT)
                pass
            elif token in [LabeledExprParser.ID]:
                localctx = LabeledExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(LabeledExprParser.ID)
                pass
            elif token in [LabeledExprParser.T__3]:
                localctx = LabeledExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(LabeledExprParser.T__3)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.match(LabeledExprParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LabeledExprParser.MulDivContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.MUL or _la==LabeledExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = LabeledExprParser.AddSubContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.ADD or _la==LabeledExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expr(5)
                        pass

             
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class SuiteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_suite

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ToSuiteContext(SuiteContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.SuiteContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prog(self):
            return self.getTypedRuleContext(LabeledExprParser.ProgContext,0)

        def end_func(self):
            return self.getTypedRuleContext(LabeledExprParser.End_funcContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToSuite" ):
                return visitor.visitToSuite(self)
            else:
                return visitor.visitChildren(self)



    def suite(self):

        localctx = LabeledExprParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_suite)
        try:
            localctx = LabeledExprParser.ToSuiteContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(LabeledExprParser.T__7)
            self.state = 63
            self.prog()
            self.state = 64
            self.end_func()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class End_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_end_func

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ToEndFuncContext(End_funcContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.End_funcContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToEndFunc" ):
                return visitor.visitToEndFunc(self)
            else:
                return visitor.visitChildren(self)



    def end_func(self):

        localctx = LabeledExprParser.End_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_end_func)
        try:
            localctx = LabeledExprParser.ToEndFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(LabeledExprParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TochkaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_tochka

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ToTochkaContext(TochkaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.TochkaContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToTochka" ):
                return visitor.visitToTochka(self)
            else:
                return visitor.visitChildren(self)



    def tochka(self):

        localctx = LabeledExprParser.TochkaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tochka)
        try:
            localctx = LabeledExprParser.ToTochkaContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(LabeledExprParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




