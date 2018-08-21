# Generated from LabeledExpr.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3")
        buf.write("\f\6\fC\n\f\r\f\16\fD\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\21\6\21P\n\21\r\21\16\21Q\3\22\6\22U\n\22\r\22")
        buf.write("\16\22V\3\23\6\23Z\n\23\r\23\16\23[\3\23\3\23\2\2\24\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\3\2\6\3\2c|\4\2C\\c|\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\2b\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2")
        buf.write("\2\2\7+\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2\r\65\3\2\2")
        buf.write("\2\179\3\2\2\2\21;\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27")
        buf.write("B\3\2\2\2\31F\3\2\2\2\33H\3\2\2\2\35J\3\2\2\2\37L\3\2")
        buf.write("\2\2!O\3\2\2\2#T\3\2\2\2%Y\3\2\2\2\'(\7=\2\2(\4\3\2\2")
        buf.write("\2)*\7?\2\2*\6\3\2\2\2+,\7r\2\2,-\7t\2\2-.\7k\2\2./\7")
        buf.write("p\2\2/\60\7v\2\2\60\b\3\2\2\2\61\62\7*\2\2\62\n\3\2\2")
        buf.write("\2\63\64\7+\2\2\64\f\3\2\2\2\65\66\7f\2\2\66\67\7g\2\2")
        buf.write("\678\7h\2\28\16\3\2\2\29:\7<\2\2:\20\3\2\2\2;<\7]\2\2")
        buf.write("<\22\3\2\2\2=>\7_\2\2>\24\3\2\2\2?@\7\60\2\2@\26\3\2\2")
        buf.write("\2AC\t\2\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E")
        buf.write("\30\3\2\2\2FG\7,\2\2G\32\3\2\2\2HI\7\61\2\2I\34\3\2\2")
        buf.write("\2JK\7-\2\2K\36\3\2\2\2LM\7/\2\2M \3\2\2\2NP\t\3\2\2O")
        buf.write("N\3\2\2\2PQ\3\2\2\2QO\3\2\2\2QR\3\2\2\2R\"\3\2\2\2SU\t")
        buf.write("\4\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2\2VW\3\2\2\2W$\3\2\2")
        buf.write("\2XZ\t\5\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2\2")
        buf.write("\\]\3\2\2\2]^\b\23\2\2^&\3\2\2\2\7\2DQV[\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    NAME = 11
    MUL = 12
    DIV = 13
    ADD = 14
    SUB = 15
    ID = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'print'", "'('", "')'", "'def'", "':'", "'['", 
            "']'", "'.'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "NAME", "MUL", "DIV", "ADD", "SUB", "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "NAME", "MUL", "DIV", "ADD", "SUB", 
                  "ID", "INT", "WS" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


