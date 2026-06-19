from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.auth.dependencies import get_current_user
from sqlalchemy.orm import Session
from app.schemas.projects.project_tools import ProjectToolsBase, ProjectToolsResponse, ProjectToolsUpdate
from app.models.projects.project import Project
from app.models.projects.project_tools import ProjectTools



router = APIRouter()


@router.post('/projects/{project_id}/tools', response_model=ProjectToolsResponse)
def create_tools(data: ProjectToolsBase, project_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    # first need to get the project card
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404, detail="Project not found"
        )
    
    new_tool = ProjectTools(
        title = data.title,
        project_id = project.id
    )
    
    db.add(new_tool)
    db.commit()
    db.refresh(new_tool)
        
    return new_tool


@router.put('/projects/tools/{tool_id}', response_model=ProjectToolsResponse)
def update_tool(data: ProjectToolsUpdate, tool_id: int, current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    tool = db.query(ProjectTools).filter(ProjectTools.id == tool_id).first()

    if not tool:
        raise HTTPException(
            status_code=404, detail="Tool  not found"
        )

    updated_tool = data.model_dump(exclude_unset=True)

    for key, value in updated_tool.items():
        setattr(tool, key, value)
    
    db.commit()
    db.refresh(tool)
    
    return tool


@router.delete('/projects/tools/{tool_id}')
def delete_tool(tool_id: int, current_user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    
    tool = db.query(ProjectTools).filter(ProjectTools.id == tool_id).first()

    if not tool:
        raise HTTPException(
            status_code=404, detail="Tool not found"
        )
    
    db.delete(tool)
    db.commit()

    return {"message": "Deleted successfully"}