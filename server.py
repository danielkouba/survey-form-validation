from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

app.secret_key = 'MomsSpaghettisOnHisSweaterAlreadyMomsSpaghetti'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/submitted')
def submit():
	# for 'name' in session:
	return render_template("submitted.html", name=session["name"],comment=session["comment"], language=session["language"], location=session["location"])

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['name']) < 1:
		flash( "WHOOPS! Name cannot be empty")
		return redirect('/')
	elif len(request.form['name']) > 120:
		flash( "WHOOPS! Name has to be less than 120 characters")
		return redirect('/')
	else:
		flash("Success! Your name is {}".format(request.form['name']))
		session["name"] = request.form["name"]
	
	if len(request.form['comment']) < 1:
		flash( "WHOOPS! Comment cannot be empty")
		return redirect('/')
	elif len(request.form['comment']) > 120:
		flash( "WHOOPS! Comment has to be less than 120 characters")
		return redirect('/')
	else:
		flash("Success! Your name is {}".format(request.form['name']))
		session["comment"] = request.form["comment"]

	session["location"] = request.form["location"]
	session["language"] = request.form["language"]
	
	return redirect('/submitted')	
	
app.run(debug=True)