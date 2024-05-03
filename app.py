# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from markupsafe import Markup
import plotly
import json
import plotly.graph_objs as go


app = Flask(__name__)
app.secret_key = 'ABC'

# Configurar la base de datos
def get_db_connection():
    conn = sqlite3.connect('ods.db')
    conn.row_factory = sqlite3.Row
    return conn

# Rutas y vistas
@app.route('/')
def index():
    conn = get_db_connection()
    ods = conn.execute('SELECT * FROM ods').fetchall()
    conn.close()
    return render_template('index.html', ods=ods)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # Lógica de inicio de sesión
#         pass
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # Lógica de registro
#         pass
#     return render_template('register.html')

@app.route('/progress', methods=['GET', 'POST'])
def progress():
    conn = get_db_connection()
    if request.method == 'POST':
        ods_id = request.form['ods_id']
        user_id = request.form['user_id']
        valor = request.form['valor']
        fecha = request.form['fecha']

        # Validar datos
        if not ods_id or not user_id or not valor or not fecha:
            flash('Por favor, complete todos los campos.', 'error')
        else:
            # Guardar progreso en la base de datos
            cursor = conn.cursor()
            cursor.execute("INSERT INTO progress (ods_id, user_id, valor, fecha) VALUES (?, ?, ?, ?)",
                           (ods_id, user_id, valor, fecha))
            conn.commit()
            flash('Progreso registrado correctamente.', 'success')

    # Obtener los datos de progreso de la base de datos
    progress_data = conn.execute('SELECT p.id, o.nombre, u.name, p.valor, p.fecha '
                                 'FROM progress p '
                                 'JOIN ods o ON p.ods_id = o.id '
                                 'JOIN users u ON p.user_id = u.id').fetchall()
    ods = conn.execute('SELECT * FROM ods').fetchall()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('progress.html', progress_data=progress_data, ods=ods, users=users)


@app.route('/stats')
def stats():
    conn = get_db_connection()

    # Obtener los datos de progreso de la base de datos
    progress_data = conn.execute('SELECT p.ods_id, o.nombre, SUM(p.valor) AS total_valor '
                                 'FROM progress p '
                                 'JOIN ods o ON p.ods_id = o.id '
                                 'GROUP BY p.ods_id').fetchall()

    # Preparar los datos para la gráfica
    ods_nombres = [row['nombre'] for row in progress_data]
    ods_valores = [row['total_valor'] for row in progress_data]

    # Crear la gráfica de barras
    trace = go.Bar(x=ods_nombres, y=ods_valores)
    layout = go.Layout(title='Porcentaje de avance de los ODS',
                       xaxis=dict(title='ODS'),
                       yaxis=dict(title='Valor'))
    fig = go.Figure(data=[trace], layout=layout)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    graphJSON = Markup(graphJSON)  

    conn.close()
    return render_template('stats.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)