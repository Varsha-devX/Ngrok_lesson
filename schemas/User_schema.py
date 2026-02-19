from pydantic import BaseModel

class UserSchema(BaseModel):
    email:str
    password:str
class userupdateapikey(BaseModel):
    api_key:str   