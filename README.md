Script to filter CSV seating file of students.

Optional Args:
-r to specify txt file of emails of students to be removed from file (removes row)
-l to specify txt file of emails of students who should be designated left-handed

Usage
python3 fix_seating.py -r removals.txt -l lefties.txt sheet.csv

Writes output file as output.csv

Missing students for each filter are listed in missing.txt in each filter's specific folder.