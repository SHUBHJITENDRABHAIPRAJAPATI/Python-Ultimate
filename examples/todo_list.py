"""
Todo List Manager
=================
A simple todo list application to manage tasks.
"""

class TodoList:
    """A simple todo list manager."""
    
    def __init__(self):
        """Initialize empty todo list."""
        self.tasks = []
    
    def add_task(self, task):
        """Add a new task."""
        self.tasks.append({"task": task, "completed": False})
        print(f"✓ Added: {task}")
    
    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nNo tasks in your list!")
            return
        
        print("\n" + "=" * 40)
        print("Your Todo List")
        print("=" * 40)
        for idx, item in enumerate(self.tasks, 1):
            status = "✓" if item["completed"] else "○"
            print(f"{idx}. [{status}] {item['task']}")
    
    def complete_task(self, task_number):
        """Mark a task as completed."""
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"✓ Completed: {self.tasks[task_number - 1]['task']}")
        else:
            print("Invalid task number!")
    
    def delete_task(self, task_number):
        """Delete a task."""
        if 1 <= task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"✓ Deleted: {deleted_task['task']}")
        else:
            print("Invalid task number!")
    
    def clear_completed(self):
        """Remove all completed tasks."""
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if not task["completed"]]
        removed = initial_count - len(self.tasks)
        print(f"✓ Removed {removed} completed task(s)")

def main():
    """Main function to run the todo list manager."""
    todo = TodoList()
    
    print("=" * 40)
    print("Todo List Manager")
    print("=" * 40)
    
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Clear completed tasks")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        
        elif choice == '2':
            todo.view_tasks()
        
        elif choice == '3':
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to complete: "))
                todo.complete_task(task_num)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '4':
            todo.view_tasks()
            try:
                task_num = int(input("Enter task number to delete: "))
                todo.delete_task(task_num)
            except ValueError:
                print("Invalid input!")
        
        elif choice == '5':
            todo.clear_completed()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
