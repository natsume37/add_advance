from enum import Enum
import uvicorn
from fastapi import FastAPI
from run_json import YouDaoFanYi

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 继承Enum类、限制url参数
class Name(str, Enum):
    name1 = "小明"
    name2 = "小华"
    name3 = "小李"


@app.get("/hello/{name}")
async def say_hello(name: Name):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def pic(item_id: int):
    return {"items": item_id}


@app.get("/fanyi/{text:str}")
async def index4(text: str):
    res = YouDaoFanYi(text).main()
    return res


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8090)
