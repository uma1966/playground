print("inner module")

import innerst

def f():
    print('inner f():', innerst.FOO)

_hidden = 'foo'
