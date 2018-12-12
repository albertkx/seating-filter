import os.path

EMAIL_COLUMN = 0
NAME_COLUMN = 1

def switch_lefty(sheet_rows, emails_file):
    emails = []
    with open(emails_file, "r") as emails_list:
        for email in emails_list:
            emails.append(email.strip('\n').lower())

    emails = list(set(emails))

    num_swapped = 0
    missing = []
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
            num_swapped += 1
            row = sheet_rows[found_indices[0]]
            row[4] = "TRUE"
            row[5] = ""
            print("Changing row", found_indices[0], "with email", email, "and name", row[NAME_COLUMN], "to lefty")
        else:
            print("Found multiple", email, "- skipping")

    print("Swapped", num_swapped, "students, now writing file.")

    with open(os.path.join("lefty", "missing.txt"), "w") as missing_students:
        for m in missing:
            missing_students.write(m + "\n")

    return sheet_rows