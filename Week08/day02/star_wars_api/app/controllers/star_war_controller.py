from app import app
import os
from flask import Flask, render_template, request, redirect, flash, session, url_for, send_from_directory
import requests
import json
from werkzeug.utils import secure_filename

from app.models.like_model import Like

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

api_url = "https://swapi.dev/api"

@app.route('/hello')
def hello():
    return {
        "greeting_type": "welcome",
        "greeting_text": "Hello world!"
    }
    
@app.route('/')
def dashboard():
    response = requests.get(f'{api_url}/people')
    # print(response.text)
    people_response = json.loads(response.text)
    # print(people_response)
    people = people_response['results']
    # print(people)
    
    likes = Like.get_all()

    likes_data = {}
    
    for like in likes:
        if like['people_id'] not in likes_data:
            # print(like['people_id'])
            likes_data[like['people_id']] = 0
            
        likes_data[like['people_id']] += 1
    
    # print(likes_data)
    
    for index, person in enumerate(people):
        person['id'] = index + 1
        if index+1 in likes_data:
            person['likes'] = likes_data[index+1]
        else:
            person['likes'] = 0

    # for i in range(len(people)):
    #     people[i]['id'] = i + 1
    
    # return people, 200
    
    return render_template('dashboard.html', people = people)

@app.route('/people/<int:id>')
def get_person(id):
    response = requests.get(f'{api_url}/people/{id}')
    
    person = json.loads(response.text)

    likes = Like.get_likes_for_character(id)
    likes_data = {}
    print("!!!!!!!!!!!!!! ",likes)
    total_likes = 0
    for like in likes:
        if like['people_id'] not in likes_data:
            likes_data[like['people_id']] = 0
            
        total_likes += 1
        
    return render_template('people.html', person = person, total_likes=total_likes)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/image/upload')
def get_upload_form():
    return render_template('upload.html')


@app.route('/image/upload', methods=['POST'])
def upload_file():
    
    from app.models.picture_model import Picture
    
    
    if 'image' not in request.files:
        return redirect(request.url)
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        file_data = {
            "image_name": filename
        }
        Picture.upload_image(file_data)
        
        return redirect(url_for('dashboard'))
    return redirect(request.url)


@app.route('/get/images')
def get_images():
    from app.models.picture_model import Picture
    pictures = Picture.get_all_images()
    
    picture_files = [pic['image_name'] for pic in pictures]
    return render_template('pictures.html', picture_files=picture_files)

@app.route('/images/<filename>')
def send_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)