from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/wiki/")
def wiki_home():
	return render_template("/wiki/home.html")

@app.route("/wiki/fico/")
def wiki_fico():
	return render_template("/wiki/fico.html")

@app.route("/wiki/students/")
def wiki_students():
	return render_template("/wiki/students.html")

@app.route("/wiki/investing/")
def wiki_investing():
	return render_template("/wiki/investing.html")

@app.route("/expenses/")
def expenses():
	return render_template("expenses.html")

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")


if __name__ == '__main__':
	app.run(debug=True)