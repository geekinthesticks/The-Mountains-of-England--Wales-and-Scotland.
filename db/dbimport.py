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

db = sqlite3.connect("ukhills.db")
cur = db.cursor()



# Remove any existing data.
cur.execute("DELETE FROM Hills")

# Don't forget to call commit, or nothing happens!
db.commit()

# Now nuke the Areas table.
# You have backed up haven't you?
cur.execute("DELETE FROM Areas")
db.commit()

# DictReader returns the column names as the first row.
dict_reader = csv.DictReader(open("../csv/hills_4.csv"))



values = []

# Each row of the csv is returned as a dictionary in the form
# fieldname : value.

# We build a list of dictionaries for appending to the database.

for row in dict_reader:
    values.append(row)


# Insert all the field values.
cur.executemany('INSERT INTO Hills ("Hillnumber","_Section","Hillname","Section","Region","Area","Metres","Feet","Map","Map25","Gridref","Colgridref","Colheight","Drop","Gridref10","Feature","Observations","Survey","Climbed","Classification","Countyname","Revision","Comments","xcoord","ycoord","Latitude","Longitude","Streetmap","Getamap","Ma","sMa","xMa","twinMa","xsMa","M","MT","xMT","C","CTM","CTC","xC","xCT","G","GTM","GTC","GTG","sG","D","DT","xDT","Mur","sMur","Hew","sHew","N","xN","W","WO","BL","Dewey","x5","B","Hu","xHu","twinHu","Bg","T100","COH","COA","COU","CoL") VALUES (:Hillnumber,:_Section,:Hillname,:Section,:Region,:Area,:Metres,:Feet,:Map,:Map25,:Gridref,:Colgridref,:Colheight,:Drop,:Gridref10,:Feature,:Observations,:Survey,:Climbed,:Classification,:Countyname,:Revision,:Comments,:xcoord,:ycoord,:Latitude,:Longitude,:Streetmap,:Getamap,:Ma,:sMa,:xMa,:twinMa,:xsMa,:M,:MT,:xMT,:C,:CTM,:CTC,:xC,:xCT,:G,:GTM,:GTC,:GTG,:sG,:D,:DT,:xDT,:Mur,:sMur,:Hew,:sHew,:N,:xN,:W,:WO,:BL,:Dewey,:x5,:B,:Hu,:xHu,:twinHu,:Bg,:T100,:COH,:COA,:COU,:CoL)', values)


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

