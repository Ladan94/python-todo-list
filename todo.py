class ToDoList:
    def __init__(self):
        self.tasks = {}
    def add_tasks(self, description):
        self.tasks[len(self.tasks) + 1] = description
        (f"Task added: {description} (ID: {len(self.tasks)})")
    def show_tasks(self):
        if not self.tasks:
            print ("No tasks available")
            return
        print("\nYour Tasks:")
        for task_id, description in self.tasks.items():
            print(f"{task_id}. {description}") 
    def remove_task (self, task_id):
        if task_id in self.tasks:
            removed_task= self.tasks.pop(task_id)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task ID.")
def main():
    todo= ToDoList()
    while True:
            print("\n1. Add Task\n2. Show Tasks\n3. Remove Task\n4. Exit")
            choice = input("Select an option: ")
            if choice == "1":
                description= input("Enter task description:")
                todo.add_tasks(description)
            elif choice== "2": 
                todo.show_tasks()  
            elif choice== "3": 
                try:
                    task_id = int(input ("Enter task ID:"))
                    todo.remove_task(task_id) 
                except ValueError:
                    print("Please enter a valid number.")  
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
    
    if __name__ == "__main__":
        main()