import databases
import ormar
import sqlalchemy


database = databases.Database('postgresql+asyncpg://postgres:postgres@localhost:5432/postgres')
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata