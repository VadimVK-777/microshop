from fastapi import APIRouter
from users.schemas import CreateUser, CreateUser
from users import crud

print("Hello World")
router = APIRouter(prefix='/users', tags=['Users'])

@router.post('/')
def create_user(user: CreateUser):
    return crud.create_user(user_in=user)
