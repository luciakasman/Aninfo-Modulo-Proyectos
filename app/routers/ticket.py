from pydantic import BaseModel

class Ticket(BaseModel):
    ticketNumber: int
    title: str