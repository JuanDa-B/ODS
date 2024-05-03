import sqlite3

def database():
    conn = sqlite3.connect('ods.db')

    # Obtener el cursor
    cursor = conn.cursor()

    # Crear la tabla de ODS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT NOT NULL
        )
    """)

    ods_data = [
        ('Fin de la pobreza', 'Poner fin a la pobreza en todas sus formas en todo el mundo.'),
        ('Hambre cero', 'Poner fin al hambre, lograr la seguridad alimentaria y la mejora de la nutrición, y promover la agricultura sostenible.'),
        ('Salud y bienestar', 'Garantizar una vida sana y promover el bienestar para todos en todas las edades.'),
        ('Educación de calidad', 'Garantizar una educación inclusiva, equitativa y de calidad, y promover oportunidades de aprendizaje durante toda la vida para todos.'),
        ('Igualdad de género', 'Lograr la igualdad entre los géneros y empoderar a todas las mujeres y las niñas.'),
        ('Agua limpia y saneamiento', 'Garantizar la disponibilidad de agua y su gestión sostenible y el saneamiento para todos.'),
        ('Energía asequible y no contaminante', 'Garantizar el acceso a una energía asequible, segura, sostenible y moderna para todos.'),
        ('Trabajo decente y crecimiento económico', 'Promover el crecimiento económico sostenido, inclusivo y sostenible, el empleo pleno y productivo y el trabajo decente para todos.'),
        ('Industria, innovación e infraestructura', 'Construir infraestructuras resilientes, promover la industrialización inclusiva y sostenible, y fomentar la innovación.'),
        ('Reducción de las desigualdades', 'Reducir la desigualdad en y entre los países.'),
        ('Ciudades y comunidades sostenibles', 'Lograr que las ciudades y los asentamientos humanos sean inclusivos, seguros, resilientes y sostenibles.'),
        ('Producción y consumo responsables', 'Garantizar modalidades de consumo y producción sostenibles.'),
        ('Acción por el clima', 'Adoptar medidas urgentes para combatir el cambio climático y sus efectos.'),
        ('Vida submarina', 'Conservar y utilizar en forma sostenible los océanos, los mares y los recursos marinos para el desarrollo sostenible.'),
        ('Vida de ecosistemas terrestres', 'Proteger, restablecer y promover el uso sostenible de los ecosistemas terrestres, gestionar los bosques de forma sostenible, luchar contra la desertificación, detener e invertir la degradación de las tierras y poner freno a la pérdida de la diversidad biológica.'),
        ('Paz, justicia e instituciones sólidas', 'Promover sociedades pacíficas e inclusivas para el desarrollo sostenible, facilitar el acceso a la justicia para todos y crear instituciones eficaces, responsables e inclusivas a todos los niveles.'),
        ('Alianzas para lograr los objetivos', 'Fortalecer los medios de ejecución y revitalizar la Alianza Mundial para el Desarrollo Sostenible.')
    ]

    # Insertar datos de los ODS
    cursor.executemany("INSERT INTO ods (nombre, descripcion) VALUES (?, ?)", ods_data)

   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    usuarios_data = [
        ('Juan David',),
        ('Natalie',)
    ]

    cursor.executemany("INSERT INTO users (name) VALUES (?)", usuarios_data)


    # Crear la tabla de progreso
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ods_id INTEGER NOT NULL,
            valor REAL NOT NULL,
            fecha TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (ods_id) REFERENCES ods(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    progreso_data = [
        (1, 25.5, '2023-04-01', 1),
        (2, 18.7, '2023-03-15', 1),
        (3, 30.0, '2023-04-05', 2),
        (4, 12.3, '2023-03-20', 2),
    
    ]

    cursor.executemany("INSERT INTO progress (ods_id, valor, fecha, user_id) VALUES (?, ?, ?, ?)", progreso_data)

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

database()