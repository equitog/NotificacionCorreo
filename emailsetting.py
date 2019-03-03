def sendmail(sender: str, receiver: str, name: str,subjectmail: str, bodymail: str, attachment: int, file: str) -> object:
    import smtplib
    import ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders
    from email.mime.base import MIMEBase

    port = 465  # Para Ssl
    password = 'AsusenaS911'

    """ Creacion de seguridad contexto SSL """
    context = ssl.create_default_context()

    """ COnfiguracion de envios """

    message = MIMEMultipart('alternative')
    message['Subject'] = subjectmail
    message['From'] = sender
    message['To'] = receiver


    # html = """\
    # <html>
    # <body>
    #     <p>Hi,<br>
    #     How are you?<br>
    #     <a href="http://www.realpython.com">Real Python</a>
    #     has many great tutorials.
    #     </p>
    # </body>
    # </html>
    # """
    bodymail = bodymail.format(name)
    message.attach(MIMEText(bodymail, 'html'))
    #part2 = MIMEText(html, 'html')

    #message.attach(part1)
    #message.attach(part2)
    if attachment == 0:
        filename = file

        with open(filename, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header(
            'Content-Disposition',
            f'attachment; filename = {filename}',
        )
        message.attach(part)

    text = message.as_string()


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver.split(', '), text)
            a = 'El correo ha sido enviado satisfactoriamente...'
    except Exception:
        a = 'No se pudo envíar correo'
    return print(a)

