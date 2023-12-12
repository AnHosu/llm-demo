from psycopg.types.json import Jsonb
from pydantic import BaseModel


class PostgresBaseModel(BaseModel):
    """
    A small extension of pydantic.BaseModel to include a dumping method for
    adapting models that are headed into a Postgres database.
    """
    def model_dump_ps(self, *args, **kwargs) -> dict:
        """
        Generate a dictionary representation of the model, optionally
        specifying which fields to include or exclude. Any dictionary entries
        will be converted to Jsonb for ingestion to Postgres.
        """
        d = self.model_dump(*args, **kwargs)
        d = {k: (Jsonb(v) if isinstance(v, dict) else v) for k, v in d.items()}
        return d
