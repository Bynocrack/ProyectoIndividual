import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

'''uri = os.getenv("DATABASE_URL")

if uri and uri.startswith("postgres://"):
  uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Mensaje(db.Model):
  nombre = db.Column(db.String(100), nullable=False)
  presupuesto = db.Column(db.Float, nullable=False)
  correo = db.Column(db.String(100), nullable=False)
  mensaje = db.Column(db.Text, nullable=False)

with app.app_context():
  db.create_all()'''

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/agradecimientos')
def agradecimientos():
  return render_template('agradecimientos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
  '''if request.method == 'POST':
    nombre = request.form['nombre']
    presupuesto = float(request.form['presupuesto'])
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    nuevo_mensaje = Mensaje(
      nombre=nombre,
      presupuesto=presupuesto,
      correo=correo,
      mensaje=mensaje
    )

    try:
      db.session.add(nuevo_mensaje)
      db.session.commit()
      return redirect(url_for('index'))
    except Exception as e:
      db.session.rollback()
      return f"Ocurrió un error al enviar el mensaje: {e}"'''

  return render_template('contacto.html')

@app.route('/experiencia')
def experiencia():
  return render_template('experiencia.html')

@app.route('/proyectos')
def proyectos():
  return render_template('proyectos.html')

if __name__ == '__main__':
  app.run(debug=True)