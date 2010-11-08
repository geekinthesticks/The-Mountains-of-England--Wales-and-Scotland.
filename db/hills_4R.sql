DROP TABLE Arealink;
CREATE TABLE Arealink
 (
	Hillnumber			Integer (2), 
	Arearef			Text (510), 
	Alt_Area			Boolean

);
-- CREATE ANY INDEXES ...

DROP TABLE Areas;
CREATE TABLE Areas
 (
	Country			Text (510), 
	Arearef			Text (510), 
	Shortname			Text (510), 
	Areaname			Text (510)

);
-- CREATE ANY INDEXES ...

DROP TABLE Class;
CREATE TABLE Class
 (
	SortSeq			Integer (2), 
	Classref			Text (510), 
	Classname			Text (510)

);
-- CREATE ANY INDEXES ...

DROP TABLE Classlink;
CREATE TABLE Classlink
 (
	Hillnumber			Integer (2), 
	Classref			Text (510)

);
-- CREATE ANY INDEXES ...

DROP TABLE Help;
CREATE TABLE Help
 (
	HelpID			Long Integer (4), 
	HelpTitle			Text (100), 
	HelpText			Memo/Hyperlink

);
-- CREATE ANY INDEXES ...

DROP TABLE Hills;
CREATE TABLE Hills
 (
	Hillnumber			Integer (2), 
	Hillname			Text (510), 
	_Section			Double (8), 
	Classification			Text (100), 
	Metres			Double (8), 
	Feet			Double (8), 
	Gridref			Text (16), 
	Gridref10			Text (28), 
	Colgridref			Text (80), 
	Colheight			Double (8), 
	Drop			Double (8), 
	Feature			Text (510), 
	Observations			Text (510), 
	Survey			Text (510), 
	Revision			DateTime (Short) (8), 
	Comments			Text (510), 
	Map			Text (30), 
	Map25			Text (40), 
	Xcoord			Long Integer (4), 
	Ycoord			Long Integer (4), 
	Latitude			Double (8), 
	Longitude			Double (8)

);
-- CREATE ANY INDEXES ...

DROP TABLE User;
CREATE TABLE User
 (
	Userkey			Long Integer (4), 
	Username			Text (100)

);
-- CREATE ANY INDEXES ...

DROP TABLE Userlog;
CREATE TABLE Userlog
 (
	Userkey			Long Integer (4), 
	Hillnumber			Double (8), 
	Climbed			DateTime (Short) (8), 
	Mydesc			Text (510)

);
-- CREATE ANY INDEXES ...



-- CREATE ANY Relationships ...

-- relationships are not supported for access
