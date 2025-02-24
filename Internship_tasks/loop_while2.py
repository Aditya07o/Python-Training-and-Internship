print("Welcome to Indala College")
name=input("Enter your name:")
while(1):
    a=("DJ night")
    b=("Sports Event")
    c=("Treasure hunt")
    choice=input("Enter your choice:\n1.DJ night\n2.Sports event\n3.Treasure hunt\n")
    if a==("a"):
        print("Please go to Ground floor for DJ night")
        break
    elif b==("b"):
        print("Please go to Main Groung")
        break
    elif c==("c"):
        print("Please go to 2nd Floor")
        break
    else:
        print("Incorrect Choice")
    
print(f"Thank You for participating in these Event*{name}.\nYou have participated in{choice}* event.")