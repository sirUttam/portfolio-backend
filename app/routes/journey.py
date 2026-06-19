from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.schemas.journey import JourneyBase, JourneyResponse, JourneyUpdate
from app.models.journey import Journey


router = APIRouter()


@router.get('/journey', response_model=list[JourneyResponse])
def get_journey(db: Session = Depends(get_db)):
    
    journey = db.query(Journey).all()

    if not journey:
        raise HTTPException(
            status_code=404, detail="Journey not found"
        )

    return journey


@router.post('/journey', response_model=JourneyResponse)
def create_journey(data: JourneyBase, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    new_journey = Journey(
        title = data.title,
        subtitle = data.subtitle
    )
    
    db.add(new_journey)
    db.commit()
    db.refresh(new_journey)

    return new_journey



@router.put('/journey/{journey_id}', response_model=JourneyResponse)
def update_journey(data: JourneyUpdate, journey_id: int, current_user:dict = Depends(get_current_user), db:Session = Depends(get_db)):
    
    journey = db.query(Journey).filter(Journey.id == journey_id).first()

    if not journey:
        raise HTTPException(
            status_code=404, detail="Journey not found"
        )

    updated_journey = data.model_dump(exclude_unset=True)

    for key, value in updated_journey.items():
        setattr(journey, key, value)

    db.commit()
    db.refresh(journey)

    return journey



@router.delete('/journey/{journey_id}')
def delete_journey(journey_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    journey = db.query(Journey).filter(Journey.id == journey_id).first()
    
    if not journey:
        raise HTTPException(
            status_code=404, detail="Journey not found"
        )
        
    db.delete(journey)
    db.commit()

    return {"deleted_id": journey_id}
    