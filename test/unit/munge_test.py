from nose.tools import eq_, istest

def munge(word):
    if len(word) >= 4:
        return (word[0] +
                word[-2:0:-1] +
                word[-1])

    return word



class TextMunger_Test:

    def test(self):
        eq_(munge(u"abc"), u"abc")

    def test2(self):
        eq_(munge(u"abcd"), u"acbd")

    @istest
    def foo(self):
        eq_(munge(u"abcde"), u"adcbe")

