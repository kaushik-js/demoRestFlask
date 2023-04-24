from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return "Welcome "+  name

@app.route('/hello/<user>')
def hello(user):
    return render_template('hello.html',name = user)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/check/<string:name>/<int:marks>')
def check(name, marks):
    return render_template('hello.html',name = name,marks=marks)

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        mrk = request.form['mrk']
        return redirect(url_for('check', name=user, marks=mrk))

    else:
        user = request.args.get('nm')
        mrk = request.args.get('mrk')
        return redirect(url_for('check', name=user, marks=mrk))

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("allresult.html",result = result);

if __name__ == '__main__':
    app.run()