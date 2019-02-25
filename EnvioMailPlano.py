def sendmail(sentmail: str, frommail: str, subjectmail: str, bodymail: str) -> object:
    import smtplib
    import ssl

    port = 465  # Para Ssl
    password = 'AsusenaS911'

    """ Creacion de seguridad contexto SSL """
    context = ssl.create_default_context()

    """ COnfiguracion de envios """
    by_email = sentmail
    from_email = frommail
    bodymails = bodymail.encode('Latin-1')
    message_body = 'Subject: {0}\n\n{1}'.format(subjectmail, bodymails)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login("empresain.erp@gmail.com", password)
            server.sendmail(by_email, from_email, message_body)
            a = 'El correo ha sido enviado satisfactoriamente...'
    except Exception:
        a = 'No se pudo envíar correo'
    return print(a)


sendmail('empresain.erp@gmail.com', 'quito.gonz.ern@gmail.com', 'Hola', 'Envío')
