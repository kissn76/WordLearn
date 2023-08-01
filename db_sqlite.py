import sqlite3
from sqlite3 import Error
import os


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


    def database_drop(self):
        os.remove(self.sqlitePath)


    def create_table(self, create_table_sql:str):
        if not bool(self.conn):
            self.create_connection()

        if bool(self.conn):
            try:
                cur = self.conn.cursor()
                cur.execute("PRAGMA foreign_keys = 1")
                cur.execute(create_table_sql)
            except Error as e:
                print(e)

            self.connection_close()
        else:
            print("Error! Cannot create the database connection.")


    def create_tables(self):
        sql_types = """
                        CREATE TABLE IF NOT EXISTS types (
                            code TEXT NOT NULL,
                            name TEXT NOT NULL,
                            description TEXT,
                            PRIMARY KEY(code),
                            UNIQUE(code),
                            CHECK (code != ''),
                            CHECK (name != '')
                        );
                    """
        self.create_table(sql_types)
        types = {"vorb_1": ("Vorb 1st format", ""), "vorb_2": ("Vorb 2nd format", ""), "vorb_3": ("Vorb 3rd format", ""), "noun_singular": ("Noun singular", ""), "noun_plural": ("Noun plural", ""), "adjective_positive": ("Adjective positive", ""), "adjective_comparative": ("Adjective comparative", ""), "adjective_superlative": ("Adjective superlative", ""), "adverb": ("Adverb", "")}
        for code, value in types.items():
            self.data_insert("types", code=code, name=value[0], description=value[1])

        sql_words = """
                        CREATE TABLE IF NOT EXISTS words (
                            id INTEGER,
                            word TEXT NOT NULL,
                            type_code TEXT NOT NULL,
                            connection_id INTEGER,
                            PRIMARY KEY(id AUTOINCREMENT),
                            UNIQUE(word, type_code),
                            FOREIGN KEY(type_code) REFERENCES types(code),
                            FOREIGN KEY(connection_id) REFERENCES words(id),
                            CHECK (word != ''),
                            CHECK (type_code != '')
                        );
                    """
        self.create_table(sql_words)
        words = [
                ["read", "vorb_1", None],
                ["read", "vorb_2", None],
                ["read", "vorb_3", None],
                ["book", "noun_singular", None],
                ["books", "noun_plural", None]
            ]
        for word, type_code, connection_id in words:
            self.data_insert("words", id=None, word=word, type_code=type_code, connection_id=connection_id)

        sql_languages = """
                        CREATE TABLE IF NOT EXISTS languages (
                            code TEXT NOT NULL,
                            name TEXT NOT NULL,
                            description TEXT,
                            PRIMARY KEY(code),
                            UNIQUE(code),
                            CHECK (code != ''),
                            CHECK (name != '')
                        );
                    """
        self.create_table(sql_languages)
        languages = {"en_AU": ("English Australian", ""), "en_GB": ("English British", ""), "en_US": ("English American", ""), "hu_HU": ("Hungarian", "")}
        for code, value in languages.items():
            self.data_insert("languages", code=code, name=value[0], description=value[1])

        sql_pronunciations = """
                        CREATE TABLE IF NOT EXISTS pronunciations (
                            id INTEGER,
                            word_id INTEGER NOT NULL,
                            language_code TEXT NOT NULL,
                            phonetic TEXT NOT NULL,
                            voice TEXT,
                            PRIMARY KEY(id),
                            FOREIGN KEY(word_id) REFERENCES words(id),
                            FOREIGN KEY(language_code) REFERENCES languages(code),
                            CHECK (language_code != ''),
                            CHECK (phonetic != '')
                        );
                    """
        self.create_table(sql_pronunciations)

        sql_media = """
                        CREATE TABLE IF NOT EXISTS medias (
                            id INTEGER,
                            name TEXT NOT NULL,
                            type TEXT NOT NULL,
                            path TEXT NOT NULL,
                            description TEXT,
                            PRIMARY KEY(id AUTOINCREMENT),
                            UNIQUE(name, type),
                            CHECK (name != ''),
                            CHECK (type != ''),
                            CHECK (path != '')
                        );
                    """
        self.create_table(sql_media)


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
                cur.execute("PRAGMA foreign_keys = 1")
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


    def languages_get(self):
        ret = self.data_select("languages")
        return ret


    def words_get(self):
        ret = self.data_select("words")
        return ret