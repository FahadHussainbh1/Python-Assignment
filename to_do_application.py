def display_menu():
    print("\nTo-Do List Application")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("Your to-do list is emty")
    else:
        print("Your to-do list:")
        index = 1
        for task in tasks:
            print(f"{index}.{task}")
            index +=1
def add_task(tasks):
    task = input("Enter the your task to add: ")               
    tasks.append(task)
    print("Task added successfully")

def delete_task(tasks):
    view_task(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' deleted successfully!")
        else:
            print("Invalid task number!")        
    except ValueError:
        print("Please enter a valid number!")


def to_do_app():
    tasks =[]
    while True:
        display_menu()
        choice = input("Enter your choice(1-4): ")
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Exting the application, Goodbye!")
            break
        else:
            print|("invalid Choice, Please try again.")

to_do_app()

      