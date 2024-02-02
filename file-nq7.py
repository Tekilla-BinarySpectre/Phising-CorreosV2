import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Colores para resaltar el texto en la consola
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main_menu():
    print(Colors.HEADER + "=====================================")
    print("|   Bienvenido a la herramienta de   |")
    print("|             phishing              |")
    print("|         Autor: Tekilla            |")
    print("=====================================" + Colors.END)
    print("Por favor, selecciona una opción:")
    print("1. " + Colors.BLUE + "Phishing de Gmail" + Colors.END)
    print("2. " + Colors.BLUE + "Phishing de Outlook" + Colors.END)
    print("3. " + Colors.BLUE + "Otros servicios de correo" + Colors.END)
    print("4. " + Colors.FAIL + "Salir" + Colors.END)

    option = input("Ingrese el número de opción: ")

    if option == "1":
        phishing_gmail()
    elif option == "2":
        phishing_outlook()
    elif option == "3":
        phishing_otro_correo()
    elif option == "4":
        exit()
    else:
        print(Colors.FAIL + "Opción inválida. Por favor, seleccione una opción válida." + Colors.END)
        main_menu()

def phishing_gmail():
    print(Colors.GREEN + "¡Phishing de Gmail seleccionado!" + Colors.END)
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.close()
        print(Colors.GREEN + "Correo enviado con éxito." + Colors.END)
    except:
        print(Colors.FAIL + "Error al enviar el correo. Verifica tus credenciales y asegúrate de tener acceso al servidor SMTP de Gmail." + Colors.END)

def phishing_outlook():
    print(Colors.GREEN + "¡Phishing de Outlook seleccionado!" + Colors.END)
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target
def phishing_outlook():
    print(Colors.GREEN + "¡Phishing de Outlook seleccionado!" + Colors.END)
    sender_email = input("Ingresa tu dirección de correo electrónico: ")
    sender_password = input("Ingresa tu contraseña: ")
    target_email = input("Ingresa la dirección de correo electrónico del objetivo: ")
    subject = input("Ingresa el asunto del correo: ")
    body = input("Ingresa el cuerpo del correo: ")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.office365.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, target_email, msg.as_string())
        server.close()
        print(Colors.GREEN + "Correo enviado con éxito." + Colors.END)
    except:
        print(Colors.FAIL + "Error al enviar el correo. Verifica tus credenciales y asegúrate de tener acceso al servidor SMTP de Outlook." + Colors.END)
