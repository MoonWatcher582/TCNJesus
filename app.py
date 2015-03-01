from flask import Flask, render_template, request
from db_init import Rating, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#database session
engine = create_engine('sqlite:///ratings.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#app initialize
app = Flask(__name__)

#routes
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/success')
def success():
	#grab food, shirts, name
	name = request.args['hackathon']
	food = request.args['food']
	shirt = request.args['shirt']
	#see if name exists in db
	hkthn = session.query(Rating).filter(Rating.name == name).first()
	#if it is, avg food, shirts, count++
	if hkthn:
		hkthn.total += 1
		avg_food, avg_shirts = averages(hkthn, int(food), int(shirt))
		hkthn.food_average = avg_food
		hkthn.shirt_average = avg_shirts
	#else initialize with food, shirts, count = 0
	else:
		hkthn = Rating()
		hkthn.name = name
		hkthn.food_one = 0
		hkthn.food_two = 0
		hkthn.food_three = 0
		hkthn.food_four = 0
		hkthn.food_five = 0
		food_switch(hkthn, int(food))
		hkthn.food_average = int(food)
		hkthn.shirt_one = 0
		hkthn.shirt_two = 0
		hkthn.shirt_three = 0
		hkthn.shirt_four = 0
		hkthn.shirt_five = 0
		shirt_switch(hkthn, int(shirt))
		hkthn.shirt_average = int(shirt)
		hkthn.total = 1
		session.add(hkthn)
	#insert hkthn
	session.commit()
	entries = session.query(Rating).all()
	return render_template('success.html', entries=entries)

def averages(hkthn, food, shirt):
	food_switch(hkthn, food)
	shirt_switch(hkthn, shirt)
	avg_food = (hkthn.food_one + 2 * hkthn.food_two + 3 * hkthn.food_three + 4 * hkthn.food_four + 5 * hkthn.food_five) / (hkthn.total * 1.0)
	avg_shirts = (hkthn.shirt_one + 2 * hkthn.shirt_two + 3 * hkthn.shirt_three + 4 * hkthn.shirt_four + 5 * hkthn.shirt_five) / (hkthn.total * 1.0)
	return avg_food, avg_shirts

def food_switch(hkthn, food):
	if food == 1:
		hkthn.food_one += 1
	elif food == 2:
		hkthn.food_two += 1
	elif food == 3:
		hkthn.food_three += 1
	elif food == 4:
		hkthn.food_four += 1
	elif food == 5:
		hkthn.food_five += 1

def shirt_switch(hkthn, shirt):
	if shirt == 1:
		hkthn.shirt_one += 1
	elif shirt == 2:
		hkthn.shirt_two += 1
	elif shirt == 3:
		hkthn.shirt_three += 1
	elif shirt == 4:
		hkthn.shirt_four += 1
	elif shirt == 5:
		hkthn.shirt_five += 1

#boilerplate
if __name__ == '__main__':
	app.run('0.0.0.0', port=4000, debug=True)
