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

# This program simply creates an empty database called ukhills.db
# in the current directory. If the database already exists, the program
# will exit without doing anything. This is to prevent you overwriting
# your existing database with a new empty one!

# Creates a blank database corresponding to the relational
# Access database.

import sqlite3
import os.path
import sys

if os.path.exists("ukhillsR.db"):
    print "The database ukhillsR.db already exists!"
    print "Exiting without creating a new database."
    sys.exit(2)

db = sqlite3.connect("ukhillsR.db")
curs = db.cursor()

curs.execute("""

CREATE TABLE IF NOT EXISTS Arealink
 (
	"Hillnumber"			Integer (2), 
	"Arearef"			Text (510), 
	"Alt_Area"			Boolean

);

"""
)

curs.execute("""

CREATE TABLE IF NOT EXISTS Areas
 (
	"Country"			Text (510), 
	"Arearef"			Text (510), 
	"Shortname"			Text (510), 
	"Areaname"			Text (510)

);

"""
)


curs.execute("""

CREATE TABLE IF NOT EXISTS Class
 (
	"SortSeq"			Integer (2), 
	"Classref"			Text (510), 
	"Classname"			Text (510)

);


"""
)

curs.execute("""

CREATE TABLE IF NOT EXISTS Classlink
 (
	"Hillnumber"			Integer (2), 
	"Classref"			Text (510)

);


"""
)

curs.execute("""

CREATE TABLE IF NOT EXISTS Hills
 (
	"Hillnumber"			Integer (2), 
	"Hillname"			Text (510), 
	"_Section"			Double (8), 
	"Classification"			Text (100), 
	"Metres"			Double (8), 
	"Feet"			Double (8), 
	"Gridref"			Text (16), 
	"Gridref10"			Text (28), 
	"Colgridref"			Text (80), 
	"Colheight"			Double (8), 
	"Drop"			Double (8), 
	"Feature"			Text (510), 
	"Observations"			Text (510), 
	"Survey"			Text (510), 
	"Revision"			Long Integer (4), 
	"Comments"			Text (510), 
	"Map"			Text (30), 
	"Map25"			Text (40), 
	"Xcoord"			Long Integer (4), 
	"Ycoord"			Long Integer (4), 
	"Latitude"			Double (8), 
	"Longitude"			Double (8)

);

"""
)


db.commit()
db.close()
