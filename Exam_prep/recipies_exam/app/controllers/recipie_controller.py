from app import app
from flask import Flask, render_template, request, redirect, flash, session
from app.models.recipie_model import Recipies
from app.models.user_model import User

@app.route('/recipie/<int:recipie_id>')
def get_recipie(recipie_id):
    return render_template('/recipie/view_recipies.html', recipie=Recipies.get_one_recipie(recipie_id))

@app.route('/recipie/my')
def my_recipies():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('/recipies/my_recipies.html', user=User.get_one_by_id(session['user_id']))

@app.route('/recipie/add')
def get_add_recipie_form():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('/recipies/add_recipie.html')

@app.route('/recipie/add', methods=['POST'])
def add_recipie():
    if not 'user_id' in session:
        return redirect('/')
    Recipies.create_recipie({
        **request.form,
        'user_id': session['user_id']
    })
    flash("Recipie Added")
    return redirect('/recipie/my')

@app.route('/recipie/update/<int:recipie_id>')
def get_update_recipie_form(recipie_id):
    if not 'user_id' in session:
        return redirect('/')
    return render_template('/recipies/update_recipie.html', recipie=Recipies.get_one_recipie(recipie_id))

@app.route('/recipie/update', methods=['POST'])
def update_recipie():
    if not 'user_id' in session:
        return redirect('/')
    Recipies.update_recipie(request.form)
    flash("Recipie Updated")
    return redirect('/recipie/my')

@app.route('/recipie/delete/<int:recipie_id>')
def delete(recipie_id):
    Recipies.delete_recipie(recipie_id)
    return redirect('/recipie/my')
