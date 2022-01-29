# import os
import smtplib  # Librería para enviar correos electrónicos desde python
from email.message import EmailMessage  # Objeto para crear un mensaje por correo


def enviar_correo(destinatario, contenido):
    """
    Envia un correo siguendo la metodologia SMTP
    
    Parametros:
    destinatario (string): Correo electronico del destinatario
    mensaje (string): Tabla HTML con las canciones del cliente.
    """
    # Credenciales del correo
    EMAIL_ADDRESS = "soporte.spotyun@gmail.com"
    EMAIL_PASSWORD = "Y@hYycq*]6br$J6;KUs6"

    mensaje = EmailMessage()  # Se crea una nueva instancia del codigo

    # Asignamos desde donde se envia, hacia donde y el asunto
    mensaje['Subject'] = "Lista de SpotyUN"
    mensaje['From'] = EMAIL_ADDRESS
    mensaje['To'] = destinatario

    # Creo el mensaje con estructura HTML
    mensaje.add_alternative(
        """\
        <html>
        <head>
            <style>
                table, th, td {
                    border: 1px solid black;
                    border-collapse: collapse;
                }
            </style>
        </head>
            <body>
                <p>Buen día apreciado cliente, aquí esta la lista con sus canciones.</p>
        """ + contenido + """\
                <p>Equipo de SpotifyUN.</p>
            </body>
        </html>
        """, subtype = "html")

    # Se establece la conexion con el servidor de gmail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Inicia sesion con las credenciales
        smtp.send_message(mensaje)  # Envia el mensaje almacenado
        print("Mensaje enviado con exito, revise su correo.")
