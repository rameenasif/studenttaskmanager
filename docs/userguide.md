# Student Task Manager: User Guide

## Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

A menu appears. Type the number of the option you want and press Enter.

## Menu options

**1. Add task**: Type a title and press Enter. Empty titles are not accepted. A task gets an ID number automatically.

**2. Show tasks**: Lists every task. `[ ]` means pending and `[x]` means completed.

**3. Complete task**: Enter the ID of the task to mark as completed. To complete several at once, separate IDs with commas, for example `1,3`. Tasks that are already completed are skipped.

**4. Delete task**: Enter the ID of the task to delete. Letters or invalid IDs show an error message.

**0. Exit**: Closes the program.

## Example

```
Choose an option: 1
Task title: Finish Git lab
Added task #1
Choose an option: 3
Task IDs to complete (e.g. 1 or 1,3): 1
Task 1 marked as completed.
Choose an option: 2
[x] 1. Finish Git lab
```

## Good to know

- Your tasks are saved automatically in `tasks.json`, so they are still there next time you start the program.
- If you enter text where a number is expected, the program shows an error and returns to the menu.