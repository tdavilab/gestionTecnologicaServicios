# compose_flask/app.py
# https://runnable.com/docker/python/docker-compose-with-flask-apps
# https://stackoverflow.com/questions/42316511/communication-between-two-flask-services-in-docker
# https://github.com/eelkevdbos/microservices-flask/blob/master/concat/concat.py
from flask import Flask
from flask import render_template,request,make_response
import requests

app = Flask(__name__)

@app.route("/<num1>/<num2>/<signo>")
def default(num1,num2,signo):
	if signo == '+':
		resultado=requests.get('http://suma:5000/'+num1+'/'+num2).text
	elif signo == '-':
		resultado=requests.get('http://resta:5000/'+num1+'/'+num2).text
	elif signo == '*':
		resultado=requests.get('http://multiplicacion:5000/'+num1+'/'+num2).text
	elif signo == '/':
		resultado=requests.get('http://division:5000/'+num1+'/'+num2).text
	return resultado

if __name__ == "__main__":
    	app.run(host="0.0.0.0", debug=True)




