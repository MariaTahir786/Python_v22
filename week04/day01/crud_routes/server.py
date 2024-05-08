import random
from datetime import datetime
from flask import Flask, render_template, session,redirect,request

app = Flask(__name__)
app.secret_key = "my_secret_key"
#read
@app.route('/')
def home():
    if not session.get('todos'):
        session['todos'] = [{
            "id": random.randint(1, 1000000),
            "text": "Todo 1",
            "description": "Feed the cat, to dog",
            "created_at": datetime.now()
        }]
    return render_template('home.html', todos =session['todos'])

@app.route('/todo/<int:id>')
def view_todo(id):
    found_todo = [todo for todo in session['todos'] if todo['id'] == id][0]
    return render_template('view.html', todo=found_todo)
#!create
#render form
@app.route('/todo/add')
def get_add_todo_form():
    return render_template('add.html')


#import request and 
@app.route('/todo/add', methods=['POST'])
def add_todo():
    new_todo=request.form
    #we are using session becoz we do not have backend
    #to get all to dos from session session is temporary storage 
    todos= session.get('todos')
    todos.append(
        {
            "id": random.randint(1, 1000000),
            "text": new_todo['text'],
            "description": new_todo['description'],
            "created_at": datetime.now()
        }
    )
    session['todos']=todos  #save todos
    return redirect('/')  #after submitting it should go to home page

#!update
#update the information
@app.route('/todo/update/<int:id>')
def get_update_todo_form(id):
    #find to do by id
    found_todo = [todo for todo in session['todos'] 
    if todo['id'] == id][0]
    if found_todo is None:
        return "Todo Not found ,404"
    return render_template('update.html', todo=found_todo)
        
        


#!update
@app.route('/todo/update',methods=['POST'])
def update_todo():
    updated_data=request.form
    todos= session.get('todos')
#find and update specific todo
    for todo in todos:
        if todo['id']== int(updated_data['id']):
            todo['text']=updated_data['text']
            todo['description']=updated_data['description']
            break
            
    session['todos']=todos
    return redirect('/')

#code for clearing the session reset session
@app.route('/todo/reset')
def reset():
    session.clear()
    return redirect('/')

#!delete
@app.route('/todo/delete/<int:id>')
def delete_todo(id):
    #retrieve the copy of todo list
    todos=session.get('todos')
    #filter the todo with id
    found_todo = [todo for todo in todos if todo['id'] != id]
    session['todos']=found_todo
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
