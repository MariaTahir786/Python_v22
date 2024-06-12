from app import app
from flask import Flask, render_template, request, redirect, flash, session
from app.models.like_model import Like

@app.route('/people/like/<int:id>')
def like_character(id):
    user_static_id=123
    response=Like.add_like(user_static_id,id)
    # return str(response),201
    return redirect('/')