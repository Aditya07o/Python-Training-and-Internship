print("Welcome to Indala College")
a=("DJ night")
b=("Sports Event")
c=("Treasure hunt")
name=input("Enter your name:")
choice=input("Enter your choice:\n1.DJ night\n2.Sports event\n3.Treasure hunt\n")
if a:
    print("Please go to Ground floor for DJ night")
    
    age=int(input("Enter your age"))
    
    if(age<0):
        print("Invalid Age")
    elif(age<=20):
        print("Go to Section A")
    else:
        print("Go to Section B")
        
elif b:
    print("Please go to Main Groung")
    
    age=int(input("Enter your age"))
    
    if(age<0):
        print("Invalid Age")
    elif(age<=20):
        print("Go to Section A")
    else:
        print("Go to Section B")
        
else:
    print("Please go to 2nd Floor")
    
    age=int(input("Enter your age"))
    
    if(age<0):
        print("Invalid Age")
    elif(age<=20):
        print("Go to Section A")
    else:
        print("Go to Section B")
    
print(f"Thank You for participating in these Event*{name}.\nYou have participated in{choice}* event.")
