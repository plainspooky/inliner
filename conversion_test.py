# tratamento de leiaute de arquivos
from Inliner import Inliner

START=10
STEP=10
LF="\n"
UPPER=False

def fake_inliner(program):
    program = Inliner.load(program)
    code = Inliner(program, START, STEP)
    return code.list(uppercase=UPPER, linefeed=LF)


def test_example():
    assert fake_inliner("examples/example.bas") == \
"""10 input "What is your name?";k$
20 print "Hello ";k$;"!"
"""

def test_comment():
    assert fake_inliner("examples/example_comment.bas") == \
"""10 ' EXAMPLE.BAS
20 input "What is your name?";k$
30 print "Hello ";k$;"!"
"""

def test_labels():
    assert fake_inliner("examples/example_labels.bas") == \
"""10 ' EXAMPLE.BAS
20 input "What is your name?";k$
30 print "Hello "; k$;", how do you doing?"
40 input "Again (Y/N)?";k$:if k$="N" then end
50 if k$="Y" then goto 20
60 goto 40
"""

def test_self_label():
    assert fake_inliner("examples/example_self_label.bas") == \
"""10 i=1:print "counting... ";
20 print i;:i=i+1:goto 20
"""

def test_self_splitting():
    assert fake_inliner("examples/example_splitting.bas") == \
"""10 ' EXAMPLE.BAS
20 input "What is your name?";k$
30 print "Hello "; k$;", how do you doing?"
"""
