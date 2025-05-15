from fastapi import APIRouter
from ..model.user import Type_User_Create, Type_Login
from ..database import Mongo_Collection
import motor.motor_asyncio
import jwt, os



SECRETE =  os.getenv('SECRETE')
CLIENT = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('CONNECTION_STRING'))
DB = CLIENT['CLOUD_COLLECTION']
COLLECTION = DB['COLLECTION_USERS']   

route_user = APIRouter()

# Create user
@route_user.post("/create_user")
async def create_user(data: Type_User_Create):
    print('START: Create user')

    # Check is passwords match
    if data.password == data.password_match:

        # Check user exist
        if await COLLECTION.find_one({"username": data.username}):
            return {"message": "user already exist"}

        print(data)
        print(data.password)
        print(data.username)
        try:
            print("SECRETE: ", SECRETE)
            jwt_password = jwt.encode({"password": data.password}, SECRETE, algorithm="HS256")
        except TypeError:
            print("Error: TypeError, missing SECRETE")
        user = {
            "username": data.username,
            "password": jwt_password
        }

        # Create user
        await COLLECTION.insert_one(user)
        return {"message": "user created"}
    
    else:
        return {"message": "Error: passwords do not match "}


# Login user
@route_user.post("/login")
async def login_user(data: Type_Login):

    #
    db_user = COLLECTION.find_one(data.username)
    # if db_user:
    #     token = jwt.decode(db_user['password'], SECRETE, algorithms=['HS256'] )
    #     if token:
    #         if 
    return "Home"