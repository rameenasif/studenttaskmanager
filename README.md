# Student Task Manager

A small Python console application for managing student tasks, developed with Git and GitHub (branches, pull requests, CI and releases).

Project status: Released (v1.0.0)

## Features

- Add tasks (empty titles are rejected)
- Show all tasks with their completed/pending status
- Mark one or several tasks as completed (for example `1,3`)
- Delete tasks by a valid task ID
- Tasks are saved automatically in a local `tasks.json` file
- Automated tests run on every push and pull request with GitHub Actions

## Setup

1. Install Python 3.8 or newer.
2. Clone the repository:

```bash
git clone https://github.com/rameenasif/studenttaskmanager.git
cd studenttaskmanager
```

No extra packages are needed.

## Usage

Start the application:

```bash
python main.py
```

Then choose an option from the menu:

```
1. Add task
2. Show tasks
3. Complete task
4. Delete task
0. Exit
```

See [docs/userguide.md](docs/userguide.md) for a short guide with examples.

## Running the tests

From the project folder, run:

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions on every push to `main` and on every pull request to `main`.

## License

This project is licensed under the MIT License.