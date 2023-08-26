from flask import Flask
from flask import render_template

app = Flask(__name__, render_template='/')

@app.route("/")
def index():
    render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)