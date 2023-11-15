from flask import Flask,render_template,request
from modules.ml import ml
app = Flask(__name__)

@app.route('/phDetection',methods=['GET','POST'])
def pred():

    x= "Please specify the number of days for predicting rainfall's pH"
    if request.method=='POST' and 'text' in request.form:
        value = request.form["text"]
        print(value)
        # ml_obj  = ml()
        # x = ml_obj.runQuery(value)
        x = 8
    return render_template('home.html',inp = x)

if __name__ == "__main__":
    app.run(debug=True)