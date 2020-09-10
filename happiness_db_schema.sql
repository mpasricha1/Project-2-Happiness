DROP TABLE IF EXISTS Alcohol;
DROP TABLE IF EXISTS Marijuana;
DROP TABLE IF EXISTS Happiness;
DROP TABLE IF EXISTS Fitness;
DROP TABLE IF EXISTS Sports;
DROP TABLE IF EXISTS HealthCare;
DROP TABLE IF EXISTS WorkHours;
DROP TABLE IF EXISTS Coordinates;
DROP TABLE IF EXISTS CountryReference;
DROP TABLE IF EXISTS userData; 


CREATE TABLE CountryReference (
	InCountryID SERIAL PRIMARY KEY,
	countryName VARCHAR,
	region VARCHAR
);

CREATE TABLE Happiness (
	InHappinessID SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	happinessRating FLOAT,
	gdpPerCapita FLOAT,
	socialSupport FLOAT,
	healthyLifeExpectancy FLOAT,
	freedomLifeChoice FLOAT,
	generosity FLOAT,
	perceptionOfCorruption FLOAT,
	dystopiaResidual FLOAT,
	year INTEGER,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE Alcohol (
	InAlcoholID SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	alcoholPerYear FLOAT,
	alcoholPerDay FLOAT,
	beer FLOAT,
	wine FLOAT,
	spirits FLOAT,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference(InCountryID)
);

CREATE TABLE Marijuana (
	InMarijuanaID SERIAL PRIMARY KEY, 
	ExCountryID INTEGER,
	recreational VARCHAR,
	medical VARCHAR,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE Fitness (
	InFitnessId SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	healthGrade FLOAT,
	pop2020 FLOAT,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE Sports (
	InSportsId SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	sport VARCHAR,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE HealthCare (
	InHealthCareID SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	hasHealthcare BOOLEAN, 
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE WorkHours (
	InWorkID SERIAL PRIMARY KEY,
	ExCountryID INT,
	avgHours FLOAT,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
);

CREATE TABLE coordinates(
	ID SERIAL PRIMARY KEY,
	ExCountryID INTEGER,
	latitude FLOAT,
	longitude FLOAT,
	FOREIGN KEY (ExCountryID) REFERENCES CountryReference (InCountryID)
	);

CREATE Table userdata(
	id serial PRIMARY KEY, 
	firstName VARCHAR, 
	lastName VARCHAR, 
	zipcode VARCHAR, 
	email VARCHAR, 
	gender VARCHAR, 
	age INTEGER, 
	income VARCHAR, 
	favRegion VARCHAR, 
	favSport VARCHAR, 
	favAlcohol VARCHAR, 
	fitness VARCHAR, 
	marijuanaMedical VARCHAR,
	marijuanaRec VARCHAR, 
	uniHealthcare BOOLEAN, 
	hoursWorked VARCHAR,
	gdpPerCap VARCHAR, 
	SocialEnv VARCHAR, 
	lifeChoices VARCHAR, 
	generosity VARCHAR, 
	govTrust VARCHAR
)