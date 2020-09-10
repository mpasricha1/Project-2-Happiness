from flask import Flask, render_template, jsonify, request, redirect
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import Session
from collections import Counter 

app = Flask(__name__) 

engine = create_engine(f"postgresql+psycopg2://postgres:postgres@localhost/happiness_db")
Base = automap_base()
Base.prepare(engine,reflect=True)
CountryReference = Base.classes.countryreference
Alcohol = Base.classes.alcohol
Fitness = Base.classes.fitness 
Happiness = Base.classes.happiness 
Healthcare = Base.classes.healthcare 
Marijuana = Base.classes.marijuana
Sports = Base.classes.sports
Workhours = Base.classes.workhours
Coordinates = Base.classes.coordinates
UserData = Base.classes.userdata

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route("/linedata", methods=["GET","POST"]) 
def chorandlinedata(): 
	session = Session(engine)
	sel = [CountryReference.countryname,Happiness.happinessrating,Happiness.year]

	if request.method == "POST":
		year = request.get_json()
		data = session.query(*sel).\
					filter(CountryReference.incountryid == Happiness.excountryid).\
					filter(Happiness.year == year).all()
	else: 
		data = session.query(*sel).\
					filter(CountryReference.incountryid == Happiness.excountryid).all()

	session.close()
	return jsonify(data)

@app.route("/scatterdata", methods=["GET","POST"])
def scatterdata():
	session = Session(engine)
	sel = [CountryReference.countryname, CountryReference.region, Happiness.happinessrating,
			   Happiness.gdppercapita, Happiness.socialsupport, Happiness.healthylifeexpectancy, 
			   Happiness.freedomlifechoice, Happiness.generosity, Happiness.perceptionofcorruption, 
			   Happiness.dystopiaresidual, Happiness.year]

	if request.method == "POST":
		year = request.get_json()
		data = session.query(*sel).\
					  filter(CountryReference.incountryid == Happiness.excountryid).\
					  filter(Happiness.year == year).all()
	else: 
		data = session.query(*sel).\
					filter(CountryReference.incountryid == Happiness.excountryid).all()
	
	session.close()
	return jsonify(data)

@app.route("/survey", methods=["GET", "POST"])
def survey():
	if request.method == "POST":
		session = Session(engine)
		if request.form.get("firstname") != "":
			fname = ""
			fName = request.form.get("firstname")
			lName = "" 
			lName = request.form.get("lastname")
			zipcode = request.form.get("zipcode")
			email = request.form.get("email")
			gender = request.form.get("gender")
			age = request.form.get("age")
			income = request.form.get("income")
			region = request.form.get("region")
			sport = request.form.get("sports")

			if request.form.get("beer") != None:
				alcohol = "beer"
			elif request.form.get("wine") != None:
				alcohol = "wine"
			elif request.form.get("spirits") != None:
				alcohol = "spirits"
			elif request.form.get("dontdrink") != None:
				alcohol = "none"

			if request.form.get("fitextreme") != None:
				fit = "Extremely Important"
			elif request.form.get("fitsomewhat") != None:
				fit = "Somewhat Important"
			elif request.form.get("fitnot") != None:
				fit = "Not Very Important"

			if request.form.get("medlegal") != None:
				maryMed = "Legal"
			elif request.form.get("meddecrim") != None:
				maryMed = "Decriminalize"
			elif request.form.get("medillegal") != None:
				maryMed = "Illegal"

			if request.form.get("reclegal") != None:
				maryRec = "Legal"
			elif request.form.get("recdecrim") != None:
				maryRec = "Decriminalize"
			elif request.form.get("recillegal") != None:
				maryRec = "Illegal"

			if request.form.get("htrue") != None:
				healthcare = True
			else:
				healthcare = False

			hoursworked = request.form.get("Workhours")

			if request.form.get("gdpextreme") != None:
				gdppercapita = "Extremely Impactful"
			elif request.form.get("gdpsomewhat") != None:
				gdppercapita = "Somewhat Impactful"
			elif request.form.get("gdpnot") != None:
				gdppercapita = "Not Very Impactful"

			if request.form.get("socialextreme") != None:
				social = "Extremely Impactful"
			elif request.form.get("socialsomewhat") != None:
				social = "Somewhat Impactful"
			elif request.form.get("socialnot") != None:
				social = "Not Very Impactful"

			if request.form.get("lifeextreme") != None:
				lifechoices = "Extremely Impactful"
			elif request.form.get("lifesomewhat") != None:
				lifechoices = "Somewhat Impactful"
			elif request.form.get("lifenot") != None:
				lifechoices = "Not Very Impactful"

			if request.form.get("genextreme") != None:
				generosity = "Extremely Impactful"
			elif request.form.get("gensomewhat") != None:
				generosity = "Somewhat Impactful"
			elif request.form.get("gennot") != None:
				generosity = "Not Very Impactful"

			if request.form.get("govextreme") != None:
				govTrust  = "Extremely Impactful"
			elif request.form.get("govsomewhat") != None:
				govTrust  = "Somewhat Impactful"
			elif request.form.get("govnot") != None:
				govTrust  = "Not Very Impactful"




			newUserData = UserData(firstname=fName,lastname=lName,zipcode=zipcode, email=email, gender=gender,age=age,
								   income=income, favregion=region,favsport=sport,favalcohol=alcohol,fitness=fit, 
								   marijuanamedical=maryMed, marijuanarec=maryRec, unihealthcare=healthcare, hoursworked=hoursworked, 
								   gdppercap=gdppercapita, socialenv=social, lifechoices=lifechoices,generosity=generosity, govtrust=govTrust)
			session.add(newUserData)
			session.commit()

		session.close()
		return redirect("summary")
	return render_template("survey.html")

