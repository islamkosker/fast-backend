from typing import Any, Dict, Optional, Union, List
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.sql import Metric 
from app.crud.sql.base import CRUDBase 
from app.schemas.sql import MetricCreate, MetricUpdate


class CRUDMetric(CRUDBase[Metric, MetricCreate, MetricUpdate]):
    pass


metric = CRUDMetric(Metric)