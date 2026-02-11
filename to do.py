task=[]
while True:
    print("\n1. Add Task")
    print("2. View task")
    print("3. exit")
    choice=input("enter your choice")
    if choice=="1":
        task==input("enter task:")
        task.append(task)
        print("task added successfully")
    elif choice=="2":
        if not task:
            print("no tasks available")
        else:
            for i, task in enumerate(task,start=1):
                print(i, task)
    elif choice=="3":
            print("existing program")
            break
    else:
            print("invalid choice")

    


    
