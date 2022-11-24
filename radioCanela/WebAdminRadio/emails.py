from django.core.mail import EmailMessage
from django.conf import settings
from smtplib import SMTPException


def enviar_email(titulo:str, contenido:dict, destinatarios:list, tipo: str):
    correo = EmailMessage(
        subject=titulo,
        body=contenido,
        from_email=settings.EMAIL_HOST_USER,
        to=destinatarios
    )

    correo.content_subtype = tipo # Actualizamos en que formato va a esta el cuerpo del correo

    try:
        correo.send(fail_silently=False)
        return True
    except SMTPException:
        print('Ocurrio un error al enviar el correo')
        return False