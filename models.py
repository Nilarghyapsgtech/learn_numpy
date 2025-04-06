from database import *
from sqlalchemy import Column, ForeignKey,Integer,String
from sqlalchemy.orm import relationship

class BaseModel(Base):
    __abstract__=True
    __allow_unmapped__=True
    id=Column(Integer,primary_key=True,index=True)

class Address(BaseModel):
    __tablename__='address'
    city=Column(String)
    state=Column(String)
    zip_code=Column(String)
    user_id=Column(ForeignKey('user.id'))
    
    def _add_info(self):
        print(f"<Address is {self.id} and {self.city}")

class User(BaseModel):
    __tablename__='user'
    name=Column(String)
    addresses=relationship('Address')

    def _add_info(self):
        print(f"<Address is {self.id} and {self.name}")