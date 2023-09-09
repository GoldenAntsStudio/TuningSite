from flask import Flask, render_template
import random
app = Flask(__name__, template_folder="Temp")

facts = ['Факт1', 'Факт2', 'Факт3', 'Факт4']
randomOR = ['Orel', 'Reshka']
chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/random-facts')
def random_facts():
    return f'<h1>{random.choice(facts)}</h1> <a href="/">назад</a>'

@app.route('/random')
def random_OR():
    return f'<h1>{random.choice(randomOR)}</h1> <a href="/">назад</a>'

@app.route('/passgen')
def passgen():
    password = ''
    for i in range(10):
        password += str(random.choice(chars))

    return f'<h1>{password}</h1> <a href="/">назад</a>'


if __name__ == "__main__":
    app.run(debug=True)