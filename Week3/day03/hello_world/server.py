from flask import Flask

app= Flask(__name__)

# decorator or tag
@app.route('/')
def hello_world():
    return "Hello World"
# static route2 
@app.route('/success')
def success():
    return "success"

# dynamic route3 
@app.route('/hello/<string:name>')
def hello(name):
    return "Hello, " +name 

# 
@app.route('/hello/<string:name>/<int:age>')
def hello_name(name,age):
    return f"Hello, {name }, you are {age}, years old." 
    # birth_year=2024-age
    # return f'"Hello," +{name} + "you are born in "+{birth_year}'
# following is a constructor which will run the application directly
if __name__ =="__main__":
    app.run(debug=True)