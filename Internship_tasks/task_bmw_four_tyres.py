for a in range(20):
    for b in range(20):
        if(a==0 and (b > 3 and b < 11)) or\
            (a==1 and (b==3 or b==11)) or\
            (a==2 and (b < 3 or b > 11)) or\
            (a==3 and (b==0 or b==19)) or\
            (a==4 and (b==0 or b==19)) or\
            (a==5 and (b==0 or b < 20))or\
            (a==6 and (b==3 or b==16)) or\
            (a==6 and (b==2 or b==15)) or\
            (a==7 and (b==2 or b==15)) or\
            (a==7 and (b==3 or b==16)):                          
           print('*', end=' ')
        else:
            print(' ',end=' ')
    print() 
