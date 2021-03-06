import os.path

EMAIL_COLUMN = 0
NAME_COLUMN = 1
LEFTY_COLUMN = 4
RIGHTY_COLUMN = 5

def remove_students(sheet_rows, emails_file):
    emails = []
    with open(emails_file, "r") as emails_list:
        for email in emails_list:
            emails.append(email.strip('\n').lower())
    emails = list(set(emails))

    # for row_i in range(len(sheet_rows)):
    #     row = sheet_rows[row_i]
    #     name = row[1] # the number of the column which name is in
    #     parts = name.split(", ")

    num_removed = 0
    missing = []
    removed = []
    for email in emails:
        found_indices = []
        for row_i in range(len(sheet_rows)):
            row = sheet_rows[row_i]
            if row[EMAIL_COLUMN].lower() == email:
                found_indices.append(row_i)
        if len(found_indices) == 0:
            print(email, "not found, skipping.")
            missing.append(email)
        elif len(found_indices) == 1:
            num_removed += 1
            student = sheet_rows.pop(found_indices[0])
            removed.append(student[EMAIL_COLUMN])
            print("Removed row", found_indices[0], "with email", email, "and name", student[NAME_COLUMN])
        else:
            print("Found multiple", email, "- skipping")

    print("Removed", num_removed, "students, now writing file.")

    with open(os.path.join("remove", "missing.txt"), "w") as missing_students:
        for m in missing:
            missing_students.write(m + "\n")
    
    with open(os.path.join("remove", "removed.txt"), "w") as removed_students:
        for r in removed:
            removed_students.write(r + "\n")
    return sheet_rows