@app.route("/calculatescore") 
def calculatescore():
	session = Session(engine)

	countryDict = {}
	countries = session.query(CountryReference.countryname).all()
	for row in countries: 
		countryDict.update({row[0]:0})

	userData = session.query(UserData).\
					order_by(UserData.id.desc()).first()

	countryDict = calculateAlcoholScore(userData, countryDict)
	countryDict = calculateFitnessScore(userData, countryDict)
	countryDict = calculateMaryMedScore(userData, countryDict)
	countryDict = calculateMaryRecScore(userData, countryDict)
	countryDict = calculateHeathcareScore(userData, countryDict)
	countryDict = calculateGDPScore(userData, countryDict)
	countryDict = calculateSocialScore(userData, countryDict)
	countryDict = calculateLifeChoiceScore(userData, countryDict)
	countryDict = calculateGenerosityScore(userData, countryDict)
	countryDict = calculateCorruptionScore(userData, countryDict)
	countryDict = calculateSportScore(userData, countryDict)
	countryDict = calculateWorkScore(userData, countryDict)

	k = Counter(countryDict)
	topFive = k.most_common(5)

	returnList = []
	count = 1
	for row in topFive: 
		country = row[0]
		points = row[1]
		sel = [CountryReference.countryname,Coordinates.latitude, Coordinates.longitude, Happiness.gdppercapita, Happiness.socialsupport,
				Happiness.healthylifeexpectancy, Happiness.freedomlifechoice, Happiness.generosity, Happiness.perceptionofcorruption,
				 Alcohol.beer, Alcohol.wine, Alcohol.spirits, Fitness.healthgrade, Marijuana.recreational, Marijuana.medical,
				 Sports.sport, Workhours.avghours]

		data = session.query(*sel).\
					  outerjoin(Coordinates, CountryReference.incountryid == Coordinates.excountryid).\
					  outerjoin(Happiness,CountryReference.incountryid == Happiness.excountryid).\
					  outerjoin(Alcohol,CountryReference.incountryid == Alcohol.excountryid).\
					  outerjoin(Fitness,CountryReference.incountryid == Fitness.excountryid).\
					  outerjoin(Marijuana,CountryReference.incountryid == Marijuana.excountryid).\
					  outerjoin(Sports,CountryReference.incountryid == Sports.excountryid).\
					  outerjoin(Workhours,CountryReference.incountryid == Workhours.excountryid).\
					  filter(CountryReference.countryname == country).first()

		countryData = {"country":data[0], 
					  "rank": count, 
					  "latitude": data[1], 
					  "longitude": data[2], 
					  "gdp": data[3], 
					  "social": data[4], 
					  "lifeexp": data[5], 
					  "lifechoice": data[6], 
					  "generosity": data[7],
					  "corruption": data[8], 
					  "beer": data[9], 
					  "wine": data[10],
					  "spirits": data[11], 
					  "healthgrade": data[12], 
					  "marymed": data[13], 
					  "maryrec": data[14], 
					  "sports": data[15], 
					  "work": data[16], 
					  "points": points
		}
		count+=1
		returnList.append(countryData)
						
	
	session.close()
	return jsonify(returnList)

