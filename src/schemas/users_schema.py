from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    description: str
    price: int


class UserCreate(UserBase):
    pass


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: EmailStr | None = None


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
