from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard_8x8():
    return render_template('checker_board.html', rows=8, columns=8)

@app.route('/<int:x>')
def checkerboard_custom_rows(x):
    return render_template('checker_board.html', rows=x, columns=8)

@app.route('/<int:x>/<int:y>')
def checkerboard_custom_dimensions(x, y):
    return render_template('checker_board.html', rows=x, columns=y)

if __name__ == "__main__":
    app.run(debug=True)

