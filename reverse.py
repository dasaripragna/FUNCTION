def a(str):

    x = ''
    i = len(str)
    while i > 0:
        x += str[ i - 1 ]
        i = i - 1
    return x
print(a('1234abcd'))