import db_sqlite as db


def get_all() -> list:
    database = db.Database()
    data = database.data_select("medias")
    objects = []
    for t in data:
        objects.append(Media(t[0], t[1], t[2], t[3], t[4]))

    return objects


class Media():
    def __init__(self, id=None, name=None, mediatype=None, path=None, description=None):
        self.id = id
        self.name = name
        self.mediatype = mediatype
        self.path = path
        self.description = description

        self.__table_name = "medias"


    def get_as_dict(self):
        representation = {}
        representation.update({"id": self.id})
        representation.update({"name": self.name})
        representation.update({"mediatype": self.mediatype})
        representation.update({"path": self.path})
        representation.update({"description": self.description})
        return representation


    def load(self):
        database = db.Database()
        data = None

        if bool(self.id):
            data = database.data_select(self.__table_name, whereClause=f"id={self.id}")
        if bool(self.path):
            data = database.data_select(self.__table_name, whereClause=f"path={self.path}")
        elif bool(self.name) and bool(self.mediatype):
            data = database.data_select(self.__table_name, whereClause=f"name={self.name} AND mediatype={self.mediatype}")

        if bool(data):
            self.id = data[0]
            self.name = data[1]
            self.mediatype = data[2]
            self.path = data[3]
            self.description = data[4]


    def save(self):
        # fájlnév beállítása, egyediség ellenőrzése
        # kép átalakítása jpg képpé, maximális képméretre csökkentés, túl kicsi kép visszadobása
        # hang
        # videó
        database = db.Database()
        self.id = database.data_insert(self.__table_name, id=None, name=self.name, mediatype=self.mediatype, path=self.path, description=self.description)