from flask import Flask,render_template,request
from modules.ml import ml
app = Flask(__name__)

@app.route('/phDetection',methods=['GET','POST'])
def pred():
    adv = ''
    x= "Please specify the number of days for predicting rainfall's pH"
    if request.method=='POST' and 'text' in request.form:
        value = request.form["text"]
        value = int(value)
        ml_obj  = ml()
        x = ml_obj.runQuery(value)
        if 0 <= x < 5.5:
            adv = "Strongly acidic. Consider neutralizing agents."
        elif 5.5 <= x< 6.5:
            adv = "Neutral. Good pH for most plants and aquatic life."
        elif 7.5 <= x < 8.5:
            adv = "Slightly alkaline. Monitor and manage alkalinity levels."
        elif 8.5 <= x:
            adv = "Strongly alkaline. Consider measures to reduce alkalinity."
    return render_template('home.html',inp = x,advice = adv)

@app.route("/",methods=['GET','POST'])
def loc():
    return render_template("loc.html")




if __name__ == "__main__":
    app.run(debug=True)