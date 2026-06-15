import csv
import shutil

file_name = "contacts.csv"

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Export Contacts")
    print("7. Import Contacts")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")

        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, phone])

        print("Contact Saved!")

    elif choice == "2":
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print("Name:", row[0], "Phone:", row[1])
        except FileNotFoundError:
            print("No contacts found.")

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    print("Found:", row[0], "-", row[1])
                    found = True

        if not found:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to edit: ")
        rows = []

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == name:
                    new_phone = input("Enter new phone: ")
                    rows.append([name, new_phone])
                else:
                    rows.append(row)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Contact Updated!")

    elif choice == "5":
        name = input("Enter name to delete: ")
        rows = []

        with open(file_name, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != name:
                    rows.append(row)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print("Contact Deleted!")


    elif choice == "6":
        export_file = input("Enter export file name: ")
        shutil.copy(file_name, export_file)
        print("Contacts Exported!")

    elif choice == "7":
        import_file = input("Enter file name to import: ")
        shutil.copy(import_file, file_name)
        print("Contacts Imported!")

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")