import oracledb

#função com Oracle Database
def get_connection():
    try:
        connection = oracledb.connect('rm557137/020106@oracle.fiap.com.br:1521/orcl')
        print('Conectado com o Oracle DB')
    except Exception as e:
        print(f'error obtaining a conncetion: {e}')
return connection

#função select
def listar():
    connection = get_connection()
    cursor = connection.cursor()
    sql = 'SELECT * FROM <tabela>'
    cursor.execute(sql)

    for linha in cursor:
        print(linha)

    cursor.close()
    connection.close()

# Função Insert 
def inserir():
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO <tabela> VALUES (1, 'Jennifer', 'Vieira')"
    cursor.execute(sql)
    connection.commit()
    print('Ddods Inseridos!')
    cursor.close()
    connection.close()


def inserir_param(id, nome, sobrenome):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO <tabela> (id, nome, sobrenome) VALUES({id}, {nome}, {sobrenome})"