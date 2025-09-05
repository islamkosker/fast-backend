"""
class Metric(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    key = Column(String, index=True, nullable=False, unique=True)
    uint = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=True)
"""

metrics = [
    {"key": {"test"}},
    {"uint": {"test_unit"}},
    {"description": {"test description"}},
]
