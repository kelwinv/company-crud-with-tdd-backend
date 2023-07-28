"""peewee db connection"""

from peewee import PostgresqlDatabase, Model

from company_server.config.env import DATABASE_CONFIG


class PostgresDatabase:
    """connection pg database"""

    database_instance = None

    @classmethod
    def connect(cls):
        """connect to database"""
        if not cls.database_instance:
            cls.database_instance = PostgresqlDatabase(
                DATABASE_CONFIG["database"],
                user=DATABASE_CONFIG["user"],
                password=DATABASE_CONFIG["password"],
                host=DATABASE_CONFIG["host"],
                port=int(DATABASE_CONFIG["port"]),
            )

        return cls.database_instance


class BasePGModel(Model):
    """Base"""

    class Meta:
        """config db"""

        database = PostgresDatabase.connect()
        schema = DATABASE_CONFIG["schema"]
