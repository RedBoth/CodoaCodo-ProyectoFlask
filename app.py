from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/destinsos')
def destinos():
  return render_template('destinations.html')

@app.route('/servicios')
def servicios():
  return render_template('services.html')

@app.route('/contacto')
def contacto():
  return render_template('form.html')

@app.route('/validacionform')
def validacionform():
  return render_template('validation-form.html')

@app.route('/viajes')
def viajes():
  return render_template('viajes/viajes.html')

if __name__=='__main__':
  app.run(debug=True)