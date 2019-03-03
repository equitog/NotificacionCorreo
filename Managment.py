""" Gestion de Personas en Base de Datos """
print("Bienvenido al gestor de directorios de correo")
print("A continuacion se le da los pasos a seguir segun su requerimiento")
print("Si presiona 'l', se listaran las primeros 15 registros.\nPresione 'i' para insertar.\nPresione 'a' para actualizar.\nPresione 'e' eliminar un registro")
option = input("Esperando opcion: ")
from conectionpostgrestsql import conectionpsql

if option.lower() == 'l':
    pass
elif option.lower() == 'i':
    index = input('Inserte Indice: ')
    name = input('Inserte Nombre del receptor: ')
    mail = input('Inserte Correo: ')
    mail_2 = input('Inserte segundo Correo(Opcional): ')
    subject = input('Asunto del correo: ')
    body = input('Inserte Text del correo: ')
    datesend = input('Ingrese fecha de envio: ')
    enabled = input('Inserte 0:habilitado, 1:inhabilitado')
    attachment = input('Inserte 0:Con correo Adjunto, 1:Sin correo Adjunto')
    file = input('Inserte el nombre del archivo si puso 0 en la opcion anterior')
    conn = conectionpsql()
    cursor = conn.cursor()

    query_insert = """INSERT INTO Test VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(query_insert, (index, name, mail, mail_2, subject, body, datesend, enabled, attachment, file))
    conn.commit()

    print('Se inserto correctamente')
    query_select = """SELECT * FROM test WHERE id = %s"""
    cursor.execute(query_select, index)
    record = cursor.fetchone()
    print(record)

    cursor.close()
    conn.close()
elif option.lower() == 'a':
    index = input('Indice: ')
    column = input('Columna: ')
    valuecolumn = input('Ingrese nuevo valor de columna: ')
    conn = conectionpsql()
    cursor = conn.cursor()

    query_update = """UPDATE Test SET {0} = %s WHERE id = %s"""
    query_update = query_update.format(column)
    cursor.execute(query_update, (valuecolumn, index))
    conn.commit()

    print('Se actualizo correctamente')
    query_select = """SELECT * FROM test WHERE id = %s"""
    cursor.execute(query_select, index)
    record = cursor.fetchone()
    print(record)

    cursor.close()
    conn.close()
elif option.lower() == 'e':
    pass


