from smtplib import SMTP  # Librería para enviar correos electrónicos desde python
from email.message import EmailMessage


def enviar_correo(destinatario, mensaje):
    email_smtp = "smtp.gmail.com"
    usuario = "soporte.spotyun@gmail.com"
    contraseña = "Y@hYycq*]6br$J6;KUs6"

    # Se crea el objeto Emailmessage con el cual se hace la estructura para mandar el correo
    message = EmailMessage() 

    # Configuración de encabezado 
    message['Subject'] = "Lista de SpotyUN"
    message['From'] = usuario
    message['To'] = destinatario

    # Se establece el mensaje 
    message.set_content(mensaje) 

    # Se establece el servidor
    server = SMTP(email_smtp, '587') 

    # Identifica este usuario al servidor SMTP
    server.ehlo() 

    # Secure the SMTP connection 
    server.starttls() 

    # Se ingresa a la cuenta
    server.login(usuario, contraseña) 

    # Se envia el mensaje 
    server.send_message(message) 
    print("Mensaje enviado rebisa tu correo.")

    # Se cierra la conexión al servidor 
    server.quit()
