from pydantic import BaseModel


class User(BaseModel):
    """A user entity"""

    id: str
    username: str
    email: str
    password: str
