from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
import  schemas
from models import Role
from database import get_db
from schemas import RoleCreate

router = APIRouter()


# @router.post("/roles/", status_code=status.HTTP_201_CREATED, response_model=None)
# def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
#     if not role.role_name.isalpha():
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="Enter valid data"
#         )

#     role_count = db.query(Role).count() + 1
#     prefixed_role_id = f"role_{role_count}"
#     db_role = Role(role_id=prefixed_role_id, role_name=role.role_name)
#     db.add(db_role)
#     db.commit()
#     db.refresh(db_role)
#     return {
#         "status_code": status.HTTP_201_CREATED,
#         "message": "Role created successfully.",
#         "Method": "POST",
#         "Path": "/roles/"
#     }

@router.post("/roles/", status_code=status.HTTP_201_CREATED, response_model=None)
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    role_name_trimmed = ' '.join(role.role_name.strip().split())
    if not all(part.isalpha() for part in role_name_trimmed.split()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Enter valid data. Role name must contain alphabetic characters only."
        )
    role_count = db.query(Role).count() + 1
    prefixed_role_id = f"role_{role_count}"
    db_role = Role(role_id=prefixed_role_id, role_name=role_name_trimmed)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return {
        "status_code": status.HTTP_201_CREATED,
        "message": "Role created successfully.",
        "Method": "POST",
        "Path": "/roles/"
    }


@router.get("/roles/{role_id}", response_model=schemas.Role)
def read_role(role_id: str, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    return db_role  

# @router.put("/roles/{role_id}",status_code=status.HTTP_200_OK, response_model=None)
# def update_role(role_id: str, role: schemas.RoleUpdate, db: Session = Depends(get_db)):
#     db_role = db.query(Role).filter(Role.role_id == role_id).first()
#     if db_role is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")

#     if role.role_name is not None:
#         db_role.role_name = role.role_name
#     if role.status is not None:
#         db_role.status = role.status
    
#     db.commit()
#     db.refresh(db_role)  
#     # return db_role  
#     return {
#         "status_code": status.HTTP_201_CREATED,
#         "message": "Role updated successfully.",
#         "Method":"PUT",
#         "Path":"/roles/"

#     }

@router.put("/roles/{role_id}", status_code=status.HTTP_200_OK, response_model=None)
def update_role(role_id: str, role: schemas.RoleUpdate, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")
    if role.role_name is not None:
        role_name_trimmed = ' '.join(role.role_name.strip().split())
        if not all(part.isalpha() for part in role_name_trimmed.split()):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Enter valid data. Role name must contain alphabetic characters only."
            )
        
        db_role.role_name = role_name_trimmed
    if role.status is not None:
        db_role.status = role.status
    db.commit()
    db.refresh(db_role)

    return {
        "status_code": status.HTTP_200_OK,
        "message": "Role updated successfully.",
        "Method": "PUT",
        "Path": "/roles/"
    }



@router.delete("/roles/{role_id}",status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete_role(role_id: str, db: Session = Depends(get_db)):
    db_role = db.query(Role).filter(Role.role_id == role_id).first()
    if db_role is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")

    db.delete(db_role)
    db.commit()
    # return db_role 
    return {"detail": "Role deleted successfully"}