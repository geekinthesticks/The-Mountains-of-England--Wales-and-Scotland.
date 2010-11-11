#!/usr/bin/python

# Copyright (C) <2010>  <Ian Barton>.

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

import csv
import sqlite3

# This is a Nuke and Reload device. All your existing data will be
# deleted and new data loaded from the csv files.

# If you have made any changes to the data in the database, make sure
# you have backed it up before running this program.

db = sqlite3.connect("ukhillsR.db")
cur = db.cursor()

# Remove any existing data.
cur.execute("DELETE FROM Class")
cur.execute("DELETE FROM ClassLink")

cur.execute("DELETE FROM Hills")


# Now nuke the Areas table.
# You have backed up haven't you?
cur.execute("DELETE FROM Areas")

cur.execute("DELETE FROM AreaLink")
# Don't forget to call commit, or nothing happens!
db.commit()


# DictReader returns the column names as the first row.
dict_reader = csv.DictReader(open("../csv/areas_4R.csv"))
values = []

"Country","Arearef","Shortname","Areaname"

for row in dict_reader:
    values.append(row)


cur.executemany('INSERT INTO Areas ("Country","Arearef","Shortname","Areaname") VALUES (:Country, :Arearef, :Shortname, :Areaname)', values)

db.commit()

dict_reader = csv.DictReader(open("../csv/arealink_4R.csv"))
values = []

"Hillnumber","Arearef","Alt_Area"

for row in dict_reader:
    values.append(row)


cur.executemany('INSERT INTO Arealink ("Hillnumber","Arearef","Alt_Area") VALUES (:Hillnumber, :Arearef, :Alt_Area)', values)

db.commit()


dict_reader = csv.DictReader(open("../csv/class_4R.csv"))
values = []

"SortSeq","Classref","Classname"

for row in dict_reader:
    values.append(row)


cur.executemany('INSERT INTO Class ("SortSeq","Classref","Classname") VALUES (:SortSeq, :Classref, :Classname)', values)

db.commit()



dict_reader = csv.DictReader(open("../csv/classlink_4R.csv"))
values = []

"Hillnumber","Clasref"

for row in dict_reader:
    values.append(row)


cur.executemany('INSERT INTO Classlink ("Hillnumber","Classref") VALUES (:Hillnumber, :Classref)', values)

db.commit()



# DictReader returns the column names as the first row.
dict_reader = csv.DictReader(open("../csv/hills_4R.csv"))

values = []

# Each row of the csv is returned as a dictionary in the form
# fieldname : value.

# We build a list of dictionaries for appending to the database.

for row in dict_reader:
    values.append(row)


# Insert all the field values.
cur.executemany('INSERT INTO Hills ("Hillnumber","Hillname","_Section","Classification","Metres","Feet","Gridref","Gridref10","Colgridref","Colheight","Drop","Feature","Observations","Survey","Revision","Comments","Map","Map25","Xcoord","Ycoord","Latitude","Longitude") VALUES (:Hillnumber,:Hillname,:_Section,:Classification,:Metres,:Feet,:Gridref,:Gridref10,:Colgridref,:Colheight,:Drop,:Feature,:Observations,:Survey,:Revision,:Comments,:Map,:Map25,:Xcoord,:Ycoord,:Latitude,:Longitude)', values)

# Save (commit) the changes
db.commit()


# Now do the same for the Areas table.
dict_reader = csv.DictReader(open("../csv/areas_4.csv"))

values = []

"Country","Arearef","Shortname","Areaname"

for row in dict_reader:
    values.append(row)


cur.executemany('INSERT INTO Areas ("Country","Arearef","Shortname","Areaname") VALUES (:Country, :Arearef, :Shortname, :Areaname)', values)

db.commit()

# We can also close the cursor now we are done with it
cur.close()

