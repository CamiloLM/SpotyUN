# import os
import smtplib  # Librería para enviar correos electrónicos desde python
from email.message import EmailMessage


def enviar_correo(destinatario, contenido):
    """
    Envia un correo siguendo la metodologia SMTP
    
    Parametros:
    destinatario (string): Correo electronico del destinatario
    mensaje (string): Cuerpo del mensaje que se va a enviar
    """
    EMAIL_ADDRESS = "soporte.spotyun@gmail.com"
    EMAIL_PASSWORD = "Y@hYycq*]6br$J6;KUs6"

    mensaje = EmailMessage()
    mensaje['Subject'] = "Lista de SpotyUN"
    mensaje['From'] = EMAIL_ADDRESS
    mensaje['To'] = destinatario
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

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(mensaje)
        print("Mensaje enviado con exito, revise su correo.")
