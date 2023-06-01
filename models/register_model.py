from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "name":"ThoriqLigarHaidar",
                "username":"thoriq123",
                "password":"12345678",
            }
        }
