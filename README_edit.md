# Project_2 M2K (formerly known as The Data Condas)
### Mark Pasrich, Melissa Hazelgreen, and Kristin Aspromonti Submitted 9/13/2020

# Background
This product was inspired from the World Happiness Report (WHR) published on March 20, 2020. This report is published annually by the United Nations Sustainable Development Solutions Network. Using the Gallop World Poll, individuals around the world are surveyed on 6 Key variables:

1. GDP per capita
2. Social Support
3. Healthy Life Expectancy
4. Freedom of Choices
5. Generosity
6. Perception of Corruption

 The scores are based on individuals’ own assessments of their lives using the Cantril Ladder (scale from 0-10), where the top represents the best possible and the bottom the worst possible life for themselves.

 ## Objective
 The objective is to create a product that will help a person       determine in which country they would be the happiest living.

 # Our Approach
  Using the WHR as our baseline for happiness, we supplemented the 6 criteria, seeking additional preferences the user may want to consider when determining their optimal living locale. Using the various resources listed below, 6 additional happiness factors are to be evaluated: 
  
  1. Fitness
  2. Alcohol Consumption
  3. Universal Healthcare
  4. Sports
  5. Legalization of Marijuana
  6. Weekly Hours Worked. 
  
  The user will complete a survey asking pertaining to the aforementioned criteria. Using an algorithm, we intend to calculate and determine which country meets their criteria and provide a visualization back to the user showing them where they would be the happiest living.

## Dependencies
* SQL/Postgres 
* Python JavaScript
* HTML/CSS
* Flask 
* SQLAlchemy Collections (new library, not covered in Class) 
* Ajax (new library, not covered in Class) 
* Pandas 
* Beautiful Soup 
* Requests 
* Plotly 
* D3 
* Bootstrap
* Leaflet 
* JQuery (new library, not covered in class)

# Creating an App

1. Data Layer
Data mined using scraping and importing of CSV files, cleaned and loaded into Postgres using SQL

2. Application: Middle Layer
* App.py 
Using Flask to “GET” and “POST” Data between Postgres and HTML
Calling in JavaScript files for data visualization 

## Algorithm
### Overview
Points assigned to each country that most meet the criteria determined by the data captured by the user’s survey 

Dictionaries are created containing the Country name an it’s accumulated points being updated with each selection from the survey 


### Alcohol Consumption - What is your favorite type of Alcohol to drink? 
* % of consumption by type by country 
* Countries with the highest %s of the preferred type (beer, wine, or spirits) that match the user’s selection = 10 pts. 
* Countries with the mid-level %s of the preferred type (beer, wine, or spirits) that match the user’s selection = 5 pts.
* All other countries = 1 pt.
 If User selects “I don’t drink alcohol” = 1 pt. to all countries  Fitness - How important is overall fitness to you? (extremely, somewhat, not)  Ranking based on Bloomberg Global Health Index  If extremely important chosen, top 1/3 % = 10 pts.  If somewhat important chosen, top 2/3 % = 5 pts.  If not important chosen, all countries = 1 pt.  Legalization of Marijuana - Choose your stance on the legalization of marijuana for MEDICINAL and RECREATIONAL purposes:  Lists the legalization status of marijuana in all countries  If selection matches the countries status = 10 pts.  Universal Healthcare - I prefer to live in a country with Universal Healthcare:  Lists the countries that subscribe to universal healthcare  If selection matches the countries status = 10 pts.  GDP per Capita - High GDP Per Capita:  GDP time series from 2018 to 2019 using country-specific forecasts of real GDP growth from the OECD Economic Outlook and the World Bank’s Global Economic Prospects  If extremely impactful chosen, top 1/3 % = 10 pts.  If somewhat impactful chosen, top 2/3 % = 5 pts.  If not impactful chosen, all countries = 1 pt.  Freedom to Make Life Choices - Freedom to make life choices (ability to do as you choose with your life):  National average of binary responses to the GWP question, “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”  If extremely impactful chosen, top 1/3 % = 10 pts.  If somewhat impactful chosen, top 2/3 % = 5 pts.  If not impactful chosen, all countries = 1 pt.  Social Support - Interactive and Supportive Social Environment:  National average of the binary responses (0=no, 1=yes) to the question, “If you were in trouble, do you have relatives or friends you can count on to help you whenever you need them, or not?”  If extremely impactful chosen, top 1/3 % = 10 pts.  If somewhat impactful chosen, top 2/3 % = 5 pts.  If not impactful chosen, all countries = 1 pt.  Generosity - Generosity (Donation/Charity work):  Generosity is the residual of regressing the national average of GWP responses to the question, “Have you donated money to a charity in the past month?” on GDP per capita. widespread within businesses or not?”  If extremely impactful chosen, top 1/3 % = 10 pts.  If somewhat impactful chosen, top 2/3 % = 5 pts.  If not impactful chosen, all countries = 1 pt.  Perception - Trust in Government (Perception of corruption in business and/or government):  Perceptions of corruption are the average of binary answers to two GWP questions: “Is corruption widespread throughout the government or not?” and “Is corruption widespread within businesses or not?”  If extremely impactful chosen, top 1/3 % = 10 pts.  If somewhat impactful chosen, top 2/3 % = 5 pts.  If not impactful chosen, all countries = 1 pt.  Sports - Choose your favorite sport from the list below:  Dataset lists each country and their most popular sport  If selection matches the countries status = 10 pts.  Hours Worked Per Week - The number of hours I'm willing to work per week:  Average number of hours worked per week by country.  If selection matches the countries status = 10 pts.

FRONT END/CLIENT Website structure designed using HTML/CSS base, index, summary and survey templates. The primary page contains interactive data creating plots of the WHR data. The user is prompted to take the survey that will return the results and map the results produced by the algorithm.

RESOURCES/DATASETS • Happiness WR: https://www.kaggle.com/mathurinache/world-happiness-report (csv) • Alcohol: https://worldpopulationreview.com/country-rankings/alcohol-consumption-by-country (csv) • Fitness: https://worldpopulationreview.com/country-rankings/healthiest-countries (csv) • Marijuana: https://en.wikipedia.org/wiki/Legality_of_cannabis (scraped) • Sports: http://chartsbin.com/view/33104 (scraped) • Workhours: https://worldpopulationreview.com/country-rankings/average-work-week-by-country (csv) • Universal Healthcare: https://en.wikipedia.org/wiki/List_of_countries_with_universal_health_care#:~:text=Countries%20with%20universal%20healthcare%20include,Turkey%2C%20Ukraine%2C%20and%20the%20United (scraped)

GitHub Repo https://github.com/kaspromonti/Data_Condas_Project_2.g