from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from uuid import UUID

from app import crud, schemas, models
from app import dependencies

router = APIRouter()


@router.post("/", response_model=schemas.sql.Metric, status_code=201)
def create_metric(
    *,
    db: Session = Depends(dependencies.get_db),
    metric_in: schemas.sql.MetricCreate,
    current_user=Depends(dependencies.get_current_user),
):
    """Create a new metric"""
    # Check if metric with this key already exists

    if crud.sql.metric.read_by_column(
        db=db, column=models.sql.Metric.key, value=metric_in.key
    ):
        raise HTTPException(
            status_code=400, detail=f"Metric with key '{metric_in.key}' already exists"
        )

    new_metric = crud.sql.metric.create(db=db, obj_in=metric_in)
    return schemas.sql.Metric.model_validate(new_metric)


@router.get("/", response_model=List[schemas.sql.Metric])
def read_metrics(
    *,
    db: Session = Depends(dependencies.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(dependencies.get_current_user),
) -> Any:
    """Get all metrics with pagination"""
    metrics = crud.sql.metric.read_multi(db=db, offset=skip, limit=limit)

    if not metrics:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    return [schemas.sql.Metric.model_validate(metric) for metric in metrics]



@router.delete("/{metric_id}")  # TODO: fix secure delete
def delete_metric(
    *,
    db: Session = Depends(dependencies.get_db),
    metric_id: UUID,
    current_user=Depends(dependencies.get_current_user),
) -> Any:
    """Delete a metric"""
    metric = crud.sql.metric.read(db=db, id=metric_id)
    if not metric:
        raise HTTPException(status_code=404, detail="Metric not found")


    crud.sql.metric.delete(db=db, id=metric_id)
    return {"message": "Metric deleted successfully"}
