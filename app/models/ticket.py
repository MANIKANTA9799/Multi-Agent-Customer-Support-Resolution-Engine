from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String, text, func, ForeignKey, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()")
    )
    
    # ADDED: ForeignKey to ensure this user actually exists
    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    
    subject: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, server_default='queued', nullable=False)
    
    # CHANGED: Back to String so we can assign it to "BillingAgent" or a human ID
    assigned_to: Mapped[str | None] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    # ADDED: Table args to enforce our state machine rules at the database level
    __table_args__ = (
        CheckConstraint(
            "status IN ('queued', 'processing', 'awaiting_user', 'escalated', 'resolved', 'failed', 'closed')",
            name="valid_status"
        ),
    )