print("Welcome to Indala College")
name=input("Enter your name:")
while(1):
    choice=input("Enter your choice:\n1.DJ night\n2.Sports event\n3.Treasure hunt\n")

    if (choice=="DJ night"):
        print("Please go to Ground floor for DJ night")
        break
        
    elif (choice=="Sports event"):
        print("Please go to Main Groung")
        break
            
    elif (choice=="Treasure hunt"):
        print("Please go to 2nd floor")
        break
                
    else:
        print("Incorrect choice\nPlease Enter your choice again:")
            
    
print(f"Thank You for participating in these Event*{name}.\nYou have participated in{choice}* event.")
