while True:
    car_choice = int(input("Which car you are looking for.? :\n 1. bmw \n 2. bmw vintage \n"))
    
    if car_choice == 1:
        while True:
            print("1. two-Tyre \n2. four-Tyre")
            tyre_choice = int(input("Enter your tyre choice: "))
            if tyre_choice == 1:
                import task_bmw_two_tyres
                break
            elif tyre_choice == 2:
                import task_bmw_four_tyres
                break
            else:
                print("We are not having that car, sorry")
        break
    elif car_choice == 2:
        while True:
            print("1. two-Tyre \n2. four-Tyre")
            tyre_choice = int(input("Enter your tyre choice: "))
            if tyre_choice == 1:
                import task_bmw_vintage_two_tyres
                break
            elif tyre_choice == 2:
                import task_bmw_vintage_four_tyres
                break
            else:
                print("We are not having that car, sorry")
        break
    else:
        print("We are not having that car, try again.!")
        