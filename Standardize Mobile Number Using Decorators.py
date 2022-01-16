ef wrapper(f):
    def fun(l):
        out = []
        for tel in l:
            num = tel[-10:]
            telnum = '+91 ' + num[:5] + ' ' + num[5:]
            out.append(telnum)
        f(out)
    return fun
