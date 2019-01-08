

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('form.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form   # this part collects all the work that is in HTML to dictionaries instead of listing them
      return render_template("result.html",result = result)

