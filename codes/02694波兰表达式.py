def poland():
    c = express.pop(0)
    if c in '+-*/':
        return str(eval(poland() + c + poland()))
    else:
        return c

express = input().split()
print('{:.6f}'.format(float(poland())))