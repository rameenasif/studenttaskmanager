"""Console interface for the Student Task Manager."""
import tasks

MENU = """
=== Student Task Manager ===
1. Add task
2. Show tasks
3. Complete task
4. Delete task
0. Exit
"""


def main():
    task_list = tasks.load_tasks()
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Task title: ")
            task = tasks.add_task(task_list, title)
            tasks.save_tasks(task_list)
            print(f"Added task #{task['id']}")
        elif choice == "2":
            tasks.show_tasks(task_list)
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            if tasks.complete_task(task_list, task_id):
                tasks.save_tasks(task_list)
                print("Task marked as completed.")
            else:
                print("Task not found.")
        elif choice == "4":
            task_id = int(input("Task ID to delete: "))
            if tasks.delete_task(task_list, task_id):
                tasks.save_tasks(task_list)
                print("Task deleted.")
            else:
                print("Task not found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()