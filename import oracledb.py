import oracledb

#função com Oracle Database
def get_connection():
    try:
        connection = oracledb.connect('rm557137/password@oracle.fiap.com.br:1521/orcl')
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
    print('Dados Inseridos!')
    cursor.close()
    connection.close()


def inserir_param(id, nome, sobrenome):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO <tabela> (id, nome, sobrenome) VALUES({id}, {nome}, {sobrenome})"
    data = (id, nome, sobrenome)
    cursor.execute(sql, data)
    print(f'Dados inseridos!')
    cursor.close()
    connection.close()

# Função Update
def atualizar():
    connection = get_connection()
    cursor = conecction.cursor()
    sql = "UPDATE <tabela> SET nome = 'Jennifer' WHERE id = 1"
    cursor.execute()
    conecction.commit()
    print(f'Dados atualizados!')
    cursor.close()
    conecction.close()

# Função delete
def apagar():
    conncetion = get_connection()
    cursor = conecction.cursor()
    sql = "DELETE FROM <tabela> WHERE id = {1}"
    cursor.execute(sql)
    connection.commit()
    print(f'Dados apagados!')
    cursor.close
    conecction.close()

# Principal
conecction = get_connection()
print(f'Versão: {conecction.version}')
listar()
Inserir()
listar()
inserir_param (5, 'Jennifer', 'Vieira')