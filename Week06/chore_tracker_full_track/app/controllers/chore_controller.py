from app import app
from flask import Flask, render_template, request,session,redirect, flash
from app.models.chore_model import Chores

@app.route('/chore/<int:chore_id>')
def get_chore(chore_id):
    return render_template('/chores/view_chores.html',chore=Chores.get_one_chore(chore_id))
