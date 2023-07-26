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
        sql_types = """
                        CREATE TABLE IF NOT EXISTS types (
                        id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT
                    );
                    """
        self.create_table(sql_types)

        types = {"vorb_1": ("Vorb 1st format", ""), "vorb_2": ("Vorb 2nd format", ""), "vorb_3": ("Vorb 3rd format", ""), "noun_singular": ("Noun singular", ""), "noun_plural": ("Noun plural", ""), "adjective_positive": ("Adjective positive", ""), "adjective_comparative": ("Adjective comparative", ""), "adjective_superlative": ("Adjective superlative", ""), "adverb": ("Adverb", "")}
        for id, value in types.items():
            self.data_insert("types", id=id, name=value[0], description=value[1])

        sql_words = """
                        CREATE TABLE IF NOT EXISTS words (
                        id INTEGER PRIMARY KEY,
                        word TEXT NOT NULL,
                        type_id TEXT NOT NULL,
                        connection_id INTEGER,
                        FOREIGN KEY(type_id) REFERENCES types(id),
                        FOREIGN KEY(connection_id) REFERENCES words(id)
                    );
                    """
        self.create_table(sql_words)

        sql_languages = """
                        CREATE TABLE IF NOT EXISTS languages (
                        code TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT
                    );
                    """
        self.create_table(sql_languages)
        languages = {"en_AU": ("English Australian", ""), "en_GB": ("English British", ""), "en_US": ("English American", ""), "hu_HU": ("Hungarian", "")}
        for code, value in languages.items():
            self.data_insert("languages", code=code, name=value[0], description=value[1])

        sql_pronunciations = """
                        CREATE TABLE IF NOT EXISTS pronunciations (
                        id INTEGER PRIMARY KEY,
                        word_id INTEGER NOT NULL,
                        language_id TEXT NOT NULL,
                        phonetic TEXT NOT NULL,
                        voice TEXT,
                        FOREIGN KEY(word_id) REFERENCES words(id),
                        FOREIGN KEY(language_id) REFERENCES languages(code)
                    );
                    """
        self.create_table(sql_pronunciations)


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
        return ret


    def languages_get(self):
        ret = self.data_select("languages")
        return ret