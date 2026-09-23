import json
import os
import re

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "records.json")

EMAIL_PATTERN = r"^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$"


def ensure_data_file_exists():
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump([], f)
    except OSError as e:
        print(f"[ERROR] Could not initialise data storage: {e}")


def load_records():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        print("[WARNING] Data file not found. A new one will be created.")
        return []
    except json.JSONDecodeError:
        print("[ERROR] Data file is corrupted. Starting with an empty record set.")
        return []
    except OSError as e:
        print(f"[ERROR] Unable to read data file: {e}")
        return []


def save_records(records):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=4)
        return True
    except OSError as e:
        print(f"[ERROR] Unable to save records: {e}")
        return False


def get_non_empty_string(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if value == "":
                raise ValueError("Input cannot be empty.")
            return value
        except ValueError as e:
            print(f"[INVALID INPUT] {e} Please try again.")


def get_valid_age(prompt):
    while True:
        try:
            age = int(input(prompt).strip())
            if age <= 0 or age > 120:
                raise ValueError("Age must be a realistic positive number.")
            return age
        except ValueError:
            print("[INVALID INPUT] Please enter a valid whole number for age.")


def get_valid_email(prompt):
    while True:
        email = input(prompt).strip()
        if re.match(EMAIL_PATTERN, email):
            return email
        print("[INVALID INPUT] Please enter a valid email address (e.g., name@example.com).")


def get_valid_phone(prompt):
    while True:
        phone = input(prompt).strip()
        if phone.isdigit() and 7 <= len(phone) <= 15:
            return phone
        print("[INVALID INPUT] Phone number must contain 7 to 15 digits only.")


def generate_new_id(records):
    if not records:
        return 1
    return max(record["id"] for record in records) + 1


def add_record(records):
    print("\n--- Add New Record ---")
    name = get_non_empty_string("Enter Name: ")
    age = get_valid_age("Enter Age: ")
    course = get_non_empty_string("Enter Course: ")
    email = get_valid_email("Enter Email: ")
    phone = get_valid_phone("Enter Phone Number: ")

    new_record = {
        "id": generate_new_id(records),
        "name": name,
        "age": age,
        "course": course,
        "email": email,
        "phone": phone,
    }

    records.append(new_record)

    if save_records(records):
        print(f"[SUCCESS] Record added with ID: {new_record['id']}")
    else:
        print("[ERROR] Record could not be saved to file.")


def view_records(records):
    print("\n--- All Student Records ---")
    if not records:
        print("No records found.")
        return

    header = f"{'ID':<5}{'Name':<20}{'Age':<5}{'Course':<15}{'Email':<25}{'Phone':<15}"
    print(header)
    print("-" * len(header))

    for record in records:
        print(
            f"{record['id']:<5}{record['name']:<20}{record['age']:<5}"
            f"{record['course']:<15}{record['email']:<25}{record['phone']:<15}"
        )


def find_record_by_id(records, record_id):
    for record in records:
        if record["id"] == record_id:
            return record
    return None


def search_record(records):
    print("\n--- Search Record ---")
    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Enter your choice (1-2): ").strip()

    results = []

    if choice == "1":
        try:
            search_id = int(input("Enter ID to search: ").strip())
            record = find_record_by_id(records, search_id)
            if record:
                results.append(record)
        except ValueError:
            print("[INVALID INPUT] ID must be a number.")
            return
    elif choice == "2":
        keyword = input("Enter name (or part of it) to search: ").strip().lower()
        results = [r for r in records if keyword in r["name"].lower()]
    else:
        print("[INVALID CHOICE] Please select option 1 or 2.")
        return

    if results:
        print(f"\n{len(results)} record(s) found:")
        header = f"{'ID':<5}{'Name':<20}{'Age':<5}{'Course':<15}{'Email':<25}{'Phone':<15}"
        print(header)
        print("-" * len(header))
        for record in results:
            print(
                f"{record['id']:<5}{record['name']:<20}{record['age']:<5}"
                f"{record['course']:<15}{record['email']:<25}{record['phone']:<15}"
            )
    else:
        print("No matching records found.")


def update_record(records):
    print("\n--- Update Record ---")
    try:
        record_id = int(input("Enter ID of record to update: ").strip())
    except ValueError:
        print("[INVALID INPUT] ID must be a number.")
        return

    record = find_record_by_id(records, record_id)
    if not record:
        print(f"[NOT FOUND] No record exists with ID {record_id}.")
        return

    print("Leave a field blank to keep its current value.")

    new_name = input(f"Name [{record['name']}]: ").strip()
    if new_name:
        record["name"] = new_name

    new_age = input(f"Age [{record['age']}]: ").strip()
    if new_age:
        try:
            age_val = int(new_age)
            if age_val <= 0 or age_val > 120:
                raise ValueError
            record["age"] = age_val
        except ValueError:
            print("[INVALID INPUT] Age unchanged (must be a valid whole number).")

    new_course = input(f"Course [{record['course']}]: ").strip()
    if new_course:
        record["course"] = new_course

    new_email = input(f"Email [{record['email']}]: ").strip()
    if new_email:
        if re.match(EMAIL_PATTERN, new_email):
            record["email"] = new_email
        else:
            print("[INVALID INPUT] Email unchanged (invalid format).")

    new_phone = input(f"Phone [{record['phone']}]: ").strip()
    if new_phone:
        if new_phone.isdigit() and 7 <= len(new_phone) <= 15:
            record["phone"] = new_phone
        else:
            print("[INVALID INPUT] Phone unchanged (must be 7-15 digits).")

    if save_records(records):
        print(f"[SUCCESS] Record with ID {record_id} updated.")
    else:
        print("[ERROR] Record could not be saved to file.")


def delete_record(records):
    print("\n--- Delete Record ---")
    try:
        record_id = int(input("Enter ID of record to delete: ").strip())
    except ValueError:
        print("[INVALID INPUT] ID must be a number.")
        return

    record = find_record_by_id(records, record_id)
    if not record:
        print(f"[NOT FOUND] No record exists with ID {record_id}.")
        return

    confirm = input(f"Are you sure you want to delete '{record['name']}' (ID {record_id})? (y/n): ").strip().lower()
    if confirm == "y":
        records.remove(record)
        if save_records(records):
            print(f"[SUCCESS] Record with ID {record_id} deleted.")
        else:
            print("[ERROR] Record could not be saved to file.")
    else:
        print("Deletion cancelled.")


def display_menu():
    print("\n" + "=" * 45)
    print("     STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("=" * 45)


def main():
    ensure_data_file_exists()
    records = load_records()

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                add_record(records)
            elif choice == "2":
                view_records(records)
            elif choice == "3":
                search_record(records)
            elif choice == "4":
                update_record(records)
            elif choice == "5":
                delete_record(records)
            elif choice == "6":
                print("Exiting application. Goodbye!")
                break
            else:
                print("[INVALID CHOICE] Please enter a number between 1 and 6.")

        except KeyboardInterrupt:
            print("\n[INTERRUPTED] Program terminated by user.")
            break
        except Exception as e:
            print(f"[UNEXPECTED ERROR] {e}")


if __name__ == "__main__":
    main()
