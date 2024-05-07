import random
from datetime import datetime
from flask import Flask, render_template, session

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route('/')
def home():
    if not session.get('todos'):
        session['todos'] = [{
            "id": random.randint(1, 1000000),
            "text": "Todo 1",
            "description": "Feed the cat, to dog",
            "created_at": datetime.now()
        }]
    return render_template('home.html', todos=session['todos'])

@app.route('/todo/<int:id>')
def view_todo(id):
    found_todo = [todo for todo in session['todos'] if todo['id'] == id][0]
    return render_template('view.html', todo=found_todo)

@app.route('/todo/add')
def get_add_todo_form():
    return render_template('add.html')

@app.route('/todo/add', methods=['POST'])
def add_todo():
    # Handle adding a new todo item
    pass

if __name__ == "__main__":
    app.run(debug=True)
