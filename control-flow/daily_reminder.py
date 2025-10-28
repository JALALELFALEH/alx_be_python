task = input("Enter your task:")
task_priority = input("Priority (high, medium, low)").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()

match task_priority :
    case "high" :
        if time_bound == "yes" :
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")        
        else :
            print(f"Reminder: '{task}' is a high priority task. Please address it soon.")
    case "medium" :
        if time_bound == "yes" :
            print(f"Note: '{task}' is a medium priority task that should be completed today.")        
        else :
            print(f"Note: '{task}' is a medium priority task. Consider completing it this week.")
    case "low" :
        if time_bound == "yes" :
            print(f"Note: '{task}' is a low priority task but requires completion today.")
        else :
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")