#app/models/sql/metric.py

from pydoc import describe
import uuid
from sqlalchemy import UUID, Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.sql.base_class import Base


class Metric(Base):
    # Performance-optimized: Integer primary key for fast joins
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    # API compatibility: UUID for external references
    uuid = Column(UUID(as_uuid=True), unique=True, index=True, default=uuid.uuid4)
    
    # Metric properties
    key = Column(String, index=True, nullable=False, unique=True)
    unit = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)

