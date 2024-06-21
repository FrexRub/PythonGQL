from . import models, database
# This will create the `tasks` table in the database
# if it doesn't exist yet
models.Base.metadata.create_all(bind=database.engine)