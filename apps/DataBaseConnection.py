import psycopg2 as psy

#Conecta no banco de dados
def conectarAoBanco():
    conn = psy.connect(
        host = "mydemoserveritv.postgres.database.azure.com",
        dbname = "postgres",
        user = "postgres@mydemoserveritv",
        password = "pvo0787P."
    )
    
    return conn

def consultaBanco(conn, query):
    all = conn.cursor() #cursos utilizado para escrever a consulta
    all.execute(query) #consulta
    all_fetch = all.fetchall() #retorna todos os resultados da consulta
    
    return all_fetch