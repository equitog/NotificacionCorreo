def conectionpsql():
    import psycopg2

    conn = psycopg2.connect(database='auditoria', user='postgres', password='g3r4ld1n3', host='144.217.87.110')

    return conn
