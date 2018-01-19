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


def test_base():
    assert fake_inliner("examples/tests/base.bas") == \
"""10 input "What is your name?";k$
20 print "Hello ";k$;"!"
"""


def test_comment():
    assert fake_inliner("examples/tests/comment.bas") == \
"""10 ' It is a comment
20 input "What is your name?";k$
30 print "Hello ";k$;"!"
"""


def test_labels():
    assert fake_inliner("examples/tests/labels.bas") == \
"""10 input "What is your name?";k$
20 print "Hello "; k$;", how do you doing?"
30 input "Again (Y/N)?";k$:if k$="N" then end
40 if k$="Y" then goto 10
50 goto 30
"""


def test_self_label():
    assert fake_inliner("examples/tests/self_label.bas") == \
"""10 i=1:print "counting... ";
20 print i;:i=i+1:goto 20
"""


def test_self_splitting():
    assert fake_inliner("examples/tests/splitting.bas") == \
"""10 input "What is your name?";k$
20 print "Hello "; k$;", how do you doing?"
"""


# vim: set fileencoding=utf-8
# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4
