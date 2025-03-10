class Add:
    def __init__ (Self,a,b):
        Self.a=a
        Self.b=b

    def result(Self):
        print(Self.a+Self.b)
        
class Multiplication:
    def __init__ (Self,a,b):
        Self.a=a
        Self.b=b
        
    def result(Self):
        print(Self.a*Self.b)
        
X=Add(10,20)
Y=Multiplication(30,40)

X.result()
Y.result()

    