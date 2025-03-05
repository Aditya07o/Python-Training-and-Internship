class car:
    Windows= 4
    Door= 4
    Color= 'Red'
    
    def horn(Self):
        print('Horn')
        print(Self.Door)
    
obj=car()
print(obj.Color)
obj.horn()
 