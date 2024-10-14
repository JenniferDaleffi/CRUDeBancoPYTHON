import oracledb

def get_connection():
    connection = oracledb.connect('rm557137/020106@oracle.fiap.com.br:1521/orcl')
    print('Conectado com o Oracle DB')
return connection

