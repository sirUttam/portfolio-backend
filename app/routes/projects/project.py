from fastapi import APIRouter, Depends, HTTPException
from app.schemas.projects.project import ProjectResponse, ProjectBase, ProjectUpdate
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.dependencies import get_current_user
from app.models.projects.project import Project

router = APIRouter()

@router.get('/projects', response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    
    projects = db.query(Project).all()
    
    if not projects:
        raise HTTPException(
            status_code=404, detail="Projects not available"
        )
    
    return projects



@router.post('/projects', response_model=ProjectResponse)
def create_project(data: ProjectBase, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    new_project = Project(
        title = data.title,
        description = data.description
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project



@router.put('/projects/{project_id}', response_model=ProjectResponse)
def update_project(data: ProjectUpdate, project_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found"
        )

    updated_project = data.model_dump(exclude_unset=True)

    for key, value in updated_project.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project



@router.delete('/projects/{project_id}')
def delete_project(project_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "deleted_id": project_id
    }