import sqlite3

class SQLiteConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print("Conexão com o banco de dados estabelecida.")
        except sqlite3.Error as error:
            print("Erro ao conectar ao banco de dados:", error)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco de dados fechada.")

    def execute_query(self, query, parameters=None):
        try:
            with self.connection as conn:
                cursor = conn.cursor()
                if parameters:
                    cursor.execute(query, parameters)
                else:
                    cursor.execute(query)
                conn.commit()
                print("Query executada com sucesso.")
                return cursor.fetchall()
        except sqlite3.Error as error:
            print("Erro ao executar a query:", error)
            return None

    def create_database(self):
        query = '''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
        '''
        self.execute_query(query)
        print("Banco de dados e tabela criados com sucesso.")

    def table_exists(self, table_name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name=?;"
        result = self.execute_query(query, (table_name,))
        return len(result) > 0
