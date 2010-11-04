DROP TABLE Areas;
CREATE TABLE Areas
 (
	Country			varchar (510), 
	Arearef			varchar (510), 
	Shortname			varchar (510), 
	Areaname			varchar (510)

);
-- CREATE ANY INDEXES ...

DROP TABLE Hills;
CREATE TABLE Hills
 (
	Hillnumber			float (8), 
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
	Drop			float (8), 
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
-- CREATE ANY INDEXES ...



-- CREATE ANY Relationships ...

-- relationships are not supported for mysql
