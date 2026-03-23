from typing import Dict
from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from model.Docs_type import docs_input,docs_response,Metadata
from Services.LLM import GPT_Edit
Data :Dict[int,docs_response] = {}
ID :int= 1

TTTTTT = "some_metadata"

async def Add_Data(D: docs_input):
    global ID  
    if ID is None:
        raise ValueError("ID is Invalid")
    try:
        if ID in Data.keys():
            raise ValueError("ID Already Exists")
        
        Memory = D.model_dump()
        Memory["MetaData"] = Metadata()# Added quotes
        Memory["ID"] = ID            # Added quotes
        list_of_items = list(Data.values()) 
        print(list_of_items)
        if list_of_items:
            if Memory['text'] in list_of_items:
                raise ValueError("Already Existed")
        Data[ID] = Memory
        
        current_id = ID
        ID += 1
        print("I was here", Data[current_id])
        return Data[current_id]
        
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")

async def Remove_data(Id:int):
    global ID  
    if ID is None:
        raise ValueError("ID is Invalid")
    try:
        if Id not in Data.keys():
            raise ValueError("ID Does not Exists ")
        
        del Data[Id]
        return JSONResponse(status_code=204,content={'msg':'Data Was Successfully Deleted'})
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")
    
async def All_docs():
    try:
        if Data:
            return Data
        raise ValueError('Data is Empty')
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")
    
async def Get_doc(Id:int):
    try:
        if Id in Data.keys():
            return Data[Id]
        raise ValueError("ID Doesnt Exist")
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")
 
async def Edit_data(Id:int , D:docs_input):
    try:
        if Id in Data.keys():
            Memory = D.model_dump()
            Memory["MetaData"] = Metadata()# Added quotes
            Memory["ID"] = Id 
            Data[Id] = Memory
            return Data[Id]
        raise ValueError("ID Doesnt Exist")
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")
 
async def Edit_data_GPT(Id:int):
    try:
        if Id in Data.keys():
            Data[Id]['text'] = await GPT_Edit(Data[Id]['text'] )
            return Data[Id]
        raise ValueError("ID Doesnt Exist")
    except Exception as e:
        # Combined into a single string message
        raise ValueError(f"Something Went Wrong Try Again Later: {e}")
 



