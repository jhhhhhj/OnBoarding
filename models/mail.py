from pydantic import BaseModel

class Mail(BaseModel):
    sender_email: str
    receiver_email: str
