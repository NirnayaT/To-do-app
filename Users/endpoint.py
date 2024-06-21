from fastapi import APIRouter,HTTPException
from Users.payload import UserCreatePayload, UserLoginPayload
from Database.database import User
from Database.database import *
from sqlalchemy.exc import IntegrityError
from hash import pass_hash, verify_pass
router = APIRouter()


@router.post("/register")
def register_user(create_user_data: UserCreatePayload):
    try:
        new_user=User(
            username = create_user_data.username,
            email = create_user_data.email,
            password_hash = pass_hash(create_user_data.password)
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already registered")

@router.post("/login")
def login_user(get_user_data: UserLoginPayload):
    user = session.query(User).filter(User.username == get_user_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not Found")
    verification = verify_pass(get_user_data.password,user.password_hash)
    if verification == False:
        raise HTTPException(status_code=401, details="Incorrect password")
    elif verification == True:
        return{"Login":"successfull"}
    


    