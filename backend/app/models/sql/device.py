#app/models/sql/device.py

from pydoc import describe
import uuid
from sqlalchemy import UUID, Boolean, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.sql.base_class import Base


class Device(Base):
    # API compatibility: UUID primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Performance-optimized: String serial number for joins
    serial_number = Column(String, index=True, nullable=False, unique=True)

    # User relationship
    user_id = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=True, index=True)

    # Device properties
    name = Column(String, index=True)
    is_active = Column(Boolean, default=True, index=True)
    model = Column(String, index=True, nullable=True)

    # Relationships
    user = relationship("User", back_populates="devices")
