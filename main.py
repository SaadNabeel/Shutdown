def shutdown():
    
    user_input = input("Do you want to shut down the system? (yes/no): ")

    
    if user_input == "yes":
        print("System is shutting down...")
    elif user_input == "no":
        print("System is not shutting down.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


shutdown()
