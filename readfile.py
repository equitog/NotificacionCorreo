def readfile(typeread, file):
    global setting
    if typeread == 0:
        import pandas as pd
        setting = pd.read_excel(file, sheet_name=0, index_col='Id')
        setting = setting[setting['enabled'] == 0]
    elif typeread == 1:
        import psycopg2
        import pandas as pd
        pd.set_option('display.expand_frame_repr', False)
        conn = psycopg2.connect(database='auditoria', user='postgres', password='g3r4ld1n3', host='144.217.87.110')
        setting = pd.read_sql_query(file, conn, index_col='id')
        setting = setting[setting['enabled'] == 0]
        conn.close()
    else:
        print('No se especifico archivo de lectura')
    return setting
