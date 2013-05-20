from nose.tools import istest, eq_
from nose_parameterized import parameterized

from roman import roman

class RomanConverter_Test:
    @parameterized.expand([(1, 'I')])
    def test_converts(self, arabic, expected_roman):
        eq_(roman(arabic), expected_roman)

    @istest
    def converts1(self):
        eq_(roman(1), 'I')

    @istest
    def converts2(self):
        eq_(roman(2), 'II')

    @istest
    def converts6(self):
        eq_(roman(6), 'VI')
