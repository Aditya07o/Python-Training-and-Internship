class parent:
    def __init__ (Self,a,b):
        Self.a=a
        Self.b=b
        
    def Add(Self):
        print(Self.a+Self.b)
        
class child(parent):
    pass
    
X=child(10,20)
X.Add()

 
        
        
        
        
