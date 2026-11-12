from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="usbw",
        database="institucion"
    )


@app.route('/')
def index():

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM estudiantes")

    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('index.html', estudiantes=estudiantes)


@app.route('/crear', methods=['GET', 'POST'])
def crear():

    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        programa = request.form['programa']

        conexion = conectar()
        cursor = conexion.cursor()

        sql = """INSERT INTO estudiantes
        (nombre, apellido, correo, programa)
        VALUES (%s, %s, %s, %s)"""

        cursor.execute(sql, (nombre, apellido, correo, programa))

        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    if request.method == 'POST':

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        programa = request.form['programa']

        sql = """UPDATE estudiantes
        SET nombre=%s, apellido=%s,
        correo=%s, programa=%s
        WHERE id=%s"""

        cursor.execute(sql, (nombre, apellido, correo, programa, id))

        conexion.commit()
        cursor.close()
        conexion.close()

        return redirect(url_for('index'))

    cursor.execute(
        "SELECT * FROM estudiantes WHERE id=%s",
        (id,)
    )

    estudiante = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template('editar.html', estudiante=estudiante)


@app.route('/eliminar/<int:id>')
def eliminar(id):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM estudiantes WHERE id=%s",
        (id,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)