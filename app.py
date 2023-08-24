from flask import Flask,render_template,request
app=Flask(__name__)

from flask_cors import CORS



import requests




def toper(a):
    percent=a*100
    return percent
CORS(app)

@app.route('/donner',methods=['get'])
def maint():




  args=request.args
  html=args.get("url")
  htmlz=requests.get(html).text
  topred=htmlz









































  return render_template('preddonner.html',azz=topred)
@app.route('/cy',methods=['POST','GET'])
def cy():
    return render_template("cy.html")
@app.after_request
def after_request(response):


  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response
