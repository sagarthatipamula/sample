def sss(tsr):
    def srt():
        a=10
        b=20
        tsr()
        print(a+b)
    return srt
@sss
def rrr():
    x=10.
    y=20
    print(x+y)
rrr()