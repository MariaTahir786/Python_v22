from app import app
from flask import Flask, render_template, request, redirect, flash, session

from app.models.sas_model import Sightings
from app.models.user_model import User


# @app.route('/chore/<int:chore_id>')
# def get_chore(chore_id):
#     return render_template('/chores/view_chores.html', chore = Chores.get_one_chore(chore_id))

# 
@app.route('/sighting/<int:sighting_id>')
def get_sighting(sighting_id):
    from app.models.sas_model import Sightings

    sighting = Sightings.get_one_sighting(sighting_id)
    user = User.get_one_by_id(session['user_id'])
    
    if not sighting:
        flash('Sighting not found', 'error')
        return redirect('/user/dashboard')
    
    return render_template('/sightings/view_sightings.html', sighting=sighting, user=user)

# 

@app.route('/sighting/my')
def my_sightings():

    if not 'user_id' in session:
        return redirect('/')

    return render_template('/sightings/my_sightings.html', user = User.get_one_by_id(session['user_id']))

@app.route('/sighting/add')
def get_add_sighting_form():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('/sightings/add_sighting.html')

@app.route('/sighting/add', methods=['POST'])
def add_sighting():
    if not 'user_id' in session:
        return redirect('/')

    # form = request.form
    # form['user_id'] = session['user_id']
    # Chore.create_chore(form)

    Sightings.create_sighting({
        **request.form,
        'user_id': session['user_id']
    })
    flash("Sighting Added")
    return redirect('/sighting/my')

@app.route('/sighting/update/<int:sighting_id>')
def get_update_sighting_form(sighting_id):
    if not 'user_id' in session:
        return redirect('/')
    return render_template('/sightings/update_sighting.html', sighting = Sightings.get_one_sighting(sighting_id))


@app.route('/sighting/update', methods=['POST'])
def update_sighting():
    if not 'user_id' in session:
        return redirect('/')

    Sightings.update_sighting(request.form)
    flash("Sighting Updated")

    return redirect('/sighting/my')

@app.route('/sighting/delete/<int:sighting_id>')
def delete(sighting_id):
        Sightings.delete_sighting(sighting_id)
        return redirect('/user/dashboard')
    
@app.route('/sighting/like/<int:sighting_id>')
def like_sighting(sighting_id):
    if not 'user_id' in session:
        return redirect('/')
    Sightings.add_saquatch(sighting_id, int(session['user_id']))
    return redirect('/user/dashboard')