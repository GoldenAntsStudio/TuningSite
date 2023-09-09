from flask import Flask, render_template
import random
app = Flask(__name__, template_folder="Temp")

facts = ['Факт1', 'Факт2', 'Факт3', 'Факт4']

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/random-facts')
def random_facts():
    return f'<h1>{random.choice(facts)}</h1> <a href="/">назад</a>'


if __name__ == "__main__":
    app.run(debug=True)