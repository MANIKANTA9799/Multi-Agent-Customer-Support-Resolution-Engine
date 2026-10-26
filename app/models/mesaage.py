from datetime import datetime
from uuid import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime, String, text, func, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
from app.models.ticket import Ticket
from app.models.base import Base

class Message(Base):
    __tablename__ = "messages"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    ticket: Mapped["Ticket"] = relationship(
    back_populates="messages"
)
    ticket_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("tickets.id", ondelete="CASCADE"), nullable=False
    )
    sender_type: Mapped[str] = mapped_column(String, nullable=False) # 'user', 'agent', 'system'
    content: Mapped[str] = mapped_column(Text, nullable=False)
    ai_metadata: Mapped[dict] = mapped_column(JSONB, server_default='{}', nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )