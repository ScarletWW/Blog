class TestError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n==0:
        raise TestError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except TestError as e:
        print('TestError!')
        #raise

bar()