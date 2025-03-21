events = {
    "DJ Night": [],
    "Dance": [],
    "Singing": [],
    "Sports": []
}

title = "Welcome to Annual Gathering by Indala Group Of Institution"
print(title.center(100))
print("-"*150)

sub_title = "Join and Enjoy the exciting events with us !!"
print(sub_title.center(50))
print("-"*100)



while True:
    print("\n1.View Events\n2.Register for an event\n3.Participants in Event\n4.Exit")
    event_choice = int(input("Enter your choice: "))
    if(event_choice == 1):
        
        print("\n1.DJ Night\n2.Dance\n3.Singing\n4.Sports")
        break
    
    elif(event_choice == 2):
        
        while True:
            name = input("Enter your name: ")
            stu_class = input("Enter your class: ")
            print("Select an Event you want to Participate: ")
            events_list = list(events.keys())  #dict is converted into list with only key values 
            for i, event in enumerate(events_list, 1):  #enumerate is used to set counter to each item in list. It is used while looping
                print(f"{i}. {event}")
                
            
            try:
                regi_event = int(input("Enter event number: "))
                event_name = events_list[regi_event - 1]  #event_name = event_list[event_choice - 1] retrieves the event from event_list.Subtracting 1 is necessary because lists are zero-indexed
                events[event_name].append((name, stu_class))
                print(f"{name} successfully registered in {event_name}")
                break
                
            except(IndexError, ValueError):  #Checks if the input is a valid index and if the input is an integer
                print("You have selected invalid event to participate!")
                print("Please try again !!")
            
    elif(event_choice == 3):
        print("Participants in Events: ")
        for event, participants in events.items(): #for event, participants means we are using event and participants as variables to print the values of keys and values in dictionary ie participants in events
            print(f"\n{event} - Total: {len(participants)}") #len () is used to get the number of items in an object
            for name, stu_class in participants:
                print(f"- {name}: Class({stu_class})")
        
    
    elif(event_choice == 4):
        print("Thank you for participating! Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again !!")