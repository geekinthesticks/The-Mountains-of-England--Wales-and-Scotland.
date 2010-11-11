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

import sqlite3
import os.path
import sys

if os.path.exists("ukhills.db"):
    print "The database ukhills.db already exists!"
    print "Exiting without creating a new database."
    sys.exit(2)

db = sqlite3.connect("ukhills.db")
curs = db.cursor()

curs.execute("""


CREATE TABLE IF NOT EXISTS Areas
 (
	Country			varchar (510), 
	Arearef			varchar (510), 
	Shortname			varchar (510), 
	Areaname			varchar (510)

);




"""
)

curs.execute("""
CREATE TABLE IF NOT EXISTS Hills
 (
	Hillnumber			bigint (8), 
	_Section			float (8), 
	Hillname			varchar (510), 
	Section			varchar (510), 
	Region			varchar (510), 
	Area			varchar (510), 
	Metres			float (8), 
	Feet			float (8), 
	Map			varchar (510), 
	Map25			varchar (510), 
	Gridref			varchar (510), 
	Colgridref			varchar (510), 
	Colheight			float (8), 
	"Drop"			float (8), 
	Gridref10			varchar (510), 
	Feature			varchar (510), 
	Observations			varchar (510), 
	Survey			varchar (510), 
	Climbed			date (8), 
	Classification			varchar (510), 
	Countyname			varchar (510), 
	Revision			date (8), 
	Comments			varchar (510), 
	xcoord			float (8), 
	ycoord			float (8), 
	Latitude			float (8), 
	Longitude			float (8), 
	Streetmap			text, 
	Getamap			text, 
	Ma			char, 
	sMa			char, 
	xMa			char, 
	twinMa			char, 
	xsMa			char, 
	M			char, 
	MT			char, 
	xMT			char, 
	C			char, 
	CTM			char, 
	CTC			char, 
	xC			char, 
	xCT			char, 
	G			char, 
	GTM			char, 
	GTC			char, 
	GTG			char, 
	sG			char, 
	D			char, 
	DT			char, 
	xDT			char, 
	Mur			char, 
	sMur			char, 
	Hew			char, 
	sHew			char, 
	N			char, 
	xN			char, 
	W			char, 
	WO			char, 
	BL			char, 
	Dewey			char, 
	x5			char, 
	B			char, 
	Hu			char, 
	xHu			char, 
	twinHu			char, 
	Bg			char, 
	T100			char, 
	COH			char, 
	COA			char, 
	COU			char, 
	CoL			char

);
"""
)

db.commit()
db.close()
