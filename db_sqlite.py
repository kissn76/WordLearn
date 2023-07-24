import sqlite3
from sqlite3 import Error


class Database():
    def __init__(self, path="database.db") -> None:
        self.sqlitePath = path
        self.conn = None


    def create_connection(self) -> sqlite3.Connection:
        try:
            self.conn = sqlite3.connect(self.sqlitePath)
        except Error as e:
            print(e)


    def connection_close(self):
        self.conn.close()
        self.conn = None


    def create_table(self, create_table_sql:str):
        if not bool(self.conn):
            self.create_connection()

        if bool(self.conn):
            try:
                cur = self.conn.cursor()
                cur.execute(create_table_sql)
            except Error as e:
                print(e)

            self.connection_close()
        else:
            print("Error! Cannot create the database connection.")


    def create_tables(self):
        sql_types = """CREATE TABLE IF NOT EXISTS types (
                        id integer PRIMARY KEY,
                        type text NOT NULL UNIQUE
                    );"""

        self.create_table(sql_types)
        types = ("vorb_1", "vorb_2", "vorb_3", "noun_singular", "noun_plural", "adjective_positive", "adjective_comparative", "adjective_superlative", "adverb")
        for word in types:
            print(word)
            self.data_insert("types", type=word)


    def data_insert(self, table:str, **values) -> int:
        columnNames = ', '.join(values.keys())
        columnValues = ', '.join(['?'] * len(values))
        sql = f"INSERT INTO {table} ({columnNames}) VALUES ({columnValues})"
        ret = None

        if not bool(self.conn):
            self.create_connection()

        if bool(self.conn):
            try:
                cur = self.conn.cursor()
                cur.execute(sql, tuple(values.values()))
                self.conn.commit()
                ret = cur.lastrowid
            except Error as e:
                print(e)

            self.connection_close()
        else:
            print("Error! Cannot create the database connection.")

        return ret


    def data_select(self, table:str, fields:tuple=("*",), whereClause:str=None) -> list:
        ret = None

        selectFields = ','.join(fields)
        sql = f"SELECT {selectFields} FROM {table}"

        if bool(whereClause):
            sql += f" WHERE {whereClause}"

        if not bool(self.conn):
            self.create_connection()

        if bool(self.conn):
            try:
                cur = self.conn.cursor()
                cur.execute(sql)
                ret = cur.fetchall()
            except Error as e:
                print(e)

            self.connection_close()
        else:
            print("Error! Cannot create the database connection.")

        return ret


    def types_get(self):
        ret = self.data_select("types")
        print(ret)
        return ret