print("Welcome to Indala College")
a=("DJ night")
b=("Sports Event")
c=("Treasure hunt")
name=input("Enter your name:")
choice=input("Enter your choice:\n1.DJ night\n2.Sports event\n3.Treasure hunt\n")
if a:
    print("Please go to Ground floor for DJ night")
elif b:
    print("Please go to Main Groung")
else:
    print("Please go to 2nd Floor")
    
print(f"Thank You for participating in these Event*{name}.\nYou have participated in{choice}* event.")
