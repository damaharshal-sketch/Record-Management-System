# Student Record Management System

A menu-driven, console-based **Record-Management Application** built in Python, developed as **Assignment 1 (Mini Project)** for **MCA Semester I – Python Programming & Relational Database**.

## Project Description

This application allows a user to manage student records (Add, View, Search, Update, Delete) through a simple text menu in the terminal. All records are persisted to a JSON file on disk, so data is retained between program runs. The project was built to demonstrate core Python fundamentals in a single, cohesive, real-world-style application rather than as isolated exercises.

## Features

- **Add Record** – Create a new student record with auto-generated unique ID.
- **View All Records** – Display every stored record in a formatted table.
- **Search Record** – Search by exact ID or by partial/case-insensitive name.
- **Update Record** – Edit any field of an existing record; blank input keeps the current value.
- **Delete Record** – Remove a record by ID, with a confirmation prompt.
- **Persistent Storage** – Records survive program restarts via a JSON data file (`data/records.json`).
- **Input Validation** – Age, email, and phone number are validated before being accepted.
- **Robust Error Handling** – Invalid menu choices, bad input, missing/corrupted data files, and keyboard interrupts are all handled gracefully without crashing.

## Technologies / Concepts Used

| Concept | Where it's used |
|---|---|
| Data Types & Variables | Record fields (`int`, `str`), menu choices |
| Conditional Statements | Menu dispatch, input validation branches |
| Loops (`while`, `for`) | Menu loop, input re-prompting, iterating over records |
| Functions | Entire app is decomposed into single-purpose functions (`add_record`, `search_record`, etc.) |
| Exception Handling | `try` / `except` around file I/O, type conversion, and the main loop |
| File I/O | `json` module used to read/write `data/records.json` |
| Menu-driven Design | `display_menu()` + `main()` dispatch loop |
| Regular Expressions | Basic email format validation |

**Language:** Python 3 (standard library only — no third-party dependencies)

## Project Structure

```
record_management_app/
│
├── record_manager.py        # Main application source code
├── data/
│   └── records.json         # Persistent data store (auto-created on first run)
├── screenshots/
│   └── sample_run.png       # Screenshot demonstrating the working application
├── Assignment_Report.docx   # Full assignment documentation
└── README.md                # This file
```

## How to Run the Application

### Prerequisites
- Python 3.7 or later installed on your system.

### Steps
1. Clone or download this repository:
   ```bash
   git clone <your-repository-url>
   cd record_management_app
   ```
2. Run the application:
   ```bash
   python3 record_manager.py
   ```
3. Use the on-screen menu (enter a number 1–6) to add, view, search, update, or delete records.
4. Choose option **6** to exit. All changes are automatically saved to `data/records.json`.

No external packages need to be installed — the application only uses Python's standard library (`json`, `os`, `re`).

## Sample Input / Output

```
=============================================
     STUDENT RECORD MANAGEMENT SYSTEM
=============================================
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
=============================================
Enter your choice (1-6): 1

--- Add New Record ---
Enter Name: Amit Sharma
Enter Age: 21
Enter Course: MCA
Enter Email: amit.sharma@example.com
Enter Phone Number: 9876543210
[SUCCESS] Record added with ID: 1

Enter your choice (1-6): 2

--- All Student Records ---
ID   Name                Age  Course         Email                    Phone
-------------------------------------------------------------------------------------
1    Amit Sharma         21   MCA            amit.sharma@example.com  9876543210

Enter your choice (1-6): 6
Exiting application. Goodbye!
```

A full terminal screenshot demonstrating a working session (add, view, and exit) is available at [`screenshots/sample_run.png`](screenshots/sample_run.png).

## Data File

The application automatically creates `data/records.json` on first run if it does not already exist. This file stores all records as a JSON array of objects, for example:

```json
[
    {
        "id": 1,
        "name": "Amit Sharma",
        "age": 21,
        "course": "MCA",
        "email": "amit.sharma@example.com",
        "phone": "9876543210"
    }
]
```

## GitHub Repository

**Repository link:** `<add your GitHub repository URL here before submission>`

## Author

`Harshal Dama` — MCA Semester I
