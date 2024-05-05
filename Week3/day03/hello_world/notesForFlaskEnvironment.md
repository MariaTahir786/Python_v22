crud operations

these instructions are steps by step how we created server.py file
flask application
web application
1. ---- pip3 install pipenv   --in our main  terminal-->to install globally only once I have it
2. create different environment for each different projects by following command
3. open folder in integrated terminal and run this to create environment 
        ====>pipenv install flask

4. then run this ==> pipenv shell
**we can not have multiple environments at the same time 
5. **to exit environment cmnd c or exit


then in server.py 
1.  from flask import Flask
2. app= Flask(__name__)  ==create instance of flask
3.  if __name__ =="__main__":
    app.run(debug=True)
4. @app.route('/')
def hello_world():
    return "Hello World"

5. now run this file -->python3 server.py (it will open the localhost cmd+click to see your application )


next steps we did in server.py to create other routes in following order
then create another route in server.py 
# static route2 
@app.route('/success')
def success():
    return "success"
//we can check rout by putting route in the opened local hosturl e.g http://127.0.0.1:5000/success

then route3 # dynamic route 
@app.route('/hello/<string:name>')//we type casted to get string variable as a dynamic variable with in url
def hello(name):
    return "Hello, " +name 
//http://127.0.0.1:5000/hello/Maria check like this in local host url

//created another route 4
@app.route('/hello/<string:name>/<int:age>')
def hello_name(name,age):
    return f"Hello, {name }, you are {age}, years old." 
    # birth_year=2024-age
    # return f'"Hello," +{name} + "you are born in "+{birth_year}'
# following is a constructor which will run the application directly

day02 template Jinja notes

first create env by this . open folder in integrated terminal and run this to create environment 
        ====>pipenv install flask

4. then run this ==> pipenv shell
1. copied first and last in server.py 
2. create static and template folder in hello_world folder
3. add html file and add script and link both from bootstrap one after title and other after body script
4. design html
5. import this in server.py from flask import Flask, render_template
6. write routes then
7. we created another template html and created its route in server.py users .html @app.route('/hello/<string:name>/<int:age>')
def hello_user(name,age):
    return render_template('hello_user.html',age=age,name=name)

8. created another template.demo and set another route for that and check that route in open url by following route e.g http://127.0.0.1:5000/user/get/1 and it will give you that particular user .....this is the route which we wrote in server.py===>#3
@app.route('/user/get/<int:id>')
def get_user(id):
    user={
        'id':3,
        "first_name":"wilma",
        "email_address":"abc@gamil.com"
    }
    return render_template('templates.demo.html',user=user)