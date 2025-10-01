import invocation_tree as ivt

def funB():
    b = -1
    b = 100
    return b

def funA():
    a = -1
    a = funB()
    a = funB()
    return a

def funX():
    x = -1
    x = funA()
    x = funA()
    return x

tree = ivt.blocking()
#tree.ignore_calls.add('funB')
tree(funX)