@app.route("/summary")
def summary():
	return render_template("summary.html")

def calculateAlcoholScore(userData, countryDict):
	session = Session(engine)

	if userData.favalcohol == "beer":
		countries = session.query(CountryReference.countryname, Alcohol.beer).\
						   filter(CountryReference.incountryid == Alcohol.excountryid).\
						   filter(and_(Alcohol.beer > Alcohol.wine, Alcohol.beer > Alcohol.spirits)).all()

		for row in countries: 
			if row[1] > 66: 
				score = countryDict[row[0]]
				score += 10 
				countryDict.update({row[0]:score})
			elif row[1] > 33 and row[1] < 67: 
				score = countryDict[row[0]]
				score += 5
				countryDict.update({row[0]:score})
			else: 
				score = countryDict[row[0]]
				score += 1
				countryDict.update({row[0]:score})

	elif userData.favalcohol == "wine":
		countries = session.query(CountryReference.countryname, Alcohol.wine).\
						   filter(CountryReference.incountryid == Alcohol.excountryid).\
						   filter(and_(Alcohol.wine > Alcohol.beer, Alcohol.wine > Alcohol.spirits)).all()

		for row in countries: 
			if row[1] > 66: 
				score = countryDict[row[0]]
				score += 10 
				countryDict.update({row[0]:score})
			elif row[1] > 33 and row[1] < 67: 
				score = countryDict[row[0]]
				score += 5
				countryDict.update({row[0]:score})
			else: 
				score = countryDict[row[0]]
				score += 1
				countryDict.update({row[0]:score})

	elif userData.favalcohol == "spirits":
		countries = session.query(CountryReference.countryname, Alcohol.spirits).\
						   filter(CountryReference.incountryid == Alcohol.excountryid).\
						   filter(and_(Alcohol.spirits > Alcohol.beer, Alcohol.spirits > Alcohol.wine)).all()

		for row in countries: 
			if row[1] > 66: 
				score = countryDict[row[0]]
				score += 10 
				countryDict.update({row[0]:score})
			elif row[1] > 33 and row[1] < 67:  
				score = countryDict[row[0]]
				score += 5
				countryDict.update({row[0]:score})
			else: 
				score = countryDict[row[0]]
				score += 1
				countryDict.update({row[0]:score})
	elif userData.favalcohol == "I don't drink alcohol":
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateFitnessScore(userData, countryDict): 
	session = Session(engine)

	if userData.fitness == "Extremely Important":
		countries = session.query(CountryReference.countryname, Fitness.healthgrade).\
						   filter(CountryReference.incountryid == Fitness.excountryid).\
						   filter(Fitness.healthgrade > 80).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.fitness == "Somewhat Important": 
		countries = session.query(CountryReference.countryname, Fitness.healthgrade).\
						   filter(CountryReference.incountryid == Fitness.excountryid).\
						   filter(and_(Fitness.healthgrade > 70)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.fitness == "Not Very Important": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateMaryMedScore(userData, countryDict):
	session = Session(engine)

	if userData.marijuanamedical == "Legal":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.medical == 'Legal').all()
		for row in countries: 
			score = countryDict[row[0]]
			score += 10 
			countryDict.update({row[0]:score})

	elif userData.marijuanamedical == "Illegal": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.medical == 'Illegal').all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})

	elif userData.marijuanamedical == "Decriminalize": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.medical == 'Decriminalize').all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})

	session.close() 
	return countryDict

