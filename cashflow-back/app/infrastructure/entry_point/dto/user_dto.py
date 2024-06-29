from pydantic import BaseModel, EmailStr

class UserDto(BaseModel):
    id: int
    email: EmailStr
    password: str

    class Config:
        orm_mode = True