from sqlalchemy import Column, DateTime
from datetime import datetime, timezone


class TimeStampMixin:

    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))