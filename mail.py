from readfile import readfile
from emailsetting import sendmail
""" Buscar por nombre y estado"""
search = 'Alejandra'
enable = 'Activo'

""" Lectura de datos """
query = 'SELECT * FROM test'

""" Obteniendo informacion de lectura """
file = readfile(1, query)
""" Realizando busqueda """
file = file[file['name'].str.contains(search)]

""" Enviar corrreo """
for reg in file.itertuples():
    name = reg[1]
    receiver_mail = reg[2]
    mail2 = reg[3]
    subject = reg[4]
    body = str(reg[5])
    sendmail('empresain.erp@gmail.com', receiver_mail, name, subject, body, 0, '')
