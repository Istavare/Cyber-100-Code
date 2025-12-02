# Simple To-Do List Program

tasks = []

def show_menu():
    """Displays the main menu options to the user"""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Count tasks")
    print("5. Exit")

def add_task():
    """Takes user input and appends it to the list."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f'"{task}" added to your to-do list!')

def view_tasks():
    """Iterates through the list and prints items in a numbered list."""
    if len(tasks) == 0:
        print("No tasks yet! Add some first.")
    else:
        print()
        print("Your current tasks:")
        for i in range(len(tasks)):
            # Print (i + 1) so the user sees "1." instead of "0."
            print(f"{i + 1}. {tasks[i]}")

def remove_task():
    """Removes a task based on the number provided by the user."""
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    view_tasks()

    number = int(input("Enter the number of the task to remove: "))

    # Check if the user input is a valid task number.
    if number > 0 and number <= len(tasks):
        # Need to subtract 1 because Python lists start at index 0
        # If user types "1", we want to remove the task at index 0.
        removed_task = tasks.pop(number - 1)
        print(f'"{removed_task}" removed from your to-do list!')
    else:
        print("Invalid task number.")

def count_tasks():
    """Displays the number of items in a list."""
    print(f"You have {len(tasks)} tasks in total.")

def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            count_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()