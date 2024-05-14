from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

@app.route('/play/')
def play_default():
    return render_template('playground.html', times=None)

@app.route('/play/<int:x>')
def play_with_param(x):
    return render_template('playground.html', times=x)

if __name__ == "__main__":
    app.run(debug=True)
