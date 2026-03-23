from fastapi import APIRouter,HTTPException,Query
from fastapi.responses import JSONResponse
from model.Docs_type import docs_input,docs_response
from Memory.Db import Add_Data,All_docs,Remove_data,Get_doc,Edit_data,Edit_data_GPT
from typing import Dict
from Services.LLM import GPT_Summary,Context_Based_Answering,Set_context
Router = APIRouter(prefix='/Data',tags=['User'])


@Router.get('/')
async def get_Status():
    return JSONResponse(status_code=200 , content={'msg':'API Works'})

@Router.post('/Add_Context_Doc',status_code=201,response_model=docs_response)
async def Add_data(text:docs_input):
    try:
        return await Add_Data(text)
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
    
@Router.get('/Get All Data',response_model=Dict[int,docs_response])
async def get_all():
    try:
        return await All_docs()
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
        
@Router.delete('/Delete Docs',status_code=204)
async def Delete_Docs(ID:int):
    try:
        return await Remove_data(ID)
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
        
@Router.get('/Get By ID Docs',response_model=docs_response)
async def getByID(Id:int):
    try:
        return await Get_doc(Id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
        
@Router.put('/update_doc',status_code=200,response_model=docs_response)
async def Update(Id:int,Data:docs_input):
    try:
        return await Edit_data(Id,Data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
         
@Router.get('/GetSummaryByID')
async def getSummary(Id:int):
    try:
        Data = await Get_doc(Id)
        return await GPT_Summary(Data['text'])
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))

@Router.get('/Edit Using ChatGPT',response_model=docs_response)
async def GPT_EDIT(Id:int):
    try:
        return await Edit_data_GPT(Id)  
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
    
@Router.get('/Edit Using ChatGPT',response_model=docs_response)
async def GPT_EDIT(Id:int):
    try:
        return await Edit_data_GPT(Id)  
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))

@Router.post('/SetContext/{ContextID}',status_code=201)
async def Set_Context(ContextID:int):
    try:
        Context = await Get_doc(ContextID)
        return await Set_context(Context['text'])
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
    
@Router.post('/Context_base_answer',status_code=201)
async def Context_Answer(prompt:str= Query(...,max_length=400)):
    try:
        return await  Context_Based_Answering(prompt)
    except ValueError as e:
        raise HTTPException(status_code=400, detail= str(e))
    except HTTPException:
        raise
    except HTTPException as e:
        raise HTTPException(status_code=500, detail= str(e))
