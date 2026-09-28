from flask import Flask
from flask import request
from flask import render_template

app=Flask (__name__)

# @app.route ("/")
# def hello_rukesh():
#     return "<h1> hello my name is rukesh gupta <h1>"

# @app.route("/student")
# def student():
#     x=8*5
#     return "<h1> result of this multiply {}<h1>.".format(x)

# @app.route("/test")
# def test():
#     data=request.args.get("y")
#     return "<h1> this is my url {}<h1>".format(data)

# @app.route("/data")
# def data():
#     a=20+15
#     return "<h1> result of this addition {}<h1>".format(a)


@app.route("/")
def hello_word():
    return render_template("index.html")

@app.route("/greeting")
def greeting():
    return """
    
     
    <h1>👋 welcome to student! </h1>
    <p> this is a basic flask </p>
    <p> Every URL can be connected to a python function</p>  
"""
@app.route ("/flask")
def flask ():
    return"""
<h1> 📕 How are you? </h1>
<p> Flask is a phython variable </p>
<h2> student is a learn </h2>
<ul> 
<li> creating application in python </li>
<li> URL Routing</li>
<li> HTML template </li>
<li> CSS Styling </li>
<li> Handling User Input </li>
<li> Connecting Python with web page </li>
</ul>
"""
@app.route("/calculate")
def calculate():
    a=50
    b=60
    result = a+b
    sub = a-b
    multiple = a*b
    return """
    <h> 🧮 python calculate </h1>
    <h2> {a} + {b} = {result}
         {a} - {b} = {result}
         {a} * {b} = {result}  
    </h2>
<p> flask can execute python code and display the result in the brower</p>
    """
@app.route("/student")
def student():
    name=request.args.get("name")
    return """
<h1>🎓 student information </h1>
<h2> hello {name}! </h2>
<p> my Good afternoon eveerone my name is Rukesh gupta at BCA 3rd semester student </p>
<p> how flask receives date from URL </p>
<p> Query Perameter:||||
<strong> name = {name} </strong>
</p>
"""
     
if __name__=="__main__":
    app.run(host="0.0.0.0")

