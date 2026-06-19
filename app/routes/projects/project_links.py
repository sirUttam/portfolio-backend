from fastapi import APIRouter, Depends, HTTPException
from app.models.projects.project_links import ProjectLinks
from app.models.projects.project import Project
from app.schemas.projects.project_links import ProjectLinksBase, ProjectLinksResponse, ProjectLinksUpdate
from app.auth.dependencies import get_current_user
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/projects/{project_id}/links', response_model=ProjectLinksResponse)
def create_links(data: ProjectLinksBase, project_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    # first need to get the project card
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found"
        )
    
    new_link = ProjectLinks(
        type = data.type,
        url = data.url,
        project_id = project.id
    )
    
    db.add(new_link)
    db.commit()
    db.refresh(new_link)
        
    return new_link


@router.put('/projects/links/{link_id}', response_model=ProjectLinksResponse)
def update_link(data: ProjectLinksUpdate, link_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    link = db.query(ProjectLinks).filter(ProjectLinks.id == link_id).first()

    if not link:
        raise HTTPException(
            status_code=404, detail="Link  not found"
        )

    updated_link = data.model_dump(exclude_unset=True)

    for key, value in updated_link.items():
        setattr(link, key, value)
    
    db.commit()
    db.refresh(link)
    
    return link


@router.delete('/projects/links/{link_id}')
def delete_link(link_id: int, current_user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    link = db.query(ProjectLinks).filter(ProjectLinks.id == link_id).first()

    if not link:
        raise HTTPException(
            status_code=404, detail="Link not found"
        )
    
    db.delete(link)
    db.commit()

    return {"message": "Deleted successfully"}