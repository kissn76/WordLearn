import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("words")
    objects = []
    for t in data:
        objects.append(Word(t[0], t[1], t[2], t[3]))

    return objects


class Word():
    def __init__(self, id=None, word=None, wordtype=None, connection_id=None):
        self.id = id
        self.word = word
        self.wordtype = wordtype
        self.connection_id = connection_id

        self.__table_name = "words"


    def get_as_dict(self):
        representation = {}
        representation.update({"id": self.id})
        representation.update({"word": self.word})
        representation.update({"wordtype": self.wordtype})
        representation.update({"connection_id": self.connection_id})
        return representation


    def load(self):
        database = db.Database()
        data = None

        if bool(self.id):
            data = database.data_select(self.__table_name, whereClause=f"id={self.id}")
        elif bool(self.word) and bool(self.wordtype):
            data = database.data_select(self.__table_name, whereClause=f"word={self.word} AND wordtype={self.wordtype}")

        if bool(data):
            self.id = data[0]
            self.word = data[1]
            self.wordtype = data[2]
            self.connection_id = data[3]


    def save(self):
        database = db.Database()
        self.id = database.data_insert(self.__table_name, id=None, word=self.word, wordtype=self.wordtype, connection_id=self.connection_id)
