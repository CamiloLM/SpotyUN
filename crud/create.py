import sqlite3
from insert import insertar_canciones, insertar_clientes, insertar_planes


def crear_tablas(con, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS cancion (
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ubicacion TEXT NOT NULL,
        genero TEXT,
        album TEXT,
        interprete TEXT
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS cliente (
        cedula INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        correo TEXT NOT NULL,
        pais TEXT,
        ciudad TEXT,
        telefono INTEGER,
        targetaCredito INTEGER,
        fechaPago TEXT,
        pago INTEGER
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS planes (
        nombre TEXT PRIMARY KEY,
        valor float,
        cantidad INTEGER,
        decripcion TEXT
        )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS subscripciones (
        cedulaCliente INTEGER,
        nombrePlan INTEGER,
        FOREIGN KEY (nombrePlan) REFERENCES planes (nombre),
        FOREIGN KEY (cedulaCliente) REFERENCES cliente (cedula)
        )''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS listaCanciones (
        nombreLista TEXT NOT NULL,
        cedulaCliente INTEGER,
        codigoCancion INTEGER,
        FOREIGN KEY (codigoCancion) REFERENCES cancion (codigo),
        FOREIGN KEY (cedulaCliente) REFERENCES cliente (cedula)
        )''')
    
    con.commit()

clientes = (
	[
		6512378532,
		"Moses",
		"White","urna.nunc@protonmail.couk",
		"Netherlands",
		"Guainía",
		14113718605,
		5893831582337562,
		"2021-03-16",
		1
	],
	[
		2179653278,
		"Nathan",
		"Atkins",
		"non.arcu@outlook.edu",
		"United States",
		"Sachsen-Anhalt",
		8727453767,
		378776287887626,
		"2021-04-05",
		1
	],
	[
		1385743748,
		"Melodie",
		"Cohen",
		"dui.nec@google.com",
		"Austria",
		"Colorado",
		4267286512,
		300294663565231,
		"2021-04-30",
		0
	],
	[
		5643232873,
		"Craig",
		"Berry",
		"dapibus.gravida.aliquam@aol.ca",
		"Peru",
		"Zeeland",
		5115628783,
		4916157787471,
		"2021-05-12",
		1
	],
	[
		3218746384,
		"Otto",
		"Dunn",
		"lectus@protonmail.com",
		"Italy",
		"Kaluga Oblast",
		2137535649,
		4508718744826,
		"2021-05-19",
		0
	],
	[
		8795632168,
		"Carter",
		"Alston",
		"sit@protonmail.edu",
		"CostaRica",
		"Ancash",
		5288877666,
		4844332836612355,
		"2021-05-21",
		0
	],
	[
		4984865495,
		"Matthew",
		"Luna",
		"fusce.mollis@hotmail.org",
		"New Zealand",
		"Dōngběi",
		18197641106,
		5152975695888742,
		"2021-06-10",
		1
	],
	[
		3216461898,
		"Laurel",
		"Wynn",
		"consectetuer.cursus@google.org",
		"Costa Rica",
		"Istanbul",
		6138086147,
		4539863565377,
		"2021-10-28",
		1
	],
	[
		3549874321,
		"Hermione",
		"Bonner",
		"id.ante@icloud.edu",
		"Netherlands",
		"Arequipa",
		3103246360,
		6465463844467538,
		"2021-11-05",
		0
	]
)


canciones = (
	[
		None,
		"Aftershock",
		"Aftershock.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Bright Red and March Away",
		"Bright Red and March Away.mp3",
		"Pop",
		"Bright Red and March Away",
		"IRIS BEVY"
	],
	[
		None,
		"Conqueror",
		"Conqueror.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Drum Go Dum",
		"Drum Go Dum.mp3",
		"Kpop",
		"ALL OUT",
		"K/DA"
	],
	[
		None,
		"Edge of Night",
		"Edge of Night.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Executioner's Calling",
		"Executioner's Calling.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"I’ll Show You",
		"I’ll Show You.mp3",
		"Kpop",
		"ALL OUT",
		"K/DA"
	],
	[
		None,
		"Last Stand",
		"Last Stand.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Lost Chapter",
		"Lost Chapter.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Love of My Life",
		"Love of My Life.mp3",
		"Pop",
		"Love of My Life",
		"BEN LVCAS"
	],
	[
		None,
		"Love Your Life Away",
		"Love Your Life Away.mp3",
		"Pop",
		"Love Your Life Away",
		"MERCURY & THE ARCHITECTS"
	],
	[
		None,
		"More",
		"More.mp3",
		"Kpop",
		"ALL OUT",
		"K/DA"
	],
	[
		None,
		"Predator",
		"Predator.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Redemption",
		"Redemption.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Stormrazor",
		"Stormrazor.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"The Baddest",
		"The Baddest.mp3",
		"Kpop",
		"ALL OUT",
		"K/DA"
	],
	[
		None,
		"The Gathering Storm",
		"The Gathering Storm.mp3",
		"Metal",
		"Pentakill 3",
		"Pentakill"
	],
	[
		None,
		"Vices",
		"Vices.mp3",
		"Pop",
		"Vices",
		"Julius Marx"
	],
	[
		None,
		"Villain",
		"Villain.mp3",
		"Kpop",
		"ALL OUT",
		"K/DA"
	]
)

planes = (
	["Gratis", None, 1, "Escucha música solo en modo aleatorio y con anuncios."],
	["Individual", 14900.00, 1, "Escucha música sin anuncios. Reproduce tus canciones en cualquier lugar, incluso sin conexión. Prepaga o suscríbete por solo $ 14900.00 al mes"],
	["Duo", 19900.00, 2, "Te damos 2 cuentas Premium perfecto parejas que conviven por $ 19900.00 al mes. Ademas te damos una lista para dos, actualizada periódicamente con la música que más les gusta."],
	["Familiar", 23900.00, 6, "Te damos 6 cuentas Premium para familiares que conviven ademas con una lista para tu familia. Reproducción de música sin anuncios, sin conexión y on-demand. Prepaga o suscríbete $ 23900.00 al mes."]
)

if __name__ == "__main__":
    con = sqlite3.connect('SpotyUN.db')
    con.execute("PRAGMA foreign_keys = 1")
    cur = con.cursor()

    crear_tablas(con, cur)
    insertar_clientes(con, cur, clientes)
    insertar_canciones(con, cur, canciones)   
    insertar_planes(con, cur, planes) 

    con.close()