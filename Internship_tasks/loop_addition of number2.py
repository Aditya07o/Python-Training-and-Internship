a=0

print("\n1.Start\n2.Stop")
while(1):
    choice= int(input("Enter your choice:"))
    if choice==1:
        num=int(input("Enter your number:"))
        result= a + num
        print(f"Result:{result}")
        a= result
            
            
    elif choice== 2:
        print("You have stop the addition loop")
        break
    
    else:
        print("Invalid choice. Please choose 1 or 2.")
        print("Please try again.")
        
        
        
            
    