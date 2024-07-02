from flask import Flask
from flask import render_template, request,redirect, send_from_directory
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gottravel'
### Puerto MySQL en Xampp
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/destinos')
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
  sql = "SELECT * FROM viajes;"
  
  conn = mysql.connection
  cursor = conn.cursor() 
  cursor.execute(sql)
  
  db_viajes = cursor.fetchall()
  
  cursor.close()
  
  return render_template('viajes/viajes.html', viajes=db_viajes)

if __name__=='__main__':
  app.run(debug=True)