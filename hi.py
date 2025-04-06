from fastapi import FastAPI


from pydantic import BaseModel

class Details(BaseModel,extra='allow'):
    name:str
    roll:int

    def get_extra_field(self):
        return {k:v for k,v in self.__dict__.items() if k not in self.model_fields}

app=FastAPI()

@app.post("/")

async def Details(user:Details):
    print(user.get_extra_field())
    return {
        "name":user.name,
        "roll":user.roll
    }
    

