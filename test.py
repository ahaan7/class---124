from flask import Flask 
app=Flask(__name__)
@app.route('/')
def hello():
    return "hello friends we are creating our first api"
@app.route('/about')
def about():
    return "Good morning i am Ahaan"

@app.route('/contact')
def contact():
    return "My mobile no:9056851045"

if (__name__=="__main__"):
    app.run(debug=True)


