from nose.tools import *
from mock import patch
import foo

class Foo_Test:
    @istest
    def foo(self):
        with patch('foo.bar') as mock:
            mock.return_value = "baz"
            eq_(foo.foo(), 'foobaz')

    @istest
    def foo2(self):
        def bar_stub(): return 'baz'
        foo.bar = bar_stub
        eq_(foo.foo(), 'foobaz')
