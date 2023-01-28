from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about/")
def about():
	return render_template("about.html")

@app.route("/wiki/")
@app.route("/wiki/fico/")
def wiki_fico():
	return render_template("fico.html")


if __name__ == '__main__':
	app.run(debug=True)