from flask import Flask, render_template #Funcao render render_template

app = Flask(__name__)

@app.route('/')
def principal():
	frutas = ["Morango", "Uva", "Laranja", "Mamão", "Maçã", "Pêra", "Melão", "Abacaxi"]
	return render_template("index.html",frutas=frutas)

@app.route('/sobre')
def sobre():
	return render_template("sobre.html")

#http://127.0.0.1:5000

app.run(debug=True)

