import db_sqlite as db


def main():
    database = db.Database()
    database.create_tables()
    # database.types_get()
    # id = "eee"
    # name = None
    # description = None
    # database.type_add(id, name, description)


if __name__ == '__main__':
    main()