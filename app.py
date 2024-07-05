from flask import Flask
from flask import render_template, request,redirect
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gottravel'
### Puerto MySQL en Xampp
#app.config['MYSQL_PORT'] = 3307

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

#Borrar registro
@app.route('/destroy/<int:id>')
def destroy(id):
  conn = mysql.connection;
  cursor = conn.cursor();
  cursor.execute("DELETE FROM `gottravel`.`viajes` WHERE id=%s", (id,))
  conn.commit()
  cursor.close()
  return redirect("/viajes");

#Editar registro
@app.route('/edit/<int:id>')
def edit(id):
  conn = mysql.connection
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `gottravel`.`viajes` WHERE id=%s", (id,))
  viajes = cursor.fetchall()
  cursor.close()
  return render_template('viajes/edit.html', viajes = viajes)

#Actualizacion de datos
@app.route('/update', methods=['POST'])
def update():
  destino = request.form['txtDestino'];
  fechaInicio = datetime.strptime(request.form['txtFechaInicio'], '%Y-%m-%d');
  fechaFin = datetime.strptime(request.form['txtFechaFin'], '%Y-%m-%d');
  pasajeros = request.form['txtPasajeros'];
  id = request.form['txtID'];
  
  conn  = mysql.connection;
  cursor = conn.cursor();
  #Actualizacion
  sql = "UPDATE `gottravel`.`viajes` SET destino=%s, fechaInicio=%s, fechaFin=%s, numPasajeros=%s WHERE id=%s"
  nuevos_datos = (destino, fechaInicio, fechaFin, pasajeros, id);
  cursor.execute(sql, nuevos_datos);
  conn.commit();
  cursor.close()
  #Redireccion a viajes
  return redirect("/viajes");

#Creacion de registros
@app.route('/create')
def create():
  return render_template('viajes/create.html')
#Guardar registros
@app.route('/store', methods=['POST'])
def storage():
  #Recibir datos del formulario y almacenarlos en variables
  destino = request.form['txtDestino'];
  fechaInicio = datetime.strptime(request.form['txtFechaInicio'], '%Y-%m-%d');
  fechaFin = datetime.strptime(request.form['txtFechaFin'], '%Y-%m-%d');
  pasajeros = request.form['txtPasajeros'];
  #Ordenar los datos
  datos = (destino, fechaInicio, fechaFin, pasajeros);
  #Almacenar datos en la DB
  sql = "INSERT INTO `gottravel`.`viajes`\
        (`id`, `destino`, `fechaInicio`, `fechaFin`, `numPasajeros`)\
        VALUES (NULL, %s, %s, %s, %s);"
  conn  = mysql.connection;
  cursor = conn.cursor();
  cursor.execute(sql, datos);
  conn.commit();
  cursor.close()
  #Redireccion a viajes
  return redirect("/viajes");

if __name__=='__main__':
  app.run(debug=True)