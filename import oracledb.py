import oracledb

#função com Oracle Database
def get_connection():
    connection = oracledb.connect('rm557137/020106@oracle.fiap.com.br:1521/orcl')
    print('Conectado com o Oracle DB')
return connection

#função select
def listar():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM <tabela>'
    cursor.execute(sql)

    for linha in cursor:
        print(linha)

# Connection.commit()
cursor.close()
connection.close()