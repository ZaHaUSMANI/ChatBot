from fastapi import FastAPI
import uvicorn
from Routes.V1.data import Router as Data_route

app =FastAPI(title='Task - FastAPI Task')
app.include_router(Data_route)

if __name__ == "__main__":
     uvicorn.run(app= 'main:app',host= '0.0.0.0',port=8000,reload=True)