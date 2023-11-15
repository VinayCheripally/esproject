from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/phDetection',methods=['GET','POST'])
def pred():

    x= 0
    if 'text' in request.form and request.method=='POST':
        x = 7
    return render_template('home.html',inp = x)

if __name__ == "__main__":
    app.run(debug=True)