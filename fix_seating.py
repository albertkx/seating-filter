import argparse
from remove.remove_students import remove_students
from lefty.lefty import switch_lefty
import csv

EMAIL_COLUMN = 0
NAME_COLUMN = 1
LEFTY_COLUMN = 4
RIGHTY_COLUMN = 5

parser = argparse.ArgumentParser(description="Read in filters for seating sheet.")
parser.add_argument("sheet", type=str, nargs=1, help="name of seating sheet to modify")
parser.add_argument("-r", nargs=1, dest="remove_emails", help="name of txt file containg students to remove")
parser.add_argument("-l", nargs=1, dest="lefty", help="name of txt file containing students to make lefty")

args = parser.parse_args()

sheet_rows = []
with open(args.sheet[0], "r") as sheet:
    sheet_reader = csv.reader(sheet)
    sheet_rows = [row for row in sheet_reader]

if args.remove_emails:
    sheet_rows = remove_students(sheet_rows, args.remove_emails[0])

if args.lefty:
    sheet_rows = switch_lefty(sheet_rows, args.lefty[0])
with open("output.csv", "w") as output_file:
    sheet_writer = csv.writer(output_file)
    for row in sheet_rows:
        sheet_writer.writerow(row)