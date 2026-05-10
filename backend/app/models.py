from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    phone: str
    roles: list[str] = []
    last_login: str | None
    is_active: bool

# Extend with other models like Router, Voucher, Session as needed