
from app import app
from flask import Flask, render_template, redirect, request

from app.models.todo_model import Todo

#! READ
@app.route('/')
def home():
    return render_template('home.html', todos=Todo.get_all_todos())

#! READ
@app.route('/todo/<int:id>')
def view_todo(id):
    return render_template('view.html', todo=Todo.get_one_by_id(id))

#! CREATE
# render form 
@app.route('/todo/add')
def get_add_todo_form():
    return render_template('add.html')

#! CREATE
# import request and redirect
#both routes should be same
@app.route('/todo/add', methods=['POST'])
def add_todo():
    new_todo = request.form
    Todo.create_todo(new_todo)  # always redirect when methods=POST
    return redirect('/')  

#! UPDATE
@app.route('/todo/update/<int:id>')
def get_update_todo_form(id):
    return render_template('update.html', todo=Todo.get_one_by_id(id))

#! UPDATE
@app.route('/todo/update', methods=["POST"])
def update_todo():
    form = request.form
    
    Todo.update_todo(form)

    return redirect('/')

#! DELETE
@app.route('/todo/delete/<int:id>')
def delete_todo(id):
    Todo.delete_todo(id)
    return redirect('/')