def calculateMaryRecScore(userData, countryDict):
	session = Session(engine)

	if userData.marijuanarec == "Legal":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.recreational == 'Legal').all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})

	elif userData.marijuanarec == "Illegal": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.recreational == 'Illegal').all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})

	elif userData.marijuanarec == "Decriminalize": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Marijuana.excountryid).\
						   filter(Marijuana.recreational == 'Decriminalize').all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})

	session.close() 
	return countryDict

def calculateHeathcareScore(userData, countryDict):
	session = Session(engine)

	if userData.unihealthcare == True: 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Healthcare.excountryid).\
						   filter(Healthcare.hashealthcare == True).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})
	else: 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Healthcare.excountryid).\
						   filter(Healthcare.hashealthcare == False).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10
			countryDict.update({row[0]:score})

	return countryDict

def calculateGDPScore(userData, countryDict): 
	session = Session(engine)

	if userData.gdppercap == "Extremely Impactful":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(Happiness.gdppercapita > 1.0).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.gdppercap == "Somewhat Impactful": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(and_(Happiness.gdppercapita > 0.50, Happiness.gdppercapita < 1.0)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.gdppercap == "Not Very Impactful": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateSocialScore(userData, countryDict): 
	session = Session(engine)

	if userData.socialenv == "Extremely Impactful":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(Happiness.socialsupport > 1.0).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.socialenv == "Somewhat Impactful": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(and_(Happiness.socialsupport > 0.5)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.socialenv == "Not Very Impactful": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateLifeChoiceScore(userData, countryDict): 
	session = Session(engine)

	if userData.lifechoices == "Extremely Impactful":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(Happiness.freedomlifechoice > 0.4).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.lifechoices == "Somewhat Impactful": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(and_(Happiness.freedomlifechoice > 0.20)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.lifechoices == "Not Very Impactful": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateGenerosityScore(userData, countryDict): 
	session = Session(engine)

	if userData.generosity == "Extremely Impactful":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(Happiness.generosity > 0.3).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.generosity == "Somewhat Impactful": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(and_(Happiness.generosity > 0.2)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.generosity == "Not Very Impactful": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateCorruptionScore(userData, countryDict): 
	session = Session(engine)

	if userData.govtrust == "Extremely Impactful":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(Happiness.perceptionofcorruption > 0.1).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.govtrust == "Somewhat Impactful": 
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Happiness.excountryid).\
						   filter(Happiness.year == 2020).\
						   filter(and_(Happiness.perceptionofcorruption > 0.7)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 5
			countryDict.update({row[0]:score})

	elif userData.govtrust == "Not Very Impactful": 
		for key in countryDict:
			score = countryDict[key]
			score += 1
			countryDict.update({key:score})
	session.close()
	return countryDict

def calculateSportScore(userData, countryDict): 
	session = Session(engine)

	sport = userData.favsport

	countries = session.query(CountryReference.countryname).\
						filter(CountryReference.incountryid == Sports.excountryid).\
						filter(Sports.sport == sport).all()

	for row in countries: 
		score = countryDict[row[0]] 
		score += 10 
		countryDict.update({row[0]:score})
	session.close()
	return countryDict

def calculateWorkScore(userData, countryDict): 
	session = Session(engine)

	if userData.hoursworked == "Less than 10 Hours per Week":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Workhours.excountryid).\
						   filter(Workhours.avghours < 10).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.hoursworked == "11-20 Hours per Week":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Workhours.excountryid).\
						   filter(and_(Workhours.avghours > 10, Workhours.avghours < 20)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.hoursworked == "21-30 Hours per Week":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Workhours.excountryid).\
						   filter(and_(Workhours.avghours > 20, Workhours.avghours < 30)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.hoursworked == "31-40 Hours per Week":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Workhours.excountryid).\
						   filter(and_(Workhours.avghours > 30, Workhours.avghours < 40)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	elif userData.hoursworked == "40+ Hours per Week":
		countries = session.query(CountryReference.countryname).\
						   filter(CountryReference.incountryid == Workhours.excountryid).\
						   filter(and_(Workhours.avghours > 40)).all()
		for row in countries: 
			score = countryDict[row[0]] 
			score += 10 
			countryDict.update({row[0]:score})
	session.close()
	return countryDict



if __name__ == "__main__":
	app.run(debug=True)