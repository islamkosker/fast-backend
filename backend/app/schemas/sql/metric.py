from typing import Optional
from pydantic import ConfigDict, BaseModel
from uuid import UUID


class MetricBase(BaseModel):
    key: str
    unit: str
    description: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class MetricCreate(MetricBase):
    pass

class MetricUpdate(MetricBase):
    pass


class MetricInDB(MetricBase):
    id: int


class Metric(MetricInDB):
    pass
