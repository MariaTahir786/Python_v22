from flask import Flask
app= Flask(__name__) 

@app.route('/')
def home():
    return "Hello World"

@app.route('/techcircle/')
def school_name():
    return "Tech Circle"

@app.route('/say/<string:name>')
def say_Hi(name):
    return "Hi, " +name

@app.route('/repeat/<int:i>/<string:word>')
def say_something(i, word):
    repeated_word = word + '<br>'  
    return repeated_word * i

if __name__ =="__main__":
    app.run(debug=True)
