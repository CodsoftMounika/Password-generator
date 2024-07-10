# To-Do List using a Class

class TodoList:
    def _init_(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

todo_list = TodoList()

while True:
    print("\nTo-Do List:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice(1/2/3/4): ")

    if choice == '1':
        todo_list.show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        todo_list.add_task(task)
    elif choice == '3':
        task_number = int(input("Enter task number to remove: "))
        todo_list.remove_task(task_number)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")