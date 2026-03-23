from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse
from openai import OpenAI
from fastapi import HTTPException,Query

load_dotenv()

Api_key = os.getenv('API_KEY')
BaseUrl = os.getenv('Base_Url')
ModelName = os.getenv('model_name')
client = OpenAI(api_key= Api_key , base_url= BaseUrl)

Context :str = ''

async def GPT_Summary(Input:str):
    try:
        Prompt = f"""Act as a professional text synthesizer. Your sole task is to provide a formal summary of the following input. 
        The summary must be concise and strictly under 10 words.and u must not about any other thing just whats 
        given to u .Input: {Input}"""

        Response = client.responses.create(input = Prompt , model = ModelName)
        Response = Response.model_dump()
        if Response['error'] is None:
            return Response['output'][1]['content'][0]['text']
        raise ValueError(Response['error'])
    except Exception as e:
        raise ValueError(str(e))

async def GPT_Edit(Input:str):
    try:
        prompt = f"""Act as a professional text synthesizer. Your sole task is to rewrite the entire text while keeping
        almost all the data not editing and maintaining the details about the data dont add useless prompt\
        just keep it to the point related to data make the tone clean and rewrite to informal
        Input: {Input}"""

        Response = client.responses.create(input = prompt , model = ModelName)
        Response = Response.model_dump()
        if Response['error'] is None:
            return Response['output'][1]['content'][0]['text']
        raise ValueError(Response['error'])
    except Exception as e:
        raise ValueError(str(e))
  
async def Set_context(Context1:str):
    global Context
    try:
        
        Context = Context1
        return JSONResponse(status_code= 201 , content= "Context Sucessfull Set")
    except Exception as e:
        raise ValueError('Something Went Wrong at setting ID')
    

async def Context_Based_Answering(Prompt:str = Query(...,max_length=400) ):
    global Context
    if len(Context) < 3:
        raise ValueError('Context Not Set Please Set Context')
    try:
        Input = f"""
            You are a text-grounded assistant.

            STRICT RULES:
            - Use ONLY the information present in the provided Context.
            - Do NOT add, assume, infer, or hallucinate any information.
            - If something is not explicitly stated in the Context, say: "Not specified in the text."
            - Answer directly and precisely. No sugar coating.

            TASK TYPES YOU MAY BE ASKED TO PERFORM:
            1. Answer factual questions whose answers must come ONLY from the Context.
            2. Transform the text without changing meaning, including:
            - Simplification
            - Rewriting for clarity
            - Changing tone (e.g., formal ↔ informal)
            3. Produce structured outputs derived strictly from the Context, such as:
            - Key points
            - Rules or obligations
            - Do’s and Don’ts
            - Step-by-step summaries (if applicable)

            CONTEXT (authoritative source — do not go beyond this):
            {Context}

            USER REQUEST (respond strictly using the Context):
            {Prompt}
                        """

        Response = client.responses.create(input = Input , model = ModelName)
        Response = Response.model_dump()
        if Response['error'] is None:
            return Response['output'][1]['content'][0]['text']
        raise ValueError(Response['error'])
    except Exception as e:
        raise ValueError(str(e))



# - Ask factual questions whose answers must come only from the stored text
# - Request transformations such as:
#   - Simplification
#   - Rewriting for clarity
#   - Tone change (formal -> informal)
# - Ask for structured outputs derived from the text, such as:
#   - Key points
#   - Rules or obligations
#   - Do’s and Don’ts