# Este modulo no llego a ser implementado a tiempo

import smtplib  # Librería para enviar correos electrónicos desde python
import getpass  # Librería para ocultar la contraseña al momento de ser ingresada
from email.message import EmailMessage 

asunto = "SpotyUN"
usuario = input("Correo: ")
destinatario = input("destinatario: ")
email_smtp = "smtp.gmail.com" 
contraseña = getpass.getpass("contraseña: ")

# se crea el objeto Emailmessage con el cual se hace la estructura para mandar el correo
message = EmailMessage() 

# Configuración de encabezado 
message['Subject'] = asunto 
message['From'] = usuario 
message['To'] = destinatario 

# Se establece el mensaje 
message.set_content(input("Mensaje: ")) 

# Se establece el servidor
server = smtplib.SMTP(email_smtp, '587') 

# Identifica este usuario al servidor SMTP
server.ehlo() 

# Secure the SMTP connection 
server.starttls() 

# Se ingresa a la cuenta
server.login(usuario, contraseña) 

# Se envia el mensaje 
server.send_message(message) 
print("Mensaje enviado")

# Se cierra la conexión al servidor 
server.quit()